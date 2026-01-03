import React, { useState } from 'react';
import { contactService } from '../../../services/contactService';
import Input from '../../common/Input/Input';
import Button from '../../common/Button/Button';
import styles from './VolunteerForm.module.css';

const VolunteerForm = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    city: '',
    country: '',
    interests: '',
    skills: '',
    why_volunteer: ''
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
      await contactService.applyVolunteer({
        first_name: formData.firstName,
        last_name: formData.lastName,
        email: formData.email,
        phone: formData.phone,
        city: formData.city,
        country: formData.country,
        interests: formData.interests,
        skills: formData.skills,
        why_volunteer: formData.why_volunteer
      });
      setSuccess(true);
    } catch (err) {
      setError(err.message || 'Failed to submit application');
    } finally {
      setLoading(false);
    }
  };

  if (success) {
    return (
      <div className={styles.successMessage}>
        <h3>Application Submitted!</h3>
        <p>Thank you for your interest in volunteering. We'll review your application and contact you within 5-7 business days.</p>
      </div>
    );
  }

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <div className={styles.formRow}>
        <Input
          label="First Name"
          name="firstName"
          value={formData.firstName}
          onChange={handleChange}
          required
        />
        <Input
          label="Last Name"
          name="lastName"
          value={formData.lastName}
          onChange={handleChange}
          required
        />
      </div>

      <Input
        label="Email"
        type="email"
        name="email"
        value={formData.email}
        onChange={handleChange}
        required
      />

      <Input
        label="Phone"
        type="tel"
        name="phone"
        value={formData.phone}
        onChange={handleChange}
      />

      <div className={styles.formRow}>
        <Input
          label="City"
          name="city"
          value={formData.city}
          onChange={handleChange}
        />
        <Input
          label="Country"
          name="country"
          value={formData.country}
          onChange={handleChange}
        />
      </div>

      <div className="form-group">
        <label className="form-label">Areas of Interest</label>
        <textarea
          name="interests"
          value={formData.interests}
          onChange={handleChange}
          className="form-textarea"
          placeholder="e.g., Education, Healthcare, Fundraising..."
          rows="3"
        />
      </div>

      <div className="form-group">
        <label className="form-label">Skills & Experience</label>
        <textarea
          name="skills"
          value={formData.skills}
          onChange={handleChange}
          className="form-textarea"
          placeholder="Tell us about your relevant skills and experience..."
          rows="3"
        />
      </div>

      <div className="form-group">
        <label className="form-label">Why do you want to volunteer? *</label>
        <textarea
          name="why_volunteer"
          value={formData.why_volunteer}
          onChange={handleChange}
          required
          className="form-textarea"
          rows="4"
        />
      </div>

      {error && <div className={styles.error}>{error}</div>}

      <Button type="submit" disabled={loading}>
        {loading ? 'Submitting...' : 'Submit Application'}
      </Button>
    </form>
  );
};

export default VolunteerForm;
