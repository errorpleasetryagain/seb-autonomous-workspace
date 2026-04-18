#!/bin/bash
# Daily Log Creator for Obsidian Vault
# Creates YYYY-MM-DD.md in ~/KimiRAG-Vault/
# Run via cron: 0 0 * * * /Users/adamturton/.openclaw/workspace/scripts/create-daily-log.sh

VAULT_DIR="$HOME/KimiRAG-Vault"
DATE=$(date +%Y-%m-%d)
DAY=$(date +%A)
MONTH=$(date +%B)
YEAR=$(date +%Y)

FILE="$VAULT_DIR/$DATE.md"

# Don't overwrite existing
if [ -f "$FILE" ]; then
  echo "Log already exists: $FILE"
  exit 0
fi

# Create log template
cat > "$FILE" << EOF
---
created: $DATE
category: "Daily Log"
tags: [daily, $(date +%Y-%m), $DAY]
---

# Daily Log — $DAY, $MONTH $DATE

## 🎯 Goals for Today
- [ ] 
- [ ] 
- [ ] 

## 📝 Notes & Thoughts


## ✅ Completed
- 

## 📊 Metrics
- Revenue: £
- Visitors: 
- Content published: 

## 🚀 Tomorrow's Priority
1. 
2. 
3. 

---

*Created automatically at $(date +%H:%M)*
EOF

echo "Created daily log: $FILE"
