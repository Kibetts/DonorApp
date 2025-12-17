import React from 'react';
import { Link } from 'react-router-dom';
import NewsletterForm from '../../forms/NewsletterForm/NewsletterForm';
import styles from './Footer.module.css';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className={styles.footer}>
      <div className="container">
        <div className={styles.footerContent}>
          <div className={styles.footerSection}>
            <h3 className={styles.footerTitle}>About Hope Foundation</h3>
            <p className={styles.footerText}>
              Transforming lives through education, nutrition, and healthcare. 
              Together, we're building a brighter future for children in need.
            </p>
            <div className={styles.socialLinks}>
              <a href="#" className={styles.socialLink} aria-label="Facebook">
                <span>📘</span>
              </a>
              <a href="#" className={styles.socialLink} aria-label="Twitter">
                <span>🐦</span>
              </a>
              <a href="#" className={styles.socialLink} aria-label="Instagram">
                <span>📷</span>
              </a>
              <a href="#" className={styles.socialLink} aria-label="LinkedIn">
                <span>💼</span>
              </a>
            </div>
          </div>

          <div className={styles.footerSection}>
            <h3 className={styles.footerTitle}>Quick Links</h3>
            <ul className={styles.footerLinks}>
              <li><Link to="/">Home</Link></li>
              <li><Link to="/about">About Us</Link></li>
              <li><Link to="/programs">Programs</Link></li>
              <li><Link to="/stories">Impact Stories</Link></li>
              <li><Link to="/get-involved">Get Involved</Link></li>
              <li><Link to="/contact">Contact</Link></li>
            </ul>
          </div>

          <div className={styles.footerSection}>
            <h3 className={styles.footerTitle}>Contact Info</h3>
            <ul className={styles.footerLinks}>
              <li>📧 info@hopefoundation.org</li>
              <li>📞 +1 (555) 123-4567</li>
              <li>📍 123 Charity Lane<br />Hope City, HC 12345</li>
            </ul>
          </div>

          <div className={styles.footerSection}>
            <h3 className={styles.footerTitle}>Stay Connected</h3>
            <p className={styles.footerText}>
              Subscribe to receive updates about our impact and ways you can help.
            </p>
            <NewsletterForm compact />
          </div>
        </div>

        <div className={styles.footerBottom}>
          <p>&copy; {currentYear} Hope Foundation. All rights reserved.</p>
          <p>Tax ID: XX-XXXXXXX | 501(c)(3) Non-Profit Organization</p>
          <div className={styles.footerBottomLinks}>
            <a href="#">Privacy Policy</a>
            <span>•</span>
            <a href="#">Terms of Service</a>
            <span>•</span>
            <a href="#">Cookie Policy</a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;