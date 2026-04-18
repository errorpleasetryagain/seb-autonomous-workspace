#!/usr/bin/env python3
"""
KimiRAG - Personal Memory System for OpenClaw Agent
RAG (Retrieval-Augmented Generation) for storing and retrieving conversation memories
Uses DuckDB for local storage + embeddings
"""

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
import subprocess

# Config
MEMORY_DIR = Path.home() / ".openclaw/workspace/memory"
RAG_DB_DIR = Path.home() / ".openclaw/workspace/kimirag"
VAULT_DIR = RAG_DB_DIR / "vault"

class KimiRAG:
    """Personal RAG system for OpenClaw agent memories"""
    
    def __init__(self):
        self.vault_dir = VAULT_DIR
        self.vault_dir.mkdir(parents=True, exist_ok=True)
        self.ensure_structure()
    
    def ensure_structure(self):
        """Create Obsidian-like vault structure"""
        (self.vault_dir / "01 - Daily Logs").mkdir(exist_ok=True)
        (self.vault_dir / "02 - Projects").mkdir(exist_ok=True)
        (self.vault_dir / "03 - People").mkdir(exist_ok=True)
        (self.vault_dir / "04 - Decisions").mkdir(exist_ok=True)
        (self.vault_dir / "05 - Skills").mkdir(exist_ok=True)
        (self.vault_dir / "06 - Templates").mkdir(exist_ok=True)
    
    def create_memory_note(self, content: str, category: str = "Daily Logs", 
                          tags: List[str] = None, links: List[str] = None) -> str:
        """Create a new memory note in the vault"""
        
        timestamp = datetime.now().isoformat()
        date_str = datetime.now().strftime("%Y-%m-%d")
        
        # Generate unique ID
        note_id = hashlib.md5(f"{content}{timestamp}".encode()).hexdigest()[:8]
        
        # Build frontmatter
        frontmatter = {
            "id": note_id,
            "created": timestamp,
            "category": category,
            "tags": tags or [],
            "links": links or [],
            "source": "Kimi (OpenClaw Agent)"
        }
        
        # Format as Obsidian note
        note_content = f"""---
{json.dumps(frontmatter, indent=2)}
---

# Memory Note [{date_str}]

{content}

## Context
- **Category**: {category}
- **Tags**: {', '.join(tags or [])}
- **Related**: {', '.join(links or [])}

---
*This note was automatically created by KimiRAG*
"""
        
        # Save to vault
        folder_map = {
            "Daily Logs": "01 - Daily Logs",
            "Projects": "02 - Projects", 
            "People": "03 - People",
            "Decisions": "04 - Decisions",
            "Skills": "05 - Skills",
            "Templates": "06 - Templates"
        }
        
        folder = self.vault_dir / folder_map.get(category, "01 - Daily Logs")
        filename = f"{date_str}-{note_id}.md"
        filepath = folder / filename
        
        with open(filepath, 'w') as f:
            f.write(note_content)
        
        return str(filepath)
    
    def search_memories(self, query: str, limit: int = 10) -> List[Dict]:
        """Search memories using grep + simple scoring"""
        results = []
        
        # Simple grep-based search (can be enhanced with DuckDB)
        for md_file in self.vault_dir.rglob("*.md"):
            try:
                content = md_file.read_text()
                if query.lower() in content.lower():
                    # Extract frontmatter
                    lines = content.split('\n')
                    metadata = {}
                    in_frontmatter = False
                    
                    for line in lines:
                        if line.strip() == '---':
                            if in_frontmatter:
                                break
                            in_frontmatter = True
                            continue
                        if in_frontmatter and ':' in line:
                            key, val = line.split(':', 1)
                            metadata[key.strip()] = val.strip()
                    
                    results.append({
                        'file': str(md_file),
                        'metadata': metadata,
                        'preview': content[:500] + "..." if len(content) > 500 else content
                    })
            except Exception as e:
                continue
        
        return results[:limit]
    
    def get_recent_memories(self, days: int = 7) -> List[Dict]:
        """Get memories from last N days"""
        memories = []
        cutoff = datetime.now().timestamp() - (days * 24 * 3600)
        
        for md_file in self.vault_dir.rglob("*.md"):
            try:
                mtime = md_file.stat().st_mtime
                if mtime > cutoff:
                    content = md_file.read_text()
                    memories.append({
                        'file': str(md_file),
                        'date': datetime.fromtimestamp(mtime).isoformat(),
                        'preview': content[:200]
                    })
            except:
                continue
        
        return sorted(memories, key=lambda x: x['date'], reverse=True)
    
    def build_knowledge_graph(self):
        """Build [[wikilink]] graph from memories"""
        graph = {"nodes": [], "edges": []}
        
        for md_file in self.vault_dir.rglob("*.md"):
            try:
                content = md_file.read_text()
                # Extract wikilinks [[like this]]
                import re
                links = re.findall(r'\[\[([^\]]+)\]\]', content)
                
                graph["nodes"].append({
                    "id": md_file.stem,
                    "file": str(md_file),
                    "links": links
                })
                
                for link in links:
                    graph["edges"].append({
                        "source": md_file.stem,
                        "target": link
                    })
            except:
                continue
        
        return graph
    
    def export_for_obsidianrag(self) -> str:
        """Export vault path for ObsidianRAG integration"""
        return str(self.vault_dir)

# CLI interface
if __name__ == "__main__":
    import argparse
    
    rag = KimiRAG()
    parser = argparse.ArgumentParser(description="KimiRAG - Personal Memory System")
    parser.add_argument("--add", "-a", help="Add a new memory note")
    parser.add_argument("--category", "-c", default="Daily Logs", help="Category")
    parser.add_argument("--tags", "-t", help="Comma-separated tags")
    parser.add_argument("--search", "-s", help="Search memories")
    parser.add_argument("--recent", "-r", type=int, help="Get recent memories (days)")
    parser.add_argument("--vault-path", action="store_true", help="Print vault path")
    
    args = parser.parse_args()
    
    if args.add:
        tags = args.tags.split(",") if args.tags else []
        filepath = rag.create_memory_note(args.add, args.category, tags)
        print(f"✅ Memory saved: {filepath}")
    
    elif args.search:
        results = rag.search_memories(args.search)
        print(f"🔍 Found {len(results)} memories:")
        for r in results:
            print(f"  📄 {r['file']}")
            print(f"     Preview: {r['preview'][:100]}...")
    
    elif args.recent:
        memories = rag.get_recent_memories(args.recent)
        print(f"📅 Last {args.recent} days:")
        for m in memories:
            print(f"  {m['date'][:10]}: {m['file']}")
    
    elif args.vault_path:
        print(rag.export_for_obsidianrag())
    
    else:
        print("KimiRAG - Personal Memory System for OpenClaw")
        print(f"Vault location: {rag.vault_dir}")
        print("\nUsage:")
        print("  python3 kimirag.py --add 'Memory content' --category 'Projects'")
        print("  python3 kimirag.py --search 'keyword'")
        print("  python3 kimirag.py --recent 7")
