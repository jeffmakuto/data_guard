<template>
  <div class="container">
    <h1>Sign Up</h1>
    <form @submit.prevent="signup" class="form">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" v-model="email" required class="form-control">
        <div v-if="!isEmailValid && email !== ''" class="error-message">Please enter a valid email address.</div>
      </div>
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" v-model="username" required class="form-control">
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" v-model="password" required class="form-control">
        <div v-if="!isPasswordStrong && password !== ''" class="error-message">Password should be at least 12 characters long.</div>
      </div>
      <button type="submit" class="btn btn-primary">Sign Up</button>
    </form>
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    <div v-if="successMessage" class="success-message">{{ successMessage }}</div>
    <button @click="returnToDashboard" class="btn btn-secondary return-btn">Return to Dashboard</button>
  </div>
</template>

<script>
import api from '../api/api';

export default {
  data() {
    return {
      email: '',
      username: '',
      password: '',
      errorMessage: '',
      successMessage: '',
    };
  },
  computed: {
    isEmailValid() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(this.email);
    },
    isPasswordStrong() {
      return this.password.length >= 12;
    }
  },
  methods: {
    signup() {
      if (!this.isEmailValid || !this.isPasswordStrong) {
        return; // Prevent form submission if email or password is invalid
      }
      api.register({ email: this.email, username: this.username, password: this.password })
        .then(() => {
          this.errorMessage = '';
          this.successMessage = 'Account created successfully. You can now log in.';
          setTimeout(() => {
            this.$router.push('/login');
          }, 3000); // Redirect after 3 seconds
        })
        .catch(error => {
          if (error.response && error.response.status === 400) {
            this.errorMessage = error.response.data.error;
          } else {
            this.errorMessage = 'An unexpected error occurred. Please try again later.';
          }
        });
    },
    returnToDashboard() {
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>
@import '../assets/styles/signup.css';
</style>
