def main():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # Email configuration
    sender_email = "your_email@outlook.com"  
    sender_password = "your_password"
    recipient_email = "recipient@example.com"
    subject = "Test Email"
    body = "This is a test email sent from Python"

    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email 
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to Outlook SMTP server
    try:
        server = smtplib.SMTP("smtp-mail.outlook.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send email
        server.send_message(message)
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Error sending email: {e}")
        
    finally:
        server.quit()


if __name__ == "__main__":
    main()
