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
          Your Profile Page
        </h1>
      </v-col>

      <v-col
        class="mb-5"
        cols="12"
      >
        <v-row justify="center">
          <router-link class="subheading mx-3" to="/admin/signup">Forgor your password?</router-link>
          <router-link class="subheading mx-3" to="/profile/password-change">Change your password?</router-link>
        </v-row>
      </v-col>
    </v-row>
    <router-view/>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Profile',
  data () {
    return {
      userInfo: '',
    }
  },
  computed: {
    ...mapState(['userData']),
  },
  methods: {
    ...mapActions([])
  },
  created() {
    this.userInfo = this.userData
  }
}
</script>

<style scoped>
.form {
    margin-top: 100px;
}
</style>