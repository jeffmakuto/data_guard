<template>
    <div id="courses-list" class="container">
      <div v-for="course in courses" :key="course.id" class="course">
        <strong>Course Title:</strong> {{ course.title }}<br>
        <strong>Description:</strong> {{ course.description || 'N/A' }}<br>
        <hr>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      courses: {
        type: Array,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  @import '../assets/styles/course.css';
  </style>
  