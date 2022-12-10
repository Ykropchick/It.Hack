<template>
  <div class="container">
    <h3 class="title">{{post.title}}</h3>
    <div class="body">{{post.body}}</div>

    <button class="More">Подробнее</button>
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
.container{
  text-align: center;
  word-wrap: break-word;
  position: relative;
}
.title{
  color: white;
}
.body{
  overflow: hidden;
  clear: both;
  color: white;
}
.More{
  float: right;

  position: absolute;
  top: 245px;
  right: 10px;

  width: 150px;
  height: 42px;
  font-style: normal;
  font-weight: 800;
  font-size: 20px;
  line-height: 39px;

  color: white;
  background: #7B45EC;

}
</style>