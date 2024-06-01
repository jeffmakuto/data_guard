<template>
    <div id="contents-list" class="container">
      <div v-for="content in contents" :key="content.id" class="content">
        <strong>Title:</strong> {{ content.title }}<br>
        <strong>Module:</strong> {{ content.module.title }}<br>
        <strong>Content Type:</strong> {{ content.content_type }}<br>
        <a :href="content.file" download>Download File</a><br>
        <hr>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      contents: {
        type: Array,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  @import '../assets/styles/content.css';
  </style>
  