import React, { useState } from 'react';
import { newsletterService } from '../../../services/newsletterService';
import styles from './NewsletterForm.module.css';

const NewsletterForm = ({ compact = false }) => {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage('');

    try {
      await newsletterService.subscribe(email);
      setSuccess(true);
      setMessage('Thank you for subscribing!');
      setEmail('');
    } catch (error) {
      setMessage(error.message || 'Failed to subscribe');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className={`${styles.form} ${compact ? styles.compact : ''}`} onSubmit={handleSubmit}>
      <div className={styles.inputGroup}>
        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          className={styles.input}
        />
        <button type="submit" disabled={loading} className={styles.button}>
          {loading ? 'Subscribing...' : 'Subscribe'}
        </button>
      </div>
      {message && (
        <p className={success ? styles.success : styles.error}>
          {message}
        </p>
      )}
    </form>
  );
};

export default NewsletterForm;