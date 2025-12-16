import api from './api';

export const contactService = {
  submitContact: async (contactData) => {
    const response = await api.post('/contact/submit', contactData);
    return response.data;
  },

  applyVolunteer: async (volunteerData) => {
    const response = await api.post('/volunteers/apply', volunteerData);
    return response.data;
  },
};