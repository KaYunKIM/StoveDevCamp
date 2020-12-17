<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />
      </div>
      <v-spacer></v-spacer>
      <router-link class="link" to="/signup">SIGNUP<v-icon>mdi-register</v-icon></router-link>
      <router-link class="link" to="/login">LOGIN<v-icon>mdi-login</v-icon></router-link>
      <router-link class="link" to="/" @click.native="logout">LOGOUT<v-icon>mdi-logout</v-icon></router-link>
    </v-app-bar>
    
    <router-view/>

    <!-- <v-main>
      <HelloWorld/>
    </v-main> -->
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';
import { mapActions } from 'vuex'

export default {
  name: 'App',

  components: {
    // HelloWorld,
  },

  methods: {
    ...mapActions(['logout'])
  },

  data: () => ({
    //
  }),
};
</script>

<style>
#app {
  margin: 100px;
}
.link {
  color: beige !important;
  font-weight:bold;
  /* font-family: "Roboto", sans-serif !important; */
  margin-right: 10px;
  
}
a {
  text-decoration: none;
}
</style>