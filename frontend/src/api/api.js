import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_URL || 'http://localhost:8080/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export function setAuthToken(token) {
  apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

export default {
  login(credentials) {
    return apiClient.post('/users/login/', credentials);
  },
  register(user) {
    return apiClient.post('/users/register/', user);
  },
  getCourses() {
    return apiClient.get('/courses/');
  },
  getModules() {
    return apiClient.get('/modules/');
  },
  getContents() {
    return apiClient.get('/contents/');
  },
};
