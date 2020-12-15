<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          src="@/assets/YoURL_logo.jpg"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to YoURL
        </h1>
      </v-col>
      
      <v-col
        class="mb-5"
        cols="12"
      >
        <h2 class="headline font-weight-bold mb-3">
          Create your own URL!
        </h2>

        <v-row justify="center">
          <v-col
            class="mb-5"
            cols="12"
            sm="5"
          >
          <v-text-field
            v-model="urlInfo"
            label="Input URL HERE"
            clearable
            v-on:keyup.enter="showNewUrl()"
          ></v-text-field>

          <div v-if="urlInfo && newUrlInfo">
            <v-text-field
            id='myUrl'
            v-model="newUrlInfo"
            filled
            rounded
          ></v-text-field>
            <!-- <a v-bind:href="newUrlInfo">{{ newUrlInfo }}</a> -->
          </div>
          <div v-if="urlStatus == true && newUrlInfo == ''">
            <v-btn
              depressed
              color="primary"
              @click="showNewUrl()"
            >
              CREATE
            </v-btn>
          </div>
          <div v-if="newUrlInfo">
            <v-btn
              depressed
              color="primary"
              @click="copyUrl('myUrl')"    
            >
              COPY
            </v-btn>
          </div>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'UrlShortener',

  data () {
    return {
      urlInfo : '',
      newUrlInfo: '',
      urlStatus: false,
    }    
  },

  computed: {
    ...mapState([
      'newUrl'
    ])
  },

  methods: {
    ...mapActions([
      'convertUrl'
    ]),
    showNewUrl() {
      this.convertUrl(this.urlInfo)
        .then(() => {
          this.newUrlInfo = this.newUrl
        })
    },
    copyUrl() {
      const copyURL = document.getElementById("myUrl")
      copyURL.select()
      document.execCommand('copy')
      alert(copyURL.value + ' 링크를 복사했습니다.')
    }
  },

  watch: {
    urlInfo() {
      this.urlStatus = !this.urlStatus
      // 새로운 주소 넣었을 때 단축주소가 안 보이게 하기
      if (this.urlInfo === null) {   
        this.newUrlInfo = ''
      }
    }
  },

  created() {
    console.log('created_urlInfo', this.urlInfo)
  }
}
</script>
