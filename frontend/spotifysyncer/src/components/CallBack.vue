<template>
<h1>hi</h1>
  <p v-if="success">Success</p>
  <p v-else-if="success==null">Null</p>
  <p v-else>Failure</p>
</template>

<script lang="ts">
import { getCallback, codeToToken, spotifyTokenToSyncerToken } from "../service/BackendService";
import {GetSpotifyTokenFromCode} from "../utils/auth/tokens";

export default {
  name: "CallBack",
  methods: {
    onLoad: async function() {
      console.log(this.$store.state.spotifyFlowCode)
      let code: string = this.$route.query.code;
      if (code == null) {
        return;
      }

      // Convert Spotify Code to Spotify Token
      let proccessedToken: [boolean, string, string] = await GetSpotifyTokenFromCode(code);
      if (!proccessedToken[0]){
        this.success = false;
        console.log("Sad")
        return;
      }

      this.$cookies.set("spotify_token", proccessedToken[1], 3599); // Set the cookie to expire one second before the token actually does
      this.$cookies.set("spotify_refresh_token", proccessedToken[2], (3600 * 24 * 180) - 1);

      // Convert Spotify Token to Syncer Token
      let syncerResult: [boolean, string, string] = await spotifyTokenToSyncerToken(proccessedToken[1], "default");
      if (!syncerResult[0]){
        this.success = false;
        return;
      }

      this.$cookies.set("syncer_token", syncerResult[1], 3599);
      this.$cookies.set("syncer_refresh_token", syncerResult[2], (3600 * 24 * 180) - 1); // Expire in 6 months
      console.log(syncerResult);
    }
  },
  beforeMount(){
    this.onLoad();
  },
  data() {
    return {
      success: null
    }
  }
}
</script>

<style scoped>

</style>