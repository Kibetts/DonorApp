import React from 'react';
import { Link } from 'react-router-dom';
import styles from './FeaturedStory.module.css';

const FeaturedStory = ({ story }) => {
  return (
    <div className={styles.featuredStory}>
      <div className={styles.storyImage}>
        {story.image_url && (
          <img src={story.image_url} alt={story.title} />
        )}
      </div>
      <div className={styles.storyContent}>
        <h3>{story.title}</h3>
        <p className={styles.beneficiary}>{story.beneficiary_name}, {story.beneficiary_age}</p>
        <p>{story.excerpt}</p>
        <Link to={`/stories/${story.slug}`} className="btn btn-secondary">
          Read Full Story
        </Link>
      </div>
    </div>
  );
};

export default FeaturedStory;