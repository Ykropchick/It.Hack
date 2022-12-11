<template>
    <h3 class="title" >{{post.name}}</h3>
    <div class="body" >{{post.short_description}}</div>
    <button @click="$emit('detailer', post.id)"  type="button" class="btn btn-primary More position-absolute bottom-0 end-0">Подробнее</button>

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
    },
    style:{
      type: String,
      require: false,
    }
  },

mounted() {
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