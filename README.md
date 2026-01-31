# 📧 Bulk Email Sender

A Python script for sending personalized bulk emails with attachments via Gmail's SMTP server. Perfect for job applications, newsletters, or marketing campaigns.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

- 📁 **File-based configuration** - No hardcoded emails or content
- 📎 **Attachment support** - Send PDFs, documents, or any files
- ⏱️ **Smart rate limiting** - Avoids Gmail sending limits
- 📝 **HTML email support** - Rich formatting and styling
- 🛡️ **Error handling** - Continue sending even if some emails fail
- 📊 **Progress tracking** - See real-time sending status

## 📋 Prerequisites

- Python 3.8 or higher
- Gmail account with 2-factor authentication enabled
- App Password (16-character) from Google

## 🚀 Quick Start

### 1. Clone & Setup

```bash
# Clone repository
git clone https://github.com/yourusername/bulk-email-sender.git
cd bulk-email-sender

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Gmail

1. Enable 2-factor authentication in your Google Account
2. Generate an App Password:
   - Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
   - Select "Mail" and "Other (Custom name)"
   - Name it "Bulk Email Script"
   - Copy the 16-character password

### 3. Create Required Files

Create these files in your project directory:

**1. `emails_list.txt`** - One email per line
```
recipient1@example.com
recipient2@company.com
recipient3@gmail.com
```

**2. `subject.txt`** - Email subject line
```
Job Application: Senior Developer Position
```

**3. `mail_body.txt`** - HTML or plain text email body
```html
Dear Hiring Manager,

<p>I am writing to apply for the Senior Developer position...</p>

<p>Best regards,<br>
Your Name</p>
```

**4. `resume.pdf`** - Your attachment file (rename as needed)

### 4. Configure Script

Edit the configuration section in `bulk_email.py`:

```python
# --- CONFIGURATION ---
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "xxxx xxxx xxxx xxxx"  # Your 16-digit App Password

# File Names
FILES = {
    "list": "emails_list.txt",
    "subject": "subject.txt",
    "body": "mail_body.txt",
    "attachment": "resume.pdf"
}
```

### 5. Run the Script

```bash
python bulk_email.py
```

## 📁 Project Structure

```
bulk-email-sender/
├── bulk_email.py          # Main script
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (optional)
├── .gitignore           # Git ignore file
├── emails_list.txt      # Recipient emails
├── subject.txt          # Email subject
├── mail_body.txt        # Email body content
└── resume.pdf          # Attachment file
```

## ⚙️ Configuration Options

### Email Content Customization

For personalized emails, modify the `prepare_message` function:

```python
# Add personalization
body_personalized = body_content.replace("{name}", recipient_name)
msg.attach(MIMEText(body_personalized, 'html'))
```

### Adjust Sending Delay

Change the delay between emails (default: 15 seconds):

```python
# For faster sending (riskier)
time.sleep(5)

# For safer sending
time.sleep(30)
```

### Environment Variables (Recommended)

For better security, use a `.env` file:

```env
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
```

Update the script to read from environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("GMAIL_USER")
SENDER_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
```

## 🛠️ Advanced Usage

### Batch Processing

Split large email lists into batches:

```python
# Create batches of 50 emails
batch_size = 50
for i in range(0, len(lines), batch_size):
    batch = lines[i:i+batch_size]
    # Process batch with longer delay between batches
    time.sleep(300)  # 5 minutes between batches
```

### Logging Results

Add logging to track successful/failed sends:

```python
import logging

logging.basicConfig(
    filename='email_log.csv',
    format='%(asctime)s,%(message)s',
    level=logging.INFO
)

# Log each send
logging.info(f"SUCCESS,{recipient_email}")
```

## ⚠️ Important Notes

### Gmail Limits
- **Daily limit**: 500 emails per day
- **Per minute limit**: 60-100 emails
- **Attachment size**: 25MB maximum

### Best Practices
1. Always test with 1-2 emails first
2. Use realistic sending delays (15-30 seconds)
3. Monitor your Gmail account for any restrictions
4. Keep your App Password secure

## 🐛 Troubleshooting

### Common Issues

**"SMTP Authentication Error"**
- Verify 2-factor authentication is enabled
- Regenerate App Password
- Check for extra spaces in password

**"Attachment not found"**
- Ensure file exists in same directory
- Check file name spelling
- Verify file permissions

**"Daily limit exceeded"**
- Wait 24 hours or use multiple Gmail accounts
- Reduce number of emails per day

### Debug Mode

Add debug output by modifying SMTP connection:

```python
server = smtplib.SMTP('smtp.gmail.com', 587)
server.set_debuglevel(1)  # Show debug output
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⭐ Support

If you find this project helpful, please give it a star! ⭐

---

## 📧 Contact

For questions or support, please open an issue on GitHub.

**Happy Emailing!** 🚀
