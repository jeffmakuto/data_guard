<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <label for="username">Username:</label>
      <input 
        type="text" 
        id="username"
        v-model="username" 
        required 
        @input="clearErrorMessage"
        :class="{ 'invalid': errorMessage }"
      >
      <label for="password">Password:</label>
      <input 
        type="password" 
        id="password"
        v-model="password" 
        required 
        @input="clearErrorMessage"
        :class="{ 'invalid': errorMessage }"
      >
      <button type="submit">Login</button>
    </form>
    <div v-if="errorMessage" id="error-message" class="error-message">{{ errorMessage }}</div>
    <button @click="returnToDashboard">Return to Dashboard</button>
  </div>
</template>

<script>
import api, { setAuthToken } from '../api/api';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    login() {
      // Make login API call
      api.login({ username: this.username, password: this.password })
        .then(response => {
          // If login is successful, store token in local storage
          const token = response.data.access;
          localStorage.setItem('token', token);
          
          // Set token in Axios headers
          setAuthToken(token);

          // Redirect user to dashboard or another page
          this.$router.push('/');
        })
        .catch(error => {
          // If login fails, display error message
          this.errorMessage = 'Invalid username or password';
        });
    },
    returnToDashboard() {
      this.$router.push('/');
    },
    clearErrorMessage() {
      this.errorMessage = '';
    }
  },
};
</script>

<style scoped>
@import '../assets/styles/login.css';
</style>
