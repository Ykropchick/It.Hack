<template>
    <h3 class="title">{{post.title}}</h3>
    <div class="body">{{post.body}}</div>

  <button type="button" class="btn btn-primary More position-absolute bottom-0 end-0">Подробнее</button>
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
.title{
  color: white;
}
.body{
  color: white;
}
.More{

  width: 150px;
  height: 42px;
  font-style: normal;
  font-weight: 800;
  font-size: 20px;
  line-height: 39px;

  color: white;
  background: purple;

  margin-right: 10px;
  margin-bottom: 10px;
}


</style>