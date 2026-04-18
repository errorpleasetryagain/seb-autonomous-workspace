#!/bin/bash
# ============================================================
# Claude Code MCP + Skills Setup for Passive Income Portfolio
# Run this from Terminal on your Mac
# ============================================================

echo "========================================================"
echo "  Claude Code MCP Server Setup — Good Living Co Portfolio"
echo "========================================================"
echo ""

# ── SECTION 1: Remote MCP Servers (one-liner installs) ──────
echo "--- Remote MCP Servers (Cowork-matched) ---"
echo ""

echo "1/8 Adding Figma MCP..."
claude mcp add figma \
  --transport http \
  https://mcp.figma.com/mcp \
  2>/dev/null && echo "  ✓ Figma added" || echo "  ⚠ Figma may already exist or needs manual setup"

echo "2/8 Adding Ahrefs MCP..."
claude mcp add ahrefs \
  --transport http \
  https://api.ahrefs.com/mcp/mcp \
  2>/dev/null && echo "  ✓ Ahrefs added" || echo "  ⚠ Ahrefs may already exist or needs manual setup"

echo "3/8 Adding AirOps MCP..."
claude mcp add airops \
  --transport http \
  https://app.airops.com/mcp \
  2>/dev/null && echo "  ✓ AirOps added" || echo "  ⚠ AirOps may already exist or needs manual setup"

echo "4/8 Adding Cloudinary MCP..."
claude mcp add cloudinary \
  --transport sse \
  https://asset-management.mcp.cloudinary.com/sse \
  2>/dev/null && echo "  ✓ Cloudinary added" || echo "  ⚠ Cloudinary may already exist or needs manual setup"

echo "5/8 Adding Bitly MCP..."
claude mcp add bitly \
  --transport http \
  https://api-ssl.bitly.com/v4/mcp \
  2>/dev/null && echo "  ✓ Bitly added" || echo "  ⚠ Bitly may already exist or needs manual setup"

echo "6/8 Adding Windsor.ai MCP..."
claude mcp add windsor \
  --transport http \
  https://mcp.windsor.ai \
  2>/dev/null && echo "  ✓ Windsor.ai added" || echo "  ⚠ Windsor.ai may already exist or needs manual setup"

echo ""
echo "--- Google Search Console & Analytics (GitHub MCPs) ---"
echo ""

# ── SECTION 2: Google Search Console MCP ────────────────────
echo "7/8 Setting up Google Search Console MCP..."

GSC_DIR="$HOME/.claude/mcp-servers/mcp-gsc"
if [ ! -d "$GSC_DIR" ]; then
  echo "  Cloning AminForou/mcp-gsc..."
  mkdir -p "$HOME/.claude/mcp-servers"
  git clone https://github.com/AminForou/mcp-gsc.git "$GSC_DIR" 2>/dev/null
  if [ $? -eq 0 ]; then
    echo "  Installing dependencies..."
    cd "$GSC_DIR"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt -q 2>/dev/null
    deactivate
    cd - > /dev/null
    echo "  ✓ GSC MCP cloned and dependencies installed"
  else
    echo "  ✗ Failed to clone. Check your internet connection."
  fi
else
  echo "  ✓ GSC MCP already installed at $GSC_DIR"
fi

echo ""
echo "  ⚠ GOOGLE SEARCH CONSOLE — Manual Steps Required:"
echo "  ─────────────────────────────────────────────────"
echo "  1. Go to: https://console.cloud.google.com/"
echo "  2. Create a project (or use existing)"
echo "  3. Enable 'Google Search Console API'"
echo "  4. Go to Credentials → Create OAuth 2.0 Client ID"
echo "     - Application type: Desktop app"
echo "     - Download the JSON file"
echo "  5. Set environment variables:"
echo "     export GOOGLE_CLIENT_ID='your-client-id'"
echo "     export GOOGLE_CLIENT_SECRET='your-client-secret'"
echo "  6. Add to Claude Code:"
echo "     claude mcp add gsc -- python3 $GSC_DIR/venv/bin/python $GSC_DIR/gsc_server.py"
echo ""

# ── SECTION 3: Google Analytics MCP ─────────────────────────
echo "8/8 Setting up Google Analytics MCP..."

GA_DIR="$HOME/.claude/mcp-servers/google-analytics-mcp"
if ! pip show google-analytics-mcp > /dev/null 2>&1; then
  echo "  Installing google-analytics-mcp via pip..."
  pip install google-analytics-mcp -q 2>/dev/null
  if [ $? -eq 0 ]; then
    echo "  ✓ Google Analytics MCP installed"
  else
    echo "  Trying clone method instead..."
    mkdir -p "$HOME/.claude/mcp-servers"
    git clone https://github.com/surendranb/google-analytics-mcp.git "$GA_DIR" 2>/dev/null
    if [ $? -eq 0 ]; then
      cd "$GA_DIR" && pip install . -q 2>/dev/null && cd - > /dev/null
      echo "  ✓ Google Analytics MCP installed from source"
    else
      echo "  ✗ Failed to install. Check your internet connection."
    fi
  fi
else
  echo "  ✓ Google Analytics MCP already installed"
fi

echo ""
echo "  ⚠ GOOGLE ANALYTICS — Manual Steps Required:"
echo "  ─────────────────────────────────────────────"
echo "  1. Go to: https://console.cloud.google.com/"
echo "  2. Enable 'Google Analytics Data API'"
echo "  3. Create a Service Account"
echo "     - Download the JSON key file"
echo "     - Save it to: ~/.claude/mcp-servers/ga-service-account.json"
echo "  4. In Google Analytics (admin), add the service account"
echo "     email as a Viewer on your GA4 properties"
echo "  5. Get your GA4 Property ID from Analytics → Admin → Property Settings"
echo "  6. Set environment variables:"
echo "     export GOOGLE_ANALYTICS_SERVICE_ACCOUNT_KEY_PATH=~/.claude/mcp-servers/ga-service-account.json"
echo "     export GOOGLE_ANALYTICS_GA4_PROPERTY_ID='properties/YOUR_ID'"
echo "  7. Add to Claude Code:"
echo "     claude mcp add google-analytics -- google-analytics-mcp"
echo ""

# ── Summary ─────────────────────────────────────────────────
echo "========================================================"
echo "  SETUP SUMMARY"
echo "========================================================"
echo ""
echo "  ✅ Ready to use (auto-auth on first call):"
echo "     • Figma       — Design → Code pipeline"
echo "     • Ahrefs      — SEO & keyword research"
echo "     • AirOps      — AI search optimisation"
echo "     • Cloudinary   — Image/video management"
echo "     • Bitly        — Link tracking"
echo "     • Windsor.ai   — Multi-source analytics"
echo ""
echo "  ⚠ Needs Google Cloud setup first:"
echo "     • Google Search Console — OAuth credentials"
echo "     • Google Analytics      — Service account key"
echo ""
echo "  Both Google MCPs need a Google Cloud project with"
echo "  the relevant APIs enabled. Create one at:"
echo "  https://console.cloud.google.com/"
echo ""

echo "=== Current MCP Server Config ==="
claude mcp list 2>/dev/null || echo "Run 'claude mcp list' to see all configured servers"

echo ""
echo "=== Quick Test Commands for Claude Code ==="
echo "  'What keywords is maleoptimal.co.uk ranking for?'  (Ahrefs)"
echo "  'Show my Figma files'                               (Figma)"
echo "  'List my Cloudinary images'                          (Cloudinary)"
echo "  'Shorten this URL: maleoptimal.co.uk/best-trt-uk'  (Bitly)"
echo "  'How many clicks did my sites get this week?'       (GSC)"
echo "  'Show my GA4 traffic for the last 7 days'           (GA)"
echo ""
echo "Done! Run 'claude' to start Claude Code."
