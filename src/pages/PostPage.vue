<template>


  <div class="row PostArray" v-for="postArray in slicedArray">
    <div class="col post position-relative"  v-for="post in postArray" :key="post.id">
      <Post @detailer="showMoreInfo" :post="post"/>
    </div>
  </div>
  <my-dialog :show="showDialog">
    <div class="content">
      <div class="row Name">
        {{dialogContent.name}}
      </div>
      <div class="row Date">
        {{dialogContent.date}}
      </div>
      <div class="row Desc">
        {{dialogContent.description}}
      </div>
    </div>
  </my-dialog>


</template>

<script>
import axios from "axios";
import {mapState, mapGetters, mapActions, mapMutations} from 'vuex'
import Post from "@/components/Post";
import MyDialog from "@/components/UI/MyDialog";
import myDialog from "@/components/UI/MyDialog";

export default {
  components: {Post, MyDialog},
  data(){
    return{
      showDialog: false,
      dialogContent:{

        name:'',
        description:'',
        date:'',
      },
      posts: [],

    }
  },
  methods:{
    async getPosts () {
      const response = await axios.get("http://127.0.0.1:8001/api/Projects/",);
      this.posts = response.data;
    },
    showMoreInfo(id){
      const showPost = this.posts.filter(p => p.id === id);
      this.showDialog = true;
      this.dialogContent = {
        name: showPost.name,
        description: showPost.description,
        date: showPost.date,
      }
    },

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
  padding: 10px 400px;
}
.post{
  border: solid 4px purple;
  margin: 10px 10px;
  width: 400px;
  height: 400px;


}

</style>







'