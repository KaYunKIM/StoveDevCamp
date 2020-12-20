<template>
  <v-simple-table class="form">
    <template v-slot:default>
      <thead>
        <h1>Admin Page</h1>
        <tr>
          <th class="text-left">
            Username
          </th>
          <th class="text-left">
            Email
          </th>
          <th class="text-left">
            Date Joined
          </th>
          <th class="text-left">
            Superuser
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in users"
          :key="item.username"
        >
          <td>{{ item.username }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.date_joined }}</td>
          <td>{{ item.is_superuser }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'AdminMain',
  data () {
    return {
      users: [],
    }
  },
  computed: {
    ...mapState(['userList']),
  },
  methods: {
    ...mapActions(['fetchUserList'])
  },
  created() {
    this.fetchUserList()
    this.users = this.userList
  }
}
</script>

<style scoped>
.form {
    margin-top: 100px;
}
</style>