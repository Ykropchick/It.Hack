<template>
  <div class="PostArray" v-for="postArray in slicedArray">
    <div class="post" v-for="post in postArray" :key="post.id">
      <Post :post="post"/>
    </div>
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
    }
  },
  computed:{
    ...mapState({
      UrlApi: state => state.UrlAPI,
      UserApi: state => state.UsersAPI,
      PostApi: state => state.PostAPi,
    }),
    slicedArray(){
      const res = [];
      for(let i = 0; i < this.posts.length; i+= 4){
        res.push(this.posts.slice(i, i+4))
      }
      console.log(res)
      return res
    }
  },
  mounted() {
    this.getPosts()
  }

}
</script>

<style scoped>

.PostArray{
  display: flex;
  padding: 10px 400px;
}
.post{
  display: inline-block;
  border: solid 4px purple;
  margin: 10px 10px;
  width: 300px;
  height: 300px;

}

</style>







'