export const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';
export const STRIPE_KEY = process.env.REACT_APP_STRIPE_PUBLISHABLE_KEY;

export const DONATION_TIERS = [
  { amount: 25, impact: 'Feeds a child for a week' },
  { amount: 50, impact: 'Provides school supplies for one child' },
  { amount: 100, impact: 'Covers healthcare for a month' },
  { amount: 250, impact: 'Sponsors a child\'s education for a term' },
  { amount: 500, impact: 'Supports a full program for a month' },
  { amount: 1000, impact: 'Transforms an entire community' }
];

export const DONATION_FREQUENCIES = [
  { value: 'one-time', label: 'One-Time' },
  { value: 'monthly', label: 'Monthly' },
  { value: 'quarterly', label: 'Quarterly' },
  { value: 'yearly', label: 'Yearly' }
];

export const PROGRAM_CATEGORIES = {
  education: 'Education',
  nutrition: 'Nutrition',
  healthcare: 'Healthcare',
  shelter: 'Shelter',
  other: 'Other'
};

export const ROUTES = {
  HOME: '/',
  ABOUT: '/about',
  DONATE: '/donate',
  PROGRAMS: '/programs',
  STORIES: '/stories',
  GET_INVOLVED: '/get-involved',
  CONTACT: '/contact'
};