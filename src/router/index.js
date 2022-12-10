import { createRouter, createWebHistory } from 'vue-router'
import PostPage from '@/pages/PostPage';

const routes = [
  {
    path: '/posts',
    component: PostPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
