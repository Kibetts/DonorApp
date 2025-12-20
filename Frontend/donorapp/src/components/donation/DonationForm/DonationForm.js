import React, { useState } from 'react';
import { donationService } from '../../../services/donationService';
import Input from '../../common/Input/Input';
import Button from '../../common/Button/Button';
import styles from './DonationForm.module.css';

const DonationForm = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    amount: '',
    donationType: 'one-time',
    frequency: 'monthly'
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const result = await donationService.createDonation({
        first_name: formData.firstName,
        last_name: formData.lastName,
        email: formData.email,
        phone: formData.phone,
        amount: parseFloat(formData.amount),
        donation_type: formData.donationType,
        frequency: formData.donationType === 'recurring' ? formData.frequency : null
      });

      setSuccess(true);
      // Here you would redirect to payment processing
      console.log('Donation created:', result);
    } catch (err) {
      setError(err.message || 'Failed to process donation');
    } finally {
      setLoading(false);
    }
  };

  if (success) {
    return (
      <div className={styles.successMessage}>
        <h3>Thank You!</h3>
        <p>Your donation is being processed. You will receive a confirmation email shortly.</p>
      </div>
    );
  }

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <h3>Your Information</h3>
      
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
        label="Phone (Optional)"
        type="tel"
        name="phone"
        value={formData.phone}
        onChange={handleChange}
      />

      <Input
        label="Donation Amount ($)"
        type="number"
        name="amount"
        value={formData.amount}
        onChange={handleChange}
        min="1"
        required
      />

      <div className={styles.donationType}>
        <label>
          <input
            type="radio"
            name="donationType"
            value="one-time"
            checked={formData.donationType === 'one-time'}
            onChange={handleChange}
          />
          One-Time Donation
        </label>
        <label>
          <input
            type="radio"
            name="donationType"
            value="recurring"
            checked={formData.donationType === 'recurring'}
            onChange={handleChange}
          />
          Recurring Donation
        </label>
      </div>

      {formData.donationType === 'recurring' && (
        <div className={styles.frequency}>
          <label>Frequency:</label>
          <select name="frequency" value={formData.frequency} onChange={handleChange}>
            <option value="monthly">Monthly</option>
            <option value="quarterly">Quarterly</option>
            <option value="yearly">Yearly</option>
          </select>
        </div>
      )}

      {error && <div className={styles.error}>{error}</div>}

      <Button type="submit" disabled={loading}>
        {loading ? 'Processing...' : 'Complete Donation'}
      </Button>

      <p className={styles.secureNote}>
        🔒 Your donation is secure and tax-deductible
      </p>
    </form>
  );
};

export default DonationForm;