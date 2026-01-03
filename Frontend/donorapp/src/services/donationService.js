import api from './api';

export const donationService = {
  createDonation: async (donationData) => {
    const response = await api.post('/donations/', donationData);
    return response.data;
  },

  confirmDonation: async (donationId) => {
    const response = await api.post(`/donations/${donationId}/confirm`);
    return response.data;
  },

  getStats: async () => {
    const response = await api.get('/donations/stats');
    return response.data;
  },

  getRecentDonations: async (limit = 10) => {
    const response = await api.get(`/donations/recent?limit=${limit}`);
    return response.data;
  },
};