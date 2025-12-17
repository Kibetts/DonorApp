import React, { useEffect, useState } from 'react';
import ProgramCard from '../../components/programs/ProgramCard/ProgramCard';
import { programService } from '../../services/programService';
import styles from './Programs.module.css';

const Programs = () => {
  const [programs, setPrograms] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPrograms = async () => {
      try {
        const data = await programService.getPrograms();
        setPrograms(data);
      } catch (error) {
        console.error('Error fetching programs:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchPrograms();
  }, []);

  return (
    <div className={styles.programs}>
      <div className="container">
        <h1 className="section-title">Our Programs</h1>
        <p className={styles.description}>
          We run comprehensive programs that address the fundamental needs of children and communities,
          creating lasting change through education, nutrition, healthcare, and infrastructure development.
        </p>
        
        {loading ? (
          <p style={{textAlign: 'center'}}>Loading programs...</p>
        ) : (
          <div className={styles.programsGrid}>
            {programs.map(program => (
              <ProgramCard key={program.id} program={program} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Programs;