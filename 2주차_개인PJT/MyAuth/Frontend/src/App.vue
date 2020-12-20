<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <router-link v-if="userData.is_superuser" to="/admin">
          <v-img
            alt="MyAuth Logo"
            class="shrink mr-2"
            contain
            src="@/assets/logo.png"
            transition="scale-transition"
            width="40"
          />
        </router-link>
        <router-link v-else to="/">
          <v-img
            alt="MyAuth Logo"
            class="shrink mr-2"
            contain
            src="@/assets/logo.png"
            transition="scale-transition"
            width="40"
          />
        </router-link>
      </div>
      <v-spacer></v-spacer>
      <router-link v-if="!isAuthenticated" class="link" to="/signup">SIGNUP<v-icon class="ml-1">person_add</v-icon></router-link>
      <router-link v-if="!isAuthenticated" class="link" to="/login">LOGIN<v-icon>mdi-login</v-icon></router-link>
      <router-link v-if="isAuthenticated" class="link" to="/profile"><span class="mr-2 cursor" >Welcome {{this.userData.username}}!</span></router-link>
      <router-link v-if="isAuthenticated" class="link" to="/" @click.native="logout">LOGOUT<v-icon>mdi-logout</v-icon></router-link>
    
    </v-app-bar>
    
    <router-view/>
  </v-app>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex'

export default {
  name: 'App',
  data: () => ({
    //
  }),
  computed: {
    ...mapState(['userData']),
    ...mapGetters(['isAuthenticated'])
  },
  methods: {
    ...mapActions(['logout'])
  },
};
</script>

<style>
#app {
  margin-left: 25%;
  width: 50%;
}
.link {
  color: beige !important;
  font-weight:bold;
  text-decoration: none;
  /* font-family: "Roboto", sans-serif !important; */
  margin-right: 10px;  
}

.cursor { 
  cursor: pointer; 
}

</style>