import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Hero from '../../components/home/Hero/Hero';
import ImpactCounter from '../../components/home/ImpactCounter/ImpactCounter';
import FeaturedStory from '../../components/home/FeaturedStory/FeaturedStory';
import DonationBreakdown from '../../components/home/DonationBreakdown/DonationBreakdown';
import ProgramCard from '../../components/programs/ProgramCard/ProgramCard';
import { programService } from '../../services/programService';
import { storyService } from '../../services/storyService';
import styles from './Home.module.css';

const Home = () => {
  const [featuredPrograms, setFeaturedPrograms] = useState([]);
  const [featuredStory, setFeaturedStory] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [programs, stories] = await Promise.all([
          programService.getPrograms(true),
          storyService.getStories(true, 1)
        ]);
        
        setFeaturedPrograms(programs.slice(0, 3));
        setFeaturedStory(stories[0]);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div className={styles.home}>
      <Hero />
      <ImpactCounter />
      
      <section className="section">
        <div className="container">
          <h2 className="section-title">Our Programs</h2>
          <p className={styles.sectionDescription}>
            We run comprehensive programs that address the fundamental needs of children and communities.
          </p>
          <div className={styles.programsGrid}>
            {loading ? (
              <p>Loading programs...</p>
            ) : (
              featuredPrograms.map(program => (
                <ProgramCard key={program.id} program={program} />
              ))
            )}
          </div>
          <div className={styles.ctaCenter}>
            <Link to="/programs" className="btn btn-secondary">
              View All Programs
            </Link>
          </div>
        </div>
      </section>

      {featuredStory && (
        <section className="section" style={{ background: 'var(--bg-secondary)' }}>
          <div className="container">
            <h2 className="section-title">Featured Success Story</h2>
            <FeaturedStory story={featuredStory} />
          </div>
        </section>
      )}

      <DonationBreakdown />

      <section className="section" style={{ background: 'var(--primary-color)', color: 'white' }}>
        <div className="container">
          <div className={styles.ctaSection}>
            <h2>Ready to Make a Difference?</h2>
            <p>Your donation today can transform a child's tomorrow.</p>
            <Link to="/donate" className="btn btn-primary" style={{ marginTop: '1.5rem' }}>
              Donate Now
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;