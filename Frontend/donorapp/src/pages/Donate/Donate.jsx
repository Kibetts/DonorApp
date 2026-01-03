import React from 'react';
import DonationForm from '../../components/donation/DonationForm/DonationForm';
import DonationTiers from '../../components/donation/DonationTiers/DonationTiers';
import styles from './Donate.module.css';

const Donate = () => {
  return (
    <div className={styles.donate}>
      <div className="container">
        <h1 className="section-title">Make a Difference Today</h1>
        <p className={styles.subtitle}>
          Your generosity transforms lives. Choose your impact below.
        </p>
        <DonationTiers />
        <DonationForm />
      </div>
    </div>
  );
};

export default Donate;