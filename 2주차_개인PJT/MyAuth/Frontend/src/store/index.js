import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router'
import axios from 'axios'
import cookies from 'vue-cookies'
import SERVER from '@/API/url'
import vuexPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: cookies.get('auth-token'),
    userData: {},
    userList: [],
  },
  getters: {
    isAuthenticated(state) {
      return !!state.authToken
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
    },
    SET_USERLIST(state, userList) {
      state.userList = userList
    }  
  },
  actions: {
    authUser({ state, commit, dispatch }, authInfo) {
      return new Promise((resolve) => {
        axios.post(SERVER.URL + authInfo.api, authInfo.data)
          .then((res) => {
            commit('SET_TOKEN', res.data.key)
            dispatch('fetchUserData')
              .then(() => {
                if (state.userData.is_superuser) {
                  router.push('/admin')
                } else {
                  router.push('/')
                }
              })
              .catch(err => console.error(err.response.data))
            resolve(res)
          })
          .catch((err) => {
            console.error(err.response.data)
            alert('입력한 정보를 다시 확인해주세요.')
          })
      })
    },

    signup({dispatch}, userData) {
      const authInfo = {
        api: SERVER.ROUTES.signup,
        data: userData
      }
      dispatch('authUser', authInfo)
    },

    login({ dispatch }, userData) {
      const authInfo = {
        api: SERVER.ROUTES.login,
        data: userData
      }
      dispatch('authUser', authInfo)
    },
    
    logout({ getters, commit }) {
      axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
        .then(() => {
          commit('SET_USERDATA', {})
          commit('SET_TOKEN', null)
          cookies.remove('auth-token')
        })
        .catch(err => console.error(err.response.data))
    },

    fetchUserData({ getters, commit }) {
      return new Promise((resolve) => {
        axios.get(SERVER.URL + SERVER.ROUTES.profile, getters.config)
          .then((res) => {
            commit('SET_USERDATA', res.data)
            resolve(res.data.is_superuser)
          })
          .catch(err => console.error(err.response.data))
      })
    },

    fetchUserList({ getters, commit }) {
      return new Promise(() => {
        axios.get(SERVER.URL + SERVER.ROUTES.userList, getters.config)
          .then(res => commit('SET_USERLIST', res.data))
          .catch(err => console.error(err.response.data))
      })
    },

    passwordChange({ getters }, passwordData) {
      axios.post(SERVER.URL + SERVER.ROUTES.passwordChange, passwordData, getters.config)
        .then(() => {
          alert('비밀번호가 정상적으로 변경됐습니다.')
          router.push('/profile')
        })
        .catch(err => console.error(err.response.data))
    }
  },
  modules: {
  },
  plugins: [
    vuexPersistedState()
  ]
})
