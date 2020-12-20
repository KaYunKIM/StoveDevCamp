import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'

import LoginView from '@/views/accounts/Login.vue'
import SignupView from '@/views/accounts/Signup.vue'

import ProfileView from '@/views/accounts/Profile.vue'
import PasswordChangeView from '@/views/accounts/PasswordChange.vue'

import AdminLoginView from '@/views/admin/AdminLogin.vue'
import AdminSignupView from '@/views/admin/AdminSignup.vue'
import AdminMainView from '@/views/admin/AdminMain.vue'

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
    path: '/profile',
    name: 'Profile',
    component: ProfileView
  },
  {
    path: '/profile/password-change',
    name: 'PasswordChange',
    component: PasswordChangeView
  },
  {
    path: '/admin/login',
    name: 'AdminLogin',
    component: AdminLoginView
  },
  {
    path: '/admin/signup',
    name: 'AdminSignup',
    component: AdminSignupView
  },
  {
    path: '/admin',
    name: 'Admin',
    component: AdminMainView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
