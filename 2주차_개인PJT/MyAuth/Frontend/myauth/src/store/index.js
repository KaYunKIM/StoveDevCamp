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
    userData: {},
  },
  getters: {
    isAuthenticated: state => {
      !!state.authToken
    },
    config: state => ({
      headers: {
        Authorization: `Token ${state.authToken}`
      }
    }),
  },
  mutations: {
    SET_TOKEN(state, authToken) {
      state.authToken = authToken
      cookies.set('auth-token', authToken)
    },
    SET_USERDATA(state, userData) {
      state.userData = userData
    }  
  },
  actions: {
    authUser({ commit }, authInfo) {
      console.log('authUserok')
      axios.post(SERVER.URL + authInfo.api, authInfo.data)
        .then((res) => {
          console.log(res)
          commit('SET_TOKEN', res.data.key)
          router.push('/')
        })
        .catch(err => console.error(err.response.data))
    },

    signup({dispatch}, userData) {
      const authInfo = {
        api: SERVER.ROUTES.signup,
        data: userData
      }
      dispatch('authUser', authInfo)
    },

    login({dispatch}, userData) {
      const authInfo = {
        api: SERVER.ROUTES.login,
        data: userData
      }
      dispatch('authUser', authInfo)
    },
    
    logout({ getters, commit }) {
      console.log('logoutttt')
      console.log(SERVER.URL + SERVER.ROUTES.logout)
      axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
        .then(() => {
          commit('SET_TOKEN', null)
          commit('userData', {})
          cookies.remove('auth-token')
          router.push('/')
        })
        .catch(err => console.error(err.response.data))
    },

    // fetchUserData({ commit }) {
    //   axios.post()
    // }
  },
  modules: {
  }
})
