<template>
  <form class="form">
    <v-text-field
      v-model="old_password"
      :error-messages="old_passwordErrors"
      :counter="8"
      label="Old Password"
      required
      @input="$v.old_password.$touch()"
      @blur="$v.old_password.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="new_password1"
      :error-messages="new_password1Errors"
      :counter="8"
      label="New Password"
      required
      @input="$v.new_password1.$touch()"
      @blur="$v.new_password1.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="new_password2"
      :error-messages="new_password2Errors"
      :counter="8"
      label="New Password Confirm"
      required
      @input="$v.new_password2.$touch()"
      @blur="$v.new_password2.$touch()"
    ></v-text-field>
    <v-row class="mt-3">
      <v-btn 
        class="ml-3" 
        @click="clear"
      >
        clear
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        class="mr-4"
        @click="submit"
      >
        submit
      </v-btn>
    </v-row>
  </form>
</template>


<script>
import { validationMixin } from 'vuelidate'
import { required, minLength } from 'vuelidate/lib/validators'
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  mixins: [validationMixin],

  validations: {
    old_password: { required, minLength: minLength(8) },
    new_password1: { required, minLength: minLength(8) },
    new_password2: { required, minLength: minLength(8) },
  },

  data: () => ({
    old_password: '',
    new_password1: '',
    new_password2: '', 
  }),

  computed: {
    old_passwordErrors () {
      const errors = []
      if (!this.$v.old_password.$dirty) return errors
      !this.$v.old_password.minLength && errors.push('비밀번호는 최소 8자리를 입력하세요')
      !this.$v.old_password.required && errors.push('비밀번호를 입력하세요')
      return errors
    },
    new_password1Errors () {
      const errors = []
      if (!this.$v.new_password1.$dirty) return errors
      !this.$v.new_password1.minLength && errors.push('비밀번호는 최소 8자리를 입력하세요')
      !this.$v.new_password1.required && errors.push('비밀번호를 입력하세요')
      return errors
    },
    new_password2Errors () {
      const errors = []
      if (!this.$v.new_password2.$dirty) return errors
      if (this.new_password1 !== this.new_password2) errors.push('비밀번호가 일치하지 않습니다')
      !this.$v.new_password2.minLength && errors.push('비밀번호는 최소 8자리를 입력하세요')
      !this.$v.new_password2.required && errors.push('비밀번호를 입력하세요')
      return errors
    },
  },

  methods: {
    submit () {
      this.$v.$touch()
      const passwordData = {
          old_password: this.old_password,
          new_password1: this.new_password1,
          new_password2: this.new_password2,
      }
      this.passwordChange(passwordData)
    },
    clear () {
      this.$v.$reset()
      this.old_password = ''
      this.new_password1 = ''
      this.new_password2 = ''
    },
    ...mapActions(['passwordChange'])
  },
}
</script>

<style scoped>
.form {
    margin-top: 200px;
}
</style>