import React from 'react';
import styles from './About.module.css';

const About = () => {
  return (
    <div className={styles.about}>
      <div className="container">
        <h1 className="section-title">About Hope Foundation</h1>
        <div className={styles.content}>
          <section className={styles.section}>
            <h2>Our Mission</h2>
            <p>
              To empower children and communities through sustainable programs that provide 
              access to education, proper nutrition, healthcare, and opportunities for growth.
            </p>
          </section>

          <section className={styles.section}>
            <h2>Our Story</h2>
            <p>
              Founded in 2010, Hope Foundation has been dedicated to transforming the lives of 
              underprivileged children through comprehensive programs in education, nutrition, 
              healthcare, and community development.
            </p>
          </section>

          <section className={styles.section}>
            <h2>Financial Transparency</h2>
            <div className={styles.transparency}>
              <div className={styles.stat}>
                <div className={styles.statBar} style={{width: '85%'}}></div>
                <div className={styles.statLabel}>Programs & Services: 85%</div>
              </div>
              <div className={styles.stat}>
                <div className={styles.statBar} style={{width: '10%'}}></div>
                <div className={styles.statLabel}>Fundraising: 10%</div>
              </div>
              <div className={styles.stat}>
                <div className={styles.statBar} style={{width: '5%'}}></div>
                <div className={styles.statLabel}>Administration: 5%</div>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
};

export default About;