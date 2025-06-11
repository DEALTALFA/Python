
import win32com.client

def send_outlook_email():
    # Create Outlook application object
    outlook = win32com.client.Dispatch('Outlook.Application')
    
    # Create a new mail item
    mail = outlook.CreateItem(0)
    
    # Configure email parameters
    mail.Subject = 'Test Email'
    mail.To = 'Deepakyadav_20391053.mca@geu.ac.in'
    mail.Body = 'This is a test email sent from Python using Outlook'
    
    # Optional: Add attachments
    #mail.Attachments.Add('path/to/file.txt')
    
    # Send the email
    mail.Send()

if __name__ == '__main__':
    try:
        send_outlook_email()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")