# Outlook Email Sender
## mail.py
A simple Python script to send emails using Microsoft Outlook.

## Description

This script allows you to send emails programmatically through your installed Microsoft Outlook application using Python. It uses the `win32com` library to interact with Outlook.

## Requirements

- Windows operating system
- Microsoft Outlook installed and configured with an email account
- Python 3.x
- pywin32 package

## Installation

1. Ensure you have Python installed
2. Install the required package:
   ```
   pip install pywin32
   ```

## Usage

1. Import the script or run it directly:
   ```python
   python mail.py
   ```

2. To use in your own project:
   ```python
   from mail import send_outlook_email
   send_outlook_email()
   ```

3. Customize the email by modifying these parameters in the code:
   - `mail.Subject` - Email subject
   - `mail.To` - Recipient email address
   - `mail.Body` - Email content
   - Uncomment and modify the `mail.Attachments.Add()` line to include attachments

## Notes

- The script uses your default Outlook profile
- Ensure Outlook is properly configured before running the script
- You may need to handle Outlook security prompts on first run


 ## main.py

A Python module for sending emails using SMTP.

## Features
- Send emails with text and HTML content
- Support for attachments
- SMTP authentication
- TLS encryption support

## Requirements
- Python 3.6+
- `smtplib` (built-in)
- `email` (built-in)

## Usage
```python
from mail import send_email

# Send basic email
send_email(
    sender='from@example.com',
    recipient='to@example.com', 
    subject='Test Email',
    body='Hello World!'
)

# Send HTML email with attachment
send_email(
    sender='from@example.com',
    recipient='to@example.com',
    subject='Test Email',
    body='<h1>Hello World!</h1>',
    is_html=True,
    attachments=['document.pdf']
```