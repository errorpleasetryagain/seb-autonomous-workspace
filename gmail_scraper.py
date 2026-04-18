#!/usr/bin/env python3
"""
Gmail Affiliate Updates Scraper
Monitors Gmail for affiliate programme updates and saves to JSON
"""

import os
import json
import base64
import pickle
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Configuration
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
TOKEN_FILE = 'token.pickle'
CREDENTIALS_FILE = 'credentials.json'
OUTPUT_FILE = 'affiliate_updates.json'

# Keywords to search for
SEARCH_KEYWORDS = [
    'medichecks', 'optimale', 'affiliate', 'referral', 'commission',
    'descript', 'partnerstack', 'awin', 'approved', 'rejected',
    'application', 'verification', 'fueloptimal', 'maleoptimal'
]

# Senders to prioritize
PRIORITY_SENDERS = [
    'noreply@medichecks.com',
    'support@optimale.co.uk',
    'partners@descript.com',
    'noreply@partnerstack.com',
    'notifications@vercel.com',
    'noreply@github.com'
]

def get_gmail_service():
    """Authenticate and return Gmail API service"""
    creds = None
    
    # Load existing token
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    
    # Refresh or create new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"❌ Error: {CREDENTIALS_FILE} not found!")
                print("Download from Google Cloud Console → APIs & Services → Credentials")
                return None
            
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save token for future runs
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    
    return build('gmail', 'v1', credentials=creds)

def search_affiliate_emails(service, days_back=7):
    """Search Gmail for affiliate-related emails"""
    
    # Build query
    after_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y/%m/%d')
    
    # Search by keywords OR priority senders
    queries = []
    
    # Keyword-based search
    keyword_query = ' OR '.join([f'subject:{kw}' for kw in SEARCH_KEYWORDS])
    queries.append(f'({keyword_query}) after:{after_date}')
    
    # Sender-based search
    for sender in PRIORITY_SENDERS:
        queries.append(f'from:{sender} after:{after_date}')
    
    all_messages = []
    
    for query in queries:
        try:
            results = service.users().messages().list(
                userId='me',
                q=query,
                maxResults=50
            ).execute()
            
            messages = results.get('messages', [])
            all_messages.extend(messages)
            
        except Exception as e:
            print(f"Query failed: {e}")
    
    # Remove duplicates by message ID
    seen = set()
    unique_messages = []
    for msg in all_messages:
        if msg['id'] not in seen:
            seen.add(msg['id'])
            unique_messages.append(msg)
    
    return unique_messages

def parse_email(service, msg_id):
    """Extract key info from an email"""
    
    try:
        message = service.users().messages().get(
            userId='me',
            id=msg_id,
            format='full'
        ).execute()
        
        headers = message['payload']['headers']
        
        # Extract headers
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
        date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown')
        
        # Get body (prefer text/plain)
        body = ""
        if 'parts' in message['payload']:
            for part in message['payload']['parts']:
                if part['mimeType'] == 'text/plain':
                    body = base64.urlsafe_b64decode(
                        part['body']['data']
                    ).decode('utf-8', errors='ignore')
                    break
        elif 'body' in message['payload'] and 'data' in message['payload']['body']:
            body = base64.urlsafe_b64decode(
                message['payload']['body']['data']
            ).decode('utf-8', errors='ignore')
        
        # Truncate body
        body_preview = body[:500] + "..." if len(body) > 500 else body
        
        # Classify email
        category = classify_email(subject, sender, body)
        
        return {
            'id': msg_id,
            'subject': subject,
            'sender': sender,
            'date': date,
            'category': category,
            'body_preview': body_preview,
            'link': f"https://mail.google.com/mail/u/0/#inbox/{msg_id}"
        }
        
    except Exception as e:
        return {
            'id': msg_id,
            'error': str(e)
        }

def classify_email(subject, sender, body):
    """Classify email by importance"""
    
    text = (subject + ' ' + sender + ' ' + body).lower()
    
    # Priority classifications
    if any(word in text for word in ['approved', 'accepted', 'welcome', 'confirmed']):
        return '✅ APPROVED'
    elif any(word in text for word in ['rejected', 'declined', 'unfortunately']):
        return '❌ REJECTED'
    elif any(word in text for word in ['verification', 'review', 'pending', 'under review']):
        return '⏳ PENDING'
    elif any(word in text for word in ['commission', 'payment', 'payout', 'earnings']):
        return '💰 PAYMENT'
    elif any(word in text for word in ['password', 'login', 'security', 'verify']):
        return '🔒 SECURITY'
    else:
        return '📧 UPDATE'

def save_updates(updates):
    """Save updates to JSON file"""
    
    data = {
        'last_run': datetime.now().isoformat(),
        'total_updates': len(updates),
        'updates': sorted(updates, key=lambda x: x.get('date', ''), reverse=True)
    }
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Saved {len(updates)} updates to {OUTPUT_FILE}")

def print_summary(updates):
    """Print a readable summary"""
    
    if not updates:
        print("\n📭 No affiliate updates found")
        return
    
    print("\n" + "="*60)
    print("📬 AFFILIATE UPDATE SUMMARY")
    print("="*60)
    
    # Group by category
    by_category = {}
    for u in updates:
        cat = u.get('category', '📧 UPDATE')
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(u)
    
    # Print by priority
    priority_order = ['✅ APPROVED', '❌ REJECTED', '💰 PAYMENT', '⏳ PENDING', '🔒 SECURITY', '📧 UPDATE']
    
    for cat in priority_order:
        if cat in by_category:
            print(f"\n{cat} ({len(by_category[cat])})")
            print("-" * 40)
            for u in by_category[cat][:3]:  # Show top 3 per category
                print(f"  📩 {u['subject'][:60]}")
                print(f"     From: {u['sender'][:40]}")
                print(f"     Date: {u['date'][:30]}")
                print(f"     Link: {u['link']}")
                print()

def main():
    """Main entry point"""
    
    print("🔍 Gmail Affiliate Scraper")
    print("="*40)
    
    # Check for credentials
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"\n❌ {CREDENTIALS_FILE} not found!")
        print("\nSetup instructions:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create project → Enable Gmail API")
        print("3. APIs & Services → Credentials → Create OAuth 2.0 Client ID")
        print("4. Download JSON, save as 'credentials.json' in this folder")
        print("5. Run this script again")
        return
    
    # Get Gmail service
    print("\n🔐 Authenticating with Gmail...")
    service = get_gmail_service()
    
    if not service:
        print("❌ Failed to authenticate")
        return
    
    # Search for emails
    print("\n📧 Searching for affiliate updates...")
    messages = search_affiliate_emails(service)
    print(f"Found {len(messages)} potential updates")
    
    # Parse each email
    print("\n📝 Processing emails...")
    updates = []
    for i, msg in enumerate(messages, 1):
        print(f"  [{i}/{len(messages)}] Parsing...", end='\r')
        update = parse_email(service, msg['id'])
        if 'error' not in update:
            updates.append(update)
    
    print(f"\n✓ Processed {len(updates)} emails")
    
    # Save and display
    save_updates(updates)
    print_summary(updates)
    
    print(f"\n📁 Full results saved to: {OUTPUT_FILE}")
    print("📋 Import this file into Notion or review manually")

if __name__ == '__main__':
    main()
