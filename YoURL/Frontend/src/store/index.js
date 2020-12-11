import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import SERVER from '@/API/api'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    newUrl: []
  },
  mutations: {
    SET_NEW_URL(state, newUrl) {
      state.newUrl = newUrl
    }
  },
  actions: {
    convertUrl({ commit }, urlInfo) {
      return new Promise((resolve, reject) => {
        const urlData = {
          'link' : urlInfo
        }
        axios.post(SERVER.URL + SERVER.ROUTES.convert, urlData)
          .then(res => {
            commit('SET_NEW_URL', res.data['new_link'])
            resolve(res.data['new_link'])
          })
          .catch((err) => {
            console.error(err.response.data)
            reject(err)
          })
      })
    }
  },
  modules: {
  },
  plugins: [
    createPersistedState()
  ]
})
