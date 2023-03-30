<template>
<h1>hi</h1>
  <p v-if="success">Success</p>
  <p v-else-if="success==null">Null</p>
  <p v-else>Failure</p>
</template>

<script lang="ts">
import { getCallback, codeToToken, spotifyTokenToSyncerToken } from "../service/BackendService";

export default {
  name: "CallBack",
  methods: {
    onLoad: async function() {
     this.$cookies.get()

      let code: string = this.$route.query.code;
      if (code == null) {
        return;
      }
      // Convert Spotify Code to Spotiy Token
      let result = await codeToToken(code);
      if (result.length != 2 || result[1].access_token == null || result[1].access_token instanceof String){
        this.success = false;
      }
      console.log(result);
      // Convert Spotify Token to Syncer Token
      let syncerResult = await spotifyTokenToSyncerToken(result[1].access_token, "default");
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