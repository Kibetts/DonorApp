import React, { useEffect, useState } from 'react';
import { donationService } from "@/services/donationService";
import styles from './ImpactCounter.module.css';

const ImpactCounter = () => {
  const [stats, setStats] = useState({
    total_raised: 0,
    total_donors: 0,
    children_helped: 0,
    programs_active: 0
  });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const data = await donationService.getStats();
        setStats(data);
      } catch (error) {
        console.error('Error fetching stats:', error);
      }
    };

    fetchStats();
  }, []);

  return (
    <section className={styles.impactCounter}>
      <div className="container">
        <div className={styles.statsGrid}>
          <div className={styles.stat}>
            <div className={styles.statNumber}>
              ${Math.floor(stats.total_raised).toLocaleString()}
            </div>
            <div className={styles.statLabel}>Total Raised</div>
          </div>
          <div className={styles.stat}>
            <div className={styles.statNumber}>
              {stats.total_donors.toLocaleString()}
            </div>
            <div className={styles.statLabel}>Generous Donors</div>
          </div>
          <div className={styles.stat}>
            <div className={styles.statNumber}>
              {stats.children_helped.toLocaleString()}
            </div>
            <div className={styles.statLabel}>Children Helped</div>
          </div>
          <div className={styles.stat}>
            <div className={styles.statNumber}>
              {stats.programs_active}
            </div>
            <div className={styles.statLabel}>Active Programs</div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ImpactCounter;
