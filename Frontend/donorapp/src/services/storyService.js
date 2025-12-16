import api from './api';

export const storyService = {
  getStories: async (featured = false, limit = null) => {
    let url = `/stories/?featured=${featured}`;
    if (limit) url += `&limit=${limit}`;
    const response = await api.get(url);
    return response.data.stories;
  },

  getStory: async (id) => {
    const response = await api.get(`/stories/${id}`);
    return response.data;
  },

  getStoryBySlug: async (slug) => {
    const response = await api.get(`/stories/${slug}`);
    return response.data;
  },
};