import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Hero.module.css';

const Hero = () => {
  return (
    <section className={styles.hero}>
      <div className="container">
        <div className={styles.heroContent}>
          <h1 className={styles.heroTitle}>
            Transform Lives, One Child at a Time
          </h1>
          <p className={styles.heroSubtitle}>
            Your donation provides education, nutrition, and hope to children in need
          </p>
          <div className={styles.heroButtons}>
            <Link to="/donate" className="btn btn-primary">
              Donate Today
            </Link>
            <Link to="/programs" className="btn btn-secondary">
              Learn More
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;