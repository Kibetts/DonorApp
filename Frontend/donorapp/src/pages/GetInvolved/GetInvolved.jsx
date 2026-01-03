import React from 'react';
import VolunteerForm from '../../components/forms/VolunteerForm/VolunteerForm';
import { Link } from 'react-router-dom';
import styles from './GetInvolved.module.css';

const GetInvolved = () => {
  return (
    <div className={styles.getInvolved}>
      <div className="container">
        <h1 className="section-title">Get Involved</h1>
        
        <div className={styles.optionsGrid}>
          <div className={styles.option}>
            <h3>💰 Donate</h3>
            <p>Make a one-time or monthly donation to support our programs.</p>
            <Link to="/donate" className="btn btn-primary">Donate Now</Link>
          </div>

          <div className={styles.option}>
            <h3>🤝 Volunteer</h3>
            <p>Share your time and skills to make a direct impact.</p>
            <a href="#volunteer-form" className="btn btn-secondary">Apply to Volunteer</a>
          </div>

          <div className={styles.option}>
            <h3>🏢 Corporate Partnership</h3>
            <p>Partner with us to create sustainable change.</p>
            <Link to="/contact" className="btn btn-secondary">Contact Us</Link>
          </div>

          <div className={styles.option}>
            <h3>📣 Spread the Word</h3>
            <p>Share our mission on social media and with your network.</p>
            <button className="btn btn-secondary">Share</button>
          </div>
        </div>

        <section id="volunteer-form" className={styles.formSection}>
          <h2>Volunteer Application</h2>
          <VolunteerForm />
        </section>
      </div>
    </div>
  );
};

export default GetInvolved;