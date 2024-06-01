<template>
  <div>
    <div class="topbar">
      <img src="../assets/logo.png" alt="Data Guard" class="logo" />
      <div v-if="!isAuthenticated">
        <div class="auth-options">
          <button class="login-button" @click="redirectToLogin">Login</button>
          <button class="signup-button" @click="redirectToSignUp">Sign Up</button>
        </div>
      </div>
    </div>
    <h1>Welcome to Your Dashboard 😊👋</h1>
    <p v-if="!isAuthenticated"> Please use the login or sign up buttons above to access the contents. 🔒</p>
    <CourseList :courses="courses" v-if="courses.length > 0" />
    <ModuleList :modules="modules" v-if="modules.length > 0" />
    <ContentList :contents="contents" v-if="contents.length > 0" />
    <AboutView v-if="showAbout" />
    <div v-if="loading">Loading...</div>
    <div v-if="error">{{ error }}</div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import CourseList from '../components/CourseList.vue';
import ModuleList from '../components/ModuleList.vue';
import ContentList from '../components/ContentList.vue';
import AboutView from '../views/AboutView.vue';
import api from '../api/api';

export default {
  components: {
    CourseList,
    ModuleList,
    ContentList,
    AboutView
  },
  data() {
    return {
      courses: [],
      modules: [],
      contents: [],
      showAbout: true,
      loading: false,
      error: null
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
  created() {
    if (this.isAuthenticated) {
      this.fetchData();
    }
  },
  methods: {
    redirectToLogin() {
      this.$router.push('/login'); // Redirect to login page
    },
    redirectToSignUp() {
      this.$router.push('/signup'); // Redirect to signup page
    },
    async fetchData() {
      try {
        this.loading = true;
        const [coursesResponse, modulesResponse, contentsResponse] = await Promise.all([
          api.getCourses(),
          api.getModules(),
          api.getContents()
        ]);
        this.courses = coursesResponse.data;
        this.modules = modulesResponse.data;
        this.contents = contentsResponse.data;
      } catch (error) {
        console.error('Error fetching data:', error);
        this.error = 'Failed to fetch data. Please try again later.';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
@import '../assets/styles/dashboard.css';
</style>
