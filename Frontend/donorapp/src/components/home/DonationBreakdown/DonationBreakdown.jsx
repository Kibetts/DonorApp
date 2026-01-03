import React from 'react';
import { DONATION_TIERS } from '../../../utils/constants';
import styles from './DonationBreakdown.module.css';

const DonationBreakdown = () => {
  return (
    <section className="section">
      <div className="container">
        <h2 className="section-title">How Your Donation Helps</h2>
        <div className={styles.tiersGrid}>
          {DONATION_TIERS.map((tier, index) => (
            <div key={index} className={styles.tierCard}>
              <div className={styles.amount}>${tier.amount}</div>
              <div className={styles.impact}>{tier.impact}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default DonationBreakdown;
