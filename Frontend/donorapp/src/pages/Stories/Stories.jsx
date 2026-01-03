import React, { useEffect, useState } from 'react';
import StoryCard from '../../components/stories/StoryCard/StoryCard';
import { storyService } from '../../services/storyService';
import styles from './Stories.module.css';

const Stories = () => {
  const [stories, setStories] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStories = async () => {
      try {
        const data = await storyService.getStories();
        setStories(data);
      } catch (error) {
        console.error('Error fetching stories:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchStories();
  }, []);

  return (
    <div className={styles.stories}>
      <div className="container">
        <h1 className="section-title">Impact Stories</h1>
        <p className={styles.description}>
          Every donation creates a ripple effect of positive change. Read the inspiring stories
          of children and families whose lives have been transformed through your generosity.
        </p>
        
        {loading ? (
          <p style={{textAlign: 'center'}}>Loading stories...</p>
        ) : (
          <div className={styles.storiesGrid}>
            {stories.map(story => (
              <StoryCard key={story.id} story={story} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Stories;