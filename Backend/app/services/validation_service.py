import re
from email_validator import validate_email, EmailNotValidError

class ValidationService:
    
    @staticmethod
    def validate_email_address(email):
        """Validate email address format"""
        try:
            valid = validate_email(email)
            return True, valid.email
        except EmailNotValidError as e:
            return False, str(e)
    
    @staticmethod
    def validate_phone(phone):
        """Validate phone number format"""
        if not phone:
            return True, phone
        
        # Remove all non-digit characters
        digits = re.sub(r'\D', '', phone)
        
        # Check if it's a valid length (10-15 digits)
        if 10 <= len(digits) <= 15:
            return True, phone
        
        return False, "Invalid phone number"
    
    @staticmethod
    def validate_amount(amount):
        """Validate donation amount"""
        try:
            amount_float = float(amount)
            if amount_float < 1:
                return False, "Amount must be at least $1"
            if amount_float > 1000000:
                return False, "Amount cannot exceed $1,000,000"
            return True, amount_float
        except (ValueError, TypeError):
            return False, "Invalid amount"
    
    @staticmethod
    def validate_required_fields(data, required_fields):
        """Validate that required fields are present and not empty"""
        missing_fields = []
        
        for field in required_fields:
            if field not in data or not data[field] or str(data[field]).strip() == '':
                missing_fields.append(field)
        
        if missing_fields:
            return False, f"Missing required fields: {', '.join(missing_fields)}"
        
        return True, None
    
    @staticmethod
    def sanitize_string(text, max_length=None):
        """Sanitize string input"""
        if not text:
            return ''
        
        # Remove leading/trailing whitespace
        text = str(text).strip()
        
        # Truncate if max_length specified
        if max_length and len(text) > max_length:
            text = text[:max_length]
        
        return text