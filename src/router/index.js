import { createRouter, createWebHistory } from 'vue-router'
import PostPage from '@/pages/PostPage';
import MainPage from '@/pages/MainPage';

const routes = [
  {
    path: '/posts',
    component: PostPage
  },
  {
    path: '/',
    component: MainPage,
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
