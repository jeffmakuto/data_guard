<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 10px 0;
  background-color: #f8f9fa; /* Add a background color */
  border-bottom: 1px solid #ddd; /* Add a bottom border */
}

.nav-links {
  display: flex;
  justify-content: center;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin: 0 15px; /* Add spacing between links */
  text-decoration: none; /* Remove default underline */
  transition: color 0.3s; /* Add a smooth color transition */
}

nav a:hover {
  color: #42b983;
}

router-link-active,
router-link-exact-active {
  color: #42b983;
}
</style>
