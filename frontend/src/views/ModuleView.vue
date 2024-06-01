<template>
    <div>
      <h1>Modules</h1>
      <ModuleList :modules="modules" />
    </div>
  </template>
  
  <script>
  import ModuleList from '../components/ModuleList.vue';
  import api from '../api/api';
  
  export default {
    components: {
      ModuleList,
    },
    data() {
      return {
        modules: [],
      };
    },
    created() {
      api.getModules().then(response => {
        this.modules = response.data;
      }).catch(error => {
        console.error('Error fetching modules:', error);
      });
    },
  };
  </script>
  
  <style scoped>
  @import '../assets/styles/module.css';
  </style>
  