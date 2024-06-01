<template>
    <div>
      <h1>Contents</h1>
      <ContentList :contents="contents" />
    </div>
  </template>
  
  <script>
  import ContentList from '../components/ContentList.vue';
  import api from '../api/api';
  
  export default {
    components: {
      ContentList,
    },
    data() {
      return {
        contents: [],
      };
    },
    created() {
      api.getContents().then(response => {
        this.contents = response.data;
      }).catch(error => {
        console.error('Error fetching contents:', error);
      });
    },
  };
  </script>
  
  <style scoped>
  @import '../assets/styles/content.css';
  </style>
  