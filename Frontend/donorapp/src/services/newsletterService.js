import api from './api';

export const newsletterService = {
  subscribe: async (email, firstName = '', lastName = '') => {
    const response = await api.post('/newsletter/subscribe', {
      email,
      first_name: firstName,
      last_name: lastName,
    });
    return response.data;
  },

  unsubscribe: async (email) => {
    const response = await api.post('/newsletter/unsubscribe', { email });
    return response.data;
  },
};