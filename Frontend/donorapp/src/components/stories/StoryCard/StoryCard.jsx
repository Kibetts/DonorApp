import React from 'react';
import { Link } from 'react-router-dom';
import styles from './StoryCard.module.css';

const StoryCard = ({ story }) => {
  return (
    <div className={styles.card}>
      <div className={styles.image}>
        {story.image_url && (
          <img src={story.image_url} alt={story.title} />
        )}
      </div>
      <div className={styles.content}>
        <div className={styles.category}>{story.category}</div>
        <h3 className={styles.title}>{story.title}</h3>
        {story.beneficiary_name && (
          <p className={styles.beneficiary}>
            {story.beneficiary_name}, {story.beneficiary_age}
          </p>
        )}
        <p className={styles.excerpt}>{story.excerpt}</p>
        <Link to={`/stories/${story.slug}`} className="btn btn-secondary">
          Read Story
        </Link>
      </div>
    </div>
  );
};

export default StoryCard;