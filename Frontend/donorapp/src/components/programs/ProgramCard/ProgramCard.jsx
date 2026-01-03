import React from 'react';
import { Link } from 'react-router-dom';
import styles from './ProgramCard.module.css';

const ProgramCard = ({ program }) => {
  const progress = program.goal_amount ? 
    (program.raised_amount / program.goal_amount) * 100 : 0;

  return (
    <div className={styles.card}>
      <div className={styles.image}>
        {program.image_url && (
          <img src={program.image_url} alt={program.title} />
        )}
      </div>
      <div className={styles.content}>
        <div className={styles.category}>{program.category}</div>
        <h3 className={styles.title}>{program.title}</h3>
        <p className={styles.description}>{program.short_description || program.description}</p>
        
        {program.goal_amount && (
          <>
            <div className={styles.progressBar}>
              <div className={styles.progressFill} style={{ width: `${Math.min(progress, 100)}%` }}></div>
            </div>
            <div className={styles.stats}>
              <span>${program.raised_amount.toLocaleString()} raised</span>
              <span>of ${program.goal_amount.toLocaleString()}</span>
            </div>
          </>
        )}
        
        <div className={styles.footer}>
          <span className={styles.beneficiaries}>
            {program.beneficiaries_count} children helped
          </span>
          <Link to={`/donate?program=${program.id}`} className="btn btn-primary">
            Support Program
          </Link>
        </div>
      </div>
    </div>
  );
};

export default ProgramCard;