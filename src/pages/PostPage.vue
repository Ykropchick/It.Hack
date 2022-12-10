<template>
  <div v-for="post in posts" :key="post.id">
    <Post :post="post"/>
  </div>
</template>

<script>
import axios from "axios";
import {mapState, mapGetters, mapActions, mapMutations} from 'vuex'
import Post from "@/components/Post";

export default {
  components: {Post},
  data(){
    return{
      posts: {},
    }
  },
  methods:{
    async getPosts () {
      const response = await axios.get(this.PostApi);
      this.posts = response.data.posts;
      console.log(this.posts)
    }
  },
  computed:{
    ...mapState({
      UrlApi: state => state.UrlAPI,
      UserApi: state => state.UsersAPI,
      PostApi: state => state.PostAPi,
    })
  },
  mounted() {
    this.getPosts()
  }
}
</script>

<style scoped>

.row{
  display: inline-block;
}

</style>







'