<template>
    <div>
      <h1>Courses</h1>
      <CourseList :courses="courses" />
    </div>
  </template>
  
  <script>
  import CourseList from '../components/CourseList.vue';
  import api from '../api/api';
  
  export default {
    components: {
      CourseList,
    },
    data() {
      return {
        courses: [],
      };
    },
    created() {
      api.getCourses().then(response => {
        this.courses = response.data;
      }).catch(error => {
        console.error('Error fetching courses:', error);
      });
    },
  };
  </script>
  
  <style scoped>
  @import '../assets/styles/course.css';
  </style>
  