<script lang="ts">
import {generateState} from "../utils/randomGenerator";

export default {
  methods:{
    loginToSpotify: function(){
      let state: string = generateState();
      this.$store.commit("setFlowCode", state);
      console.log(this.$store.state.spotifyFlowCode);
      let url: string = `https://accounts.spotify.com/authorize?response_type=code&redirect_uri=http://localhost:4436/callback&client_id=a98b190ae81745a68f3b2be525f6b0e7&state=${state}`;
      // window.location.replace(url);
    }
  }
};
</script>

<template>
  <button @click="loginToSpotify">
    Login With Spotify
  </button>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
