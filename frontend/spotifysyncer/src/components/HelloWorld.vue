<script lang="ts">
import {generateState} from "../utils/randomGenerator";

export default {
  methods:{
    loginToSpotify: function() {
      // Get a randomly generated string to use as the state code
      let state: string = generateState();
      // Set cookies to be sure no MoTM attack
      this.$cookies.set("spotify_flow_code", state);
      let url: string = `https://accounts.spotify.com/authorize?response_type=code&redirect_uri=${import.meta.env.VITE_SPOTIFY_REDIRECT_URI}&client_id=${import.meta.env.VITE_SPOTIFY_CLIENT_ID}&state=${state}`;
      // Redirect to spotify auth page
      window.location.replace(url);
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
