import { createRouter, createWebHistory } from 'vue-router'
import PostPage from '@/pages/PostPage';
import MainPage from '@/pages/MainPage';
import EnterPage from "@/pages/EnterPage";

const routes = [
  {
    path: '/posts',
    component: PostPage
  },
  {
    path: '/',
    component: MainPage,
  },
  {
    path: '/login',
    component: EnterPage
  },


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
