import smtplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# --- CONFIGURATION ---
SENDER_EMAIL = "" #add ur email
SENDER_PASSWORD = ""  # Your 16-digit App Password (get app passwords for g-account)

# File Names
FILES = {
    "list": "emails_list.txt",
    "subject": "subject.txt",
    "body": "mail_body.txt",
    "attachment": "resume.pdf"  # Ensure this matches your PDF name
}


def load_file_content(filename):
    """Reads text content from a file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"❌ Error: Could not find {filename}")
        return None


def send_bulk_emails():
    # 1. Load Static Content
    subject_text = load_file_content(FILES["subject"])
    body_content = load_file_content(FILES["body"])

    if not subject_text or not body_content:
        return

        # 2. Check Attachment
    if not os.path.exists(FILES["attachment"]):
        print(f"❌ Error: Attachment '{FILES['attachment']}' not found.")
        return

    # 3. Connect to SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("✅ Connected to Gmail Server")
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return

    # 4. Process Email List
    try:
        with open(FILES["list"], "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"❌ Error: {FILES['list']} not found.")
        return

    print(f"📂 Found {len(lines)} emails. Starting...")
    print("-" * 40)

    for line in lines:
        recipient_email = line.strip()

        if not recipient_email:
            continue  # Skip empty lines

        # --- PREPARE MESSAGE ---
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject_text

        # Attach Body (No name replacement needed anymore)
        msg.attach(MIMEText(body_content, 'html'))

        # Attach Resume
        try:
            with open(FILES["attachment"], "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {FILES['attachment']}",
                )
                msg.attach(part)
        except Exception as e:
            print(f"⚠️ Error attaching file for {recipient_email}: {e}")
            continue

        # --- SEND ---
        try:
            server.send_message(msg)
            print(f"🚀 Sent to: {recipient_email}")
        except Exception as e:
            print(f"❌ Failed to send to {recipient_email}: {e}")

        # Smart Delay (15-30 seconds is safest)
        time.sleep(15)

    server.quit()
    print("-" * 40)
    print("🏁 Batch Complete.")


if __name__ == "__main__":
    send_bulk_emails()
