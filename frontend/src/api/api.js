import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Set up request interceptor to add JWT token to outgoing requests
apiClient.interceptors.request.use(
  config => {
    // Retrieve token from local storage
    const token = localStorage.getItem('token');
    // If token exists, add it to the Authorization header
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
});

// Function to set authentication token
export function setAuthToken(token) {
  apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

// API methods for login, register, and fetching data
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
