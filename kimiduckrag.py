#!/usr/bin/env python3
"""
KimiDuckRAG - DuckDB-based RAG for OpenClaw Agent Memories
No external dependencies beyond duckdb
"""

import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

# Try to import duckdb, fallback to JSON if not available
try:
    import duckdb
    DUCKDB_AVAILABLE = True
except ImportError:
    DUCKDB_AVAILABLE = False
    print("⚠️  DuckDB not available, using JSON fallback")

class KimiDuckRAG:
    """DuckDB-based RAG for agent memories"""
    
    def __init__(self, db_path: str = None):
        self.rag_dir = Path.home() / ".openclaw/workspace/kimirag"
        self.rag_dir.mkdir(parents=True, exist_ok=True)
        
        if db_path is None:
            db_path = self.rag_dir / "memories.db"
        
        self.db_path = db_path
        self.json_path = self.rag_dir / "memories.json"
        
        if DUCKDB_AVAILABLE:
            self.con = duckdb.connect(str(db_path))
            self._init_db()
        else:
            self.con = None
            self._init_json()
    
    def _init_db(self):
        """Initialize DuckDB schema"""
        self.con.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id VARCHAR PRIMARY KEY,
                content TEXT NOT NULL,
                category VARCHAR DEFAULT 'general',
                tags VARCHAR[],
                links VARCHAR[],
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                source VARCHAR DEFAULT 'Kimi'
            )
        """)
        
        # Create full-text search index
        try:
            self.con.execute("""
                CREATE INDEX IF NOT EXISTS idx_content ON memories USING FTS(content)
            """)
        except:
            pass  # FTS might not be available
    
    def _init_json(self):
        """Initialize JSON storage fallback"""
        if not self.json_path.exists():
            with open(self.json_path, 'w') as f:
                json.dump([], f)
    
    def add_memory(self, content: str, category: str = "general", 
                  tags: List[str] = None, links: List[str] = None) -> str:
        """Add a memory to the RAG"""
        
        memory_id = hashlib.md5(f"{content}{datetime.now()}".encode()).hexdigest()[:12]
        
        if DUCKDB_AVAILABLE and self.con:
            self.con.execute("""
                INSERT INTO memories (id, content, category, tags, links)
                VALUES (?, ?, ?, ?, ?)
            """, (memory_id, content, category, tags or [], links or []))
            self.con.commit()
        else:
            # JSON fallback
            with open(self.json_path, 'r') as f:
                memories = json.load(f)
            
            memories.append({
                "id": memory_id,
                "content": content,
                "category": category,
                "tags": tags or [],
                "links": links or [],
                "created_at": datetime.now().isoformat(),
                "source": "Kimi"
            })
            
            with open(self.json_path, 'w') as f:
                json.dump(memories, f, indent=2)
        
        return memory_id
    
    def search(self, query: str, limit: int = 10) -> List[Dict]:
        """Search memories"""
        
        if DUCKDB_AVAILABLE and self.con:
            try:
                # Try FTS search first
                results = self.con.execute("""
                    SELECT id, content, category, tags, links, created_at
                    FROM memories
                    WHERE content ILIKE ?
                    ORDER BY created_at DESC
                    LIMIT ?
                """, (f"%{query}%", limit)).fetchall()
                
                return [
                    {
                        "id": r[0],
                        "content": r[1][:500] + "..." if len(r[1]) > 500 else r[1],
                        "category": r[2],
                        "tags": r[3],
                        "links": r[4],
                        "created_at": r[5]
                    }
                    for r in results
                ]
            except Exception as e:
                print(f"DuckDB search error: {e}")
                return []
        else:
            # JSON fallback search
            with open(self.json_path, 'r') as f:
                memories = json.load(f)
            
            results = []
            query_lower = query.lower()
            
            for m in memories:
                if (query_lower in m.get("content", "").lower() or
                    query_lower in m.get("category", "").lower() or
                    any(query_lower in t.lower() for t in m.get("tags", []))):
                    results.append(m)
            
            return sorted(results, 
                         key=lambda x: x.get("created_at", ""), 
                         reverse=True)[:limit]
    
    def get_recent(self, limit: int = 50) -> List[Dict]:
        """Get recent memories"""
        
        if DUCKDB_AVAILABLE and self.con:
            results = self.con.execute("""
                SELECT id, content, category, tags, created_at
                FROM memories
                ORDER BY created_at DESC
                LIMIT ?
            """, (limit,)).fetchall()
            
            return [
                {
                    "id": r[0],
                    "content": r[1][:300] + "..." if len(r[1]) > 300 else r[1],
                    "category": r[2],
                    "tags": r[3],
                    "created_at": r[4]
                }
                for r in results
            ]
        else:
            with open(self.json_path, 'r') as f:
                memories = json.load(f)
            
            return sorted(memories, 
                         key=lambda x: x.get("created_at", ""), 
                         reverse=True)[:limit]
    
    def get_stats(self) -> Dict:
        """Get RAG statistics"""
        
        if DUCKDB_AVAILABLE and self.con:
            count = self.con.execute("SELECT COUNT(*) FROM memories").fetchone()[0]
            categories = self.con.execute(
                "SELECT category, COUNT(*) FROM memories GROUP BY category"
            ).fetchall()
        else:
            with open(self.json_path, 'r') as f:
                memories = json.load(f)
            count = len(memories)
            categories = {}
            for m in memories:
                cat = m.get("category", "general")
                categories[cat] = categories.get(cat, 0) + 1
            categories = list(categories.items())
        
        return {
            "total_memories": count,
            "categories": categories,
            "storage": "DuckDB" if DUCKDB_AVAILABLE else "JSON",
            "db_path": str(self.db_path) if DUCKDB_AVAILABLE else str(self.json_path)
        }
    
    def close(self):
        """Close database connection"""
        if self.con:
            self.con.close()

# CLI
if __name__ == "__main__":
    import argparse
    
    rag = KimiDuckRAG()
    parser = argparse.ArgumentParser(description="KimiDuckRAG")
    parser.add_argument("--add", "-a", help="Add memory")
    parser.add_argument("--category", "-c", default="general")
    parser.add_argument("--tags", "-t", help="Comma-separated tags")
    parser.add_argument("--search", "-s", help="Search query")
    parser.add_argument("--recent", action="store_true", help="Recent memories")
    parser.add_argument("--stats", action="store_true", help="Show stats")
    
    args = parser.parse_args()
    
    if args.add:
        tags = args.tags.split(",") if args.tags else []
        mid = rag.add_memory(args.add, args.category, tags)
        print(f"✅ Memory added: {mid}")
    
    elif args.search:
        results = rag.search(args.search)
        print(f"🔍 Found {len(results)} memories:")
        for r in results:
            print(f"  [{r['category']}] {r['content'][:100]}...")
    
    elif args.recent:
        memories = rag.get_recent()
        print(f"📅 Recent memories ({len(memories)} total):")
        for m in memories[:10]:
            print(f"  [{m['created_at'][:10]}] {m['content'][:80]}...")
    
    elif args.stats:
        stats = rag.get_stats()
        print(f"📊 KimiDuckRAG Stats:")
        print(f"  Total memories: {stats['total_memories']}")
        print(f"  Storage: {stats['storage']}")
        print(f"  Path: {stats['db_path']}")
        print(f"  Categories: {stats['categories']}")
    
    else:
        print("KimiDuckRAG - Personal Memory System")
        print("\nUsage:")
        print("  python3 kimiduckrag.py --add 'Memory text' --category 'Projects' --tags 'important,urgent'")
        print("  python3 kimiduckrag.py --search 'keyword'")
        print("  python3 kimiduckrag.py --recent")
        print("  python3 kimiduckrag.py --stats")
    
    rag.close()
