<template>
  <div class="container">
    <h3>{{post.title}}</h3>
    <div>{{post.body}}</div>

  </div>
</template>

<script>
import axios from "axios";
import {mapState} from "vuex";

export default {
  name: "Post",
  props:{
    post:{
      type:Object,
      required: true,
    }
  }


}
</script>

<style scoped>

</style>