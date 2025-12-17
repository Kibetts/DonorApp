import React from 'react';
import styles from './Loader.module.css';

const Loader = ({ size = 'medium' }) => {
  return (
    <div className={`${styles.loader} ${styles[size]}`}>
      <div className={styles.spinner}></div>
    </div>
  );
};

export default Loader;
