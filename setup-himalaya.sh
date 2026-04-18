#!/usr/bin/env bash
# Auto-configure Himalaya for affiliate email monitoring
# Usage: ./setup-himalaya.sh [email] [app-password]

EMAIL="${1:-adam.turton@gmail.com}"
APPPASS="${2:-}"

# Create config directory
mkdir -p ~/.config/himalaya

# Generate config
cat > ~/.config/himalaya/config.toml <<EOF
[accounts.gmail]
default = true
email = "$EMAIL"
display-name = "Adam Turton"

[accounts.gmail.imap]
host = "imap.gmail.com"
port = 993
login = "$EMAIL"
# Use app password (not regular Gmail password)
# Get from: myaccount.google.com/apppasswords
# passwd.command = "pass show email/gmail-app-password"

[accounts.gmail.smtp]
host = "smtp.gmail.com"
port = 465
login = "$EMAIL"
# passwd.command = "pass show email/gmail-app-password"

[accounts.gmail.mailbox-list]
drafts = "[Gmail]/Drafts"
sent = "[Gmail]/Sent Mail"
trash = "[Gmail]/Trash"

[listing]
[listing.messages]
page-size = 20

[message.read]
[message.read.headers]
show = ["From", "To", "Subject", "Date"]

# Affiliate senders to monitor
[affiliate-monitoring]
enabled = true
senders = [
  "noreply@medichecks.com",
  "support@optimale.co.uk",
  "partners@descript.com",
  "noreply@partnerstack.com"
]
EOF

echo "✅ Himalaya configured for $EMAIL"
echo ""
echo "Next: Get App Password from Google → myaccount.google.com/apppasswords"
echo "Then run: himalaya list"
