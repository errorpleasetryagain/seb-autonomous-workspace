#!/usr/bin/env python3
"""
Himalaya Affiliate Email Filter
Monitors Gmail via IMAP and saves affiliate-related emails
"""

import subprocess
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

# Config
HIMALAYA_CONFIG = Path.home() / '.config/himalaya/config.toml'
AFFILIATE_SENDERS = [
    'noreply@medichecks.com',
    'support@optimale.co.uk', 
    'partners@descript.com',
    'noreply@partnerstack.com',
    'affiliates@aweber.com'
]

# Keywords in subject/body
AFFILIATE_KEYWORDS = [
    'approved', 'rejected', 'application', 'commission',
    'payout', 'payment', 'verification',
    'affiliate', 'referral', 'partner program'
]

def run_himalaya():
    """List emails from himalaya"""
    try:
        result = subprocess.run(
            ['himalaya', 'list', '--output', 'json'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            print(f"❌ Himalaya failed: {result.stderr}")
            return []
            
        emails = json.loads(result.stdout)
        
        # Filter for affiliate emails
        affiliate_emails = []
        for email in emails:
            msg_id = email.get('id', '')
            from_addr = email.get('from', {}).get('address', '')
            subject = email.get('subject', '')
            body = email.get('body', '')
            
            # Check if affiliate-related
            is_affiliate = (
                any(sender.lower() in from_addr.lower() for sender in AFFILIATE_SENDERS) or
                any(kw in subject.lower() or kw in body.lower() for kw in AFFILIATE_KEYWORDS)
            )
            
            if is_affiliate:
                affiliate_emails.append({
                    'id': msg_id,
                    'from': from_addr,
                    'subject': subject,
                    'date': email.get('date'),
                    'status': classify_status(subject, body),
                    'preview': body[:200] + '...' if len(body) > 200 else body
                })
        
        return affiliate_emails
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def classify_status(subject, body):
    """Classify email status"""
    text = (subject + ' ' + body).lower()
    
    if any(word in text for word in ['approved', 'accepted', 'welcome', 'confirmed']):
        return '✅ APPROVED'
    elif any(word in text for word in ['rejected', 'declined', 'unfortunately', 'sorry']):
        return '❌ REJECTED'
    elif any(word in text for word in ['verification', 'review', 'pending', 'under review']):
        return '⏳ PENDING'
    elif any(word in text for word in ['payout', 'payment', 'commission', 'earnings']):
        return '💰 PAYMENT'
    elif any(word in text for word in ['password', 'login', 'security', 'suspicious']):
        return '🔒 SECURITY'
    else:
        return '📧 UPDATE'

def save_updates(emails):
    """Save to JSON"""
    data = {
        'last_check': datetime.now().isoformat(),
        'total_affiliate_emails': len(emails),
        'emails': emails
    }
    
    output_path = Path.home() / '.openclaw/workspace/affiliate_email_updates.json'
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2, default=str)
    
    print(f"💾 Saved {len(emails)} emails to {output_path}")

def print_summary(emails):
    """Display results"""
    if not emails:
        print("\n📭 No affiliate emails found")
        return
        
    print(f"\n📬 AFFILIATE EMAILS: {len(emails)} found\n")
    print("=" * 50)
    
    status_counts = {}
    for e in emails:
        s = e['status']
        status_counts[s] = status_counts.get(s, 0) + 1
    
    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count}")
    
    print(f"\n💡 Check: {HIMALAYA_CONFIG.parent}/affiliate_email_updates.json")
    print("💡 Notion: Import this to your Affiliate Programmes database")

if __name__ == '__main__':
    print("🔍 Checking affiliate emails via Himalaya...")
    emails = run_himalaya()
    save_updates(emails)
    print_summary(emails)
