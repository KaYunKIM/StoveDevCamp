import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import LoginView from '@/views/Login.vue'
import SignupView from '@/views/Signup.vue'
import AdminLoginView from '@/views/Admin/AdminLogin.vue'
import AdminSignupView from '@/views/Admin/AdminSignup.vue'
import AdminMainView from '@/views/Admin/AdminMain.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/admin/login',
    name: 'Adimin',
    component: AdminLoginView
  },
  {
    path: '/admin/signup',
    name: 'Adimin',
    component: AdminSignupView
  },
  {
    path: '/admin',
    name: 'Adimin',
    component: AdminMainView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
