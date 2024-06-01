<template>
    <div id="modules-list" class="container">
      <div v-for="module in modules" :key="module.id" class="module">
        <strong>Module Title:</strong> {{ module.title }}<br>
        <strong>Course:</strong> {{ module.course.title }}<br>
        <strong>Course Description:</strong> {{ module.course.description || 'N/A' }}<br>
        <strong>Module Description:</strong> {{ module.description || 'N/A' }}<br>
        <hr>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      modules: {
        type: Array,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  @import '../assets/styles/module.css';
  </style>
  