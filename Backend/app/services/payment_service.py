import stripe
from flask import current_app
from app.models.donation import Donation
from app.models.donor import Donor
from app.extensions import db

class PaymentService:
    
    @staticmethod
    def initialize_stripe():
        """Initialize Stripe with the secret key"""
        stripe.api_key = current_app.config['STRIPE_SECRET_KEY']
    
    @staticmethod
    def create_stripe_customer(donor):
        """Create or retrieve Stripe customer"""
        PaymentService.initialize_stripe()
        
        if donor.stripe_customer_id:
            return donor.stripe_customer_id
        
        try:
            customer = stripe.Customer.create(
                email=donor.email,
                name=f"{donor.first_name} {donor.last_name}",
                metadata={'donor_id': donor.id}
            )
            
            donor.stripe_customer_id = customer.id
            db.session.commit()
            
            return customer.id
        except stripe.error.StripeError as e:
            raise Exception(f"Stripe error: {str(e)}")
    
    @staticmethod
    def create_payment_intent(amount, currency, donor, donation_type='one-time'):
        """Create a Stripe payment intent"""
        PaymentService.initialize_stripe()
        
        customer_id = PaymentService.create_stripe_customer(donor)
        
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Convert to cents
                currency=currency.lower(),
                customer=customer_id,
                metadata={
                    'donor_id': donor.id,
                    'donation_type': donation_type
                }
            )
            
            return intent
        except stripe.error.StripeError as e:
            raise Exception(f"Stripe error: {str(e)}")
    
    @staticmethod
    def create_subscription(donor, amount, currency, frequency='monthly'):
        """Create a Stripe subscription for recurring donations"""
        PaymentService.initialize_stripe()
        
        customer_id = PaymentService.create_stripe_customer(donor)
        
        try:
            # Create a price
            price = stripe.Price.create(
                unit_amount=int(amount * 100),
                currency=currency.lower(),
                recurring={'interval': frequency.replace('ly', '')},
                product_data={'name': f'Monthly Donation - {amount} {currency}'}
            )
            
            # Create subscription
            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[{'price': price.id}],
                metadata={
                    'donor_id': donor.id,
                    'donation_type': 'recurring'
                }
            )
            
            return subscription
        except stripe.error.StripeError as e:
            raise Exception(f"Stripe error: {str(e)}")
    
    @staticmethod
    def confirm_payment(payment_intent_id):
        """Confirm a payment was successful"""
        PaymentService.initialize_stripe()
        
        try:
            intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            return intent.status == 'succeeded'
        except stripe.error.StripeError as e:
            raise Exception(f"Stripe error: {str(e)}")
    
    @staticmethod
    def refund_payment(payment_intent_id):
        """Refund a payment"""
        PaymentService.initialize_stripe()
        
        try:
            refund = stripe.Refund.create(payment_intent=payment_intent_id)
            return refund
        except stripe.error.StripeError as e:
            raise Exception(f"Stripe error: {str(e)}")