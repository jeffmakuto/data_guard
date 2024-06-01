<template>
  <div class="container">
    <h1>Sign Up</h1>
    <form @submit.prevent="signup" class="form">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" v-model="email" required class="form-control">
        <div v-if="!isEmailValid" class="error-message">Please enter a valid email address.</div>
      </div>
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" v-model="username" required class="form-control">
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" v-model="password" required class="form-control">
      </div>
      <button type="submit" class="btn btn-primary">Sign Up</button>
    </form>
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
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
    };
  },
  computed: {
    isEmailValid() {
      // Basic email validation using regex
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(this.email);
    }
  },
  methods: {
    signup() {
      if (!this.isEmailValid) {
        return; // Prevent form submission if email is invalid
      }
      api.register({ email: this.email, username: this.username, password: this.password })
        .then(() => {
          this.$router.push('/login');
        })
        .catch(() => {
          this.errorMessage = 'Username or email already exists';
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
