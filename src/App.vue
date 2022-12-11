<template>
  <my-navbar/>
  <div class="app">
    <router-view></router-view>
  </div>
</template>

<script>
import axios from 'axios';
import {mapState, mapGetters, mapActions, mapMutations} from 'vuex'
export default {
  components: {},
  data() {
  },
  methods: {
  },
  computed:{
  }


}
</script>

<style>
*{
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  background: #000000;;
}
.app{
}


</style>
