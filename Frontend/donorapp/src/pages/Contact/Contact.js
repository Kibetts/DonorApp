import React from 'react';
import ContactForm from '../../components/forms/ContactForm/ContactForm';
import styles from './Contact.module.css';

const Contact = () => {
  return (
    <div className={styles.contact}>
      <div className="container">
        <h1 className="section-title">Contact Us</h1>
        
        <div className={styles.contactGrid}>
          <div className={styles.contactInfo}>
            <h3>Get in Touch</h3>
            <p>We'd love to hear from you. Send us a message and we'll respond as soon as possible.</p>
            
            <div className={styles.infoItem}>
              <h4>📧 Email</h4>
              <p>info@hopefoundation.org</p>
            </div>

            <div className={styles.infoItem}>
              <h4>📞 Phone</h4>
              <p>+1 (555) 123-4567</p>
            </div>

            <div className={styles.infoItem}>
              <h4>📍 Address</h4>
              <p>123 Charity Lane<br />Hope City, HC 12345</p>
            </div>

            <div className={styles.infoItem}>
              <h4>⏰ Office Hours</h4>
              <p>Monday - Friday: 9:00 AM - 5:00 PM</p>
            </div>
          </div>

          <div className={styles.contactFormContainer}>
            <ContactForm />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;