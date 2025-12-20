import React, { useState } from 'react';
import { contactService } from '../../../services/contactService';
import Input from '../../common/Input/Input';
import Button from '../../common/Button/Button';
import styles from './ContactForm.module.css';

const ContactForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    subject: '',
    message: ''
  });
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      await contactService.submitContact(formData);
      setSuccess(true);
      setFormData({ name: '', email: '', phone: '', subject: '', message: '' });
    } catch (err) {
      setError(err.message || 'Failed to send message');
    } finally {
      setLoading(false);
    }
  };

  if (success) {
    return (
      <div className={styles.successMessage}>
        <h3>Message Sent!</h3>
        <p>Thank you for contacting us. We'll respond within 24-48 hours.</p>
        <Button onClick={() => setSuccess(false)}>Send Another Message</Button>
      </div>
    );
  }

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <Input
        label="Name"
        name="name"
        value={formData.name}
        onChange={handleChange}
        required
      />
      <Input
        label="Email"
        type="email"
        name="email"
        value={formData.email}
        onChange={handleChange}
        required
      />
      <Input
        label="Phone (Optional)"
        type="tel"
        name="phone"
        value={formData.phone}
        onChange={handleChange}
      />
      <Input
        label="Subject"
        name="subject"
        value={formData.subject}
        onChange={handleChange}
        required
      />
      <div className="form-group">
        <label className="form-label">Message</label>
        <textarea
          name="message"
          value={formData.message}
          onChange={handleChange}
          required
          className="form-textarea"
          rows="6"
        />
      </div>

      {error && <div className={styles.error}>{error}</div>}

      <Button type="submit" disabled={loading}>
        {loading ? 'Sending...' : 'Send Message'}
      </Button>
    </form>
  );
};

export default ContactForm;
