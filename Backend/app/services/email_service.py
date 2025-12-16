from flask import current_app, render_template_string
from flask_mail import Message
from app.extensions import mail

class EmailService:
    
    @staticmethod
    def send_email(to, subject, html_body, text_body=None):
        """Send an email"""
        try:
            msg = Message(
                subject=subject,
                recipients=[to] if isinstance(to, str) else to,
                html=html_body,
                body=text_body or html_body
            )
            mail.send(msg)
            return True
        except Exception as e:
            current_app.logger.error(f"Failed to send email: {str(e)}")
            return False
    
    @staticmethod
    def send_donation_receipt(donor, donation):
        """Send donation receipt email"""
        subject = f"Thank you for your ${donation.amount} donation!"
        
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h2 style="color: #2c5282;">Thank You for Your Generous Donation!</h2>
                    <p>Dear {donor.first_name} {donor.last_name},</p>
                    <p>We are incredibly grateful for your donation of <strong>${donation.amount}</strong>.</p>
                    <p>Your support makes a real difference in the lives of the children we serve.</p>
                    
                    <div style="background-color: #f7fafc; padding: 15px; border-radius: 5px; margin: 20px 0;">
                        <h3 style="margin-top: 0;">Donation Details:</h3>
                        <p><strong>Amount:</strong> ${donation.amount} {donation.currency}</p>
                        <p><strong>Date:</strong> {donation.created_at.strftime('%B %d, %Y')}</p>
                        <p><strong>Transaction ID:</strong> {donation.transaction_id or 'Pending'}</p>
                        <p><strong>Type:</strong> {donation.donation_type.replace('_', ' ').title()}</p>
                    </div>
                    
                    <p>This email serves as your receipt for tax purposes. Our Tax ID is: XX-XXXXXXX</p>
                    <p>If you have any questions, please don't hesitate to contact us.</p>
                    
                    <p>With gratitude,<br>
                    <strong>The Foundation Team</strong></p>
                </div>
            </body>
        </html>
        """
        
        return EmailService.send_email(donor.email, subject, html_body)
    
    @staticmethod
    def send_newsletter_confirmation(subscriber):
        """Send newsletter subscription confirmation"""
        subject = "Welcome to Our Newsletter!"
        
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h2 style="color: #2c5282;">Welcome to Our Community!</h2>
                    <p>Hi {subscriber.first_name or 'there'},</p>
                    <p>Thank you for subscribing to our newsletter! You'll now receive updates about our programs, impact stories, and ways you can help.</p>
                    <p>We're excited to keep you informed about the difference we're making together.</p>
                    <p>Best regards,<br>
                    <strong>The Foundation Team</strong></p>
                </div>
            </body>
        </html>
        """
        
        return EmailService.send_email(subscriber.email, subject, html_body)
    
    @staticmethod
    def send_volunteer_confirmation(volunteer):
        """Send volunteer application confirmation"""
        subject = "Thank You for Your Volunteer Application"
        
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h2 style="color: #2c5282;">Thank You for Applying!</h2>
                    <p>Dear {volunteer.first_name},</p>
                    <p>We have received your volunteer application and are reviewing it carefully.</p>
                    <p>Our team will contact you within 5-7 business days to discuss next steps.</p>
                    <p>Thank you for your interest in making a difference!</p>
                    <p>Best regards,<br>
                    <strong>The Foundation Team</strong></p>
                </div>
            </body>
        </html>
        """
        
        return EmailService.send_email(volunteer.email, subject, html_body)
    
    @staticmethod
    def send_contact_confirmation(submission):
        """Send contact form submission confirmation"""
        subject = "We've Received Your Message"
        
        html_body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h2 style="color: #2c5282;">Thank You for Contacting Us</h2>
                    <p>Dear {submission.name},</p>
                    <p>We have received your message and will respond as soon as possible, typically within 24-48 hours.</p>
                    <p><strong>Your message:</strong></p>
                    <div style="background-color: #f7fafc; padding: 15px; border-radius: 5px; margin: 20px 0;">
                        <p>{submission.message}</p>
                    </div>
                    <p>Best regards,<br>
                    <strong>The Foundation Team</strong></p>
                </div>
            </body>
        </html>
        """
        
        return EmailService.send_email(submission.email, subject, html_body)