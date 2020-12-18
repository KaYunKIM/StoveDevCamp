<template>
  <v-container class="home">
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          src="@/assets/logo.png"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to MyAuth
        </h1>
      </v-col>

      <v-col
        class="mb-5"
        cols="12"
      >
        <h2 class="headline font-weight-bold mb-3">
          Are you a staff?
        </h2>

        <v-row justify="center">
          <router-link class="subheading mx-3" to="/admin/signup">Need to signup?</router-link>
          <router-link class="subheading mx-3" to="/admin/login">Have an account?</router-link>
        </v-row>
      </v-col>
    </v-row>
    <router-view/>
  </v-container>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
  name: 'Home',
  data: () => ({
  }),
  computed: {
    ...mapState(['userData']),
    ...mapGetters(['isAuthenticated'])
  },
  created() {
    console.log(this.userData)
  }
}
</script>

<style>
.home {
  margin-top: 80px;
}
</style>