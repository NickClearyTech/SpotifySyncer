<template>
<h1>hi</h1>
  <p v-if="success">Success</p>
  <p v-else-if="success==null">Null</p>
  <p v-else>Failure</p>
</template>

<script lang="ts">
import {GetSpotifyTokenFromCode, GetSyncerTokenFromSpotifyToken} from "../utils/auth/tokens";

export default {
  name: "CallBack",
  methods: {
    onLoad: async function() {
      // Validate flow code in the url is the same as we set in the cookie previously
      if (this.$cookies.get("spotify_flow_code") != this.$route.query.state) {
        return;
      }

      // Remove cookie containing the flow code
      if (!this.$cookies.remove("spotify_flow_code")) {
        return;
      }

      if (this.$route.query.code == null) {
        return;
      }

      let code: string = this.$route!.query.code.toString();

      // Convert Spotify Code to Spotify Token
      let processedToken: [boolean, string, string] = await GetSpotifyTokenFromCode(code);
      if (!processedToken[0]){
        this.success = false;
        return;
      }

      this.$cookies.set("spotify_token", processedToken[1], 3599); // Set the cookie to expire one second before the token actually does
      this.$cookies.set("spotify_refresh_token", processedToken[2], (3600 * 24 * 180) - 1);

      // Convert Spotify Token to Syncer Token
      let syncerResult: [boolean, string, string] = await GetSyncerTokenFromSpotifyToken(processedToken[1], "default");
      if (!syncerResult[0]){
        this.success = false;
        return;
      }

      this.$cookies.set("syncer_token", syncerResult[1], 3599);
      this.$cookies.set("syncer_refresh_token", syncerResult[2], (3600 * 24 * 180) - 1); // Expire in 6 months
      this.success = true;
    }
  },
  beforeMount(){
    this.onLoad();
  },
  data() {
    return {
      success: false
    }
  }
}
</script>

<style scoped>

</style>