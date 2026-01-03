import React, { useState } from 'react';
import { DONATION_TIERS } from '../../../utils/constants';
import styles from './DonationTiers.module.css';

const DonationTiers = ({ onSelectTier }) => {
  const [selectedTier, setSelectedTier] = useState(null);

  const handleSelectTier = (amount) => {
    setSelectedTier(amount);
    if (onSelectTier) {
      onSelectTier(amount);
    }
  };

  return (
    <div className={styles.tiers}>
      <h3 className={styles.title}>Choose Your Impact</h3>
      <div className={styles.tiersGrid}>
        {DONATION_TIERS.map((tier) => (
          <div
            key={tier.amount}
            className={`${styles.tier} ${selectedTier === tier.amount ? styles.selected : ''}`}
            onClick={() => handleSelectTier(tier.amount)}
          >
            <div className={styles.amount}>${tier.amount}</div>
            <div className={styles.impact}>{tier.impact}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default DonationTiers;