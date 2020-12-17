import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router'
import axios from 'axios'
import cookies from 'vue-cookies'
import SERVER from '@/API/django_rest_framework'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: cookies.get('auth-token'),
  },
  getters: {
    
  },
  mutations: {
    SET_TOKEN(state, authToken) {
      state.authToken = authToken
      cookies.set('auth-token', authToken)
    } 
  },
  actions: {
    

    login({}) {

    },
    
    logout() {

    },

    signup() {

    },
  },
  modules: {
  }
})
