import { createRouter, createWebHistory } from 'vue-router';
import DashboardView from '../views/DashboardView.vue';
import ContentView from '../views/ContentView.vue';
import CourseView from '../views/CourseView.vue';
import LoginView from '../views/LoginView.vue';
import ModuleView from '../views/ModuleView.vue';
import SignupView from '../views/SignupView.vue';
import AboutView from '../views/AboutView.vue';

const routes = [
  { path: '/', component: DashboardView },
  { path: '/content', component: ContentView },
  { path: '/course', component: CourseView },
  { path: '/login', component: LoginView },
  { path: '/module', component: ModuleView },
  { path: '/signup', component: SignupView },
  { path: '/about', component: AboutView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
