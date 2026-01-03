import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import styles from './Header.module.css';

const Header = () => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  return (
    <header className={styles.header}>
      <div className="container">
        <div className={styles.headerContent}>
          <Link to="/" className={styles.logo}>
            <span className={styles.logoIcon}>❤️</span>
            Hope Foundation
          </Link>

          <button 
            className={styles.mobileMenuButton}
            onClick={toggleMobileMenu}
            aria-label="Toggle menu"
          >
            <span className={styles.hamburger}></span>
            <span className={styles.hamburger}></span>
            <span className={styles.hamburger}></span>
          </button>

          <nav className={`${styles.nav} ${mobileMenuOpen ? styles.navOpen : ''}`}>
            <Link to="/" className={styles.navLink} onClick={() => setMobileMenuOpen(false)}>
              Home
            </Link>
            <Link to="/about" className={styles.navLink} onClick={() => setMobileMenuOpen(false)}>
              About
            </Link>
            <Link to="/programs" className={styles.navLink} onClick={() => setMobileMenuOpen(false)}>
              Programs
            </Link>
            <Link to="/stories" className={styles.navLink} onClick={() => setMobileMenuOpen(false)}>
              Stories
            </Link>
            <Link to="/get-involved" className={styles.navLink} onClick={() => setMobileMenuOpen(false)}>
              Get Involved
            </Link>
            <Link to="/contact" className={styles.navLink} onClick={() => setMobileMenuOpen(false)}>
              Contact
            </Link>
            <Link 
              to="/donate" 
              className={styles.donateButton}
              onClick={() => setMobileMenuOpen(false)}
            >
              Donate Now
            </Link>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;