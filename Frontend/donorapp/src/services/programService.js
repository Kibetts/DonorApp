import api from './api';

export const programService = {
  getPrograms: async (featured = false) => {
    const response = await api.get(`/programs/?featured=${featured}`);
    return response.data.programs;
  },

  getProgram: async (id) => {
    const response = await api.get(`/programs/${id}`);
    return response.data;
  },

  getProgramBySlug: async (slug) => {
    const response = await api.get(`/programs/${slug}`);
    return response.data;
  },
};