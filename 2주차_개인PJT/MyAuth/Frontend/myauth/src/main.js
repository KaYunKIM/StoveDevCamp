import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import vuetify from './plugins/vuetify'

import axios from 'axios'
import cookies from 'vue-cookies'

Vue.config.productionTip = false

Vue.prototype.$axios = axios
Vue.use(cookies)
Vue.$cookies.config("7d") //쿠키 만료일은 7일 사용


new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
