<template>
<h1>hi</h1>
  <p v-if="success">Success</p>
  <p v-else-if="success==null">Null</p>
  <p v-else>Failure</p>
</template>

<script lang="ts">
import { getCallback,codeToToken } from "../service/BaseService";
export default {
  name: "CallBack",
  methods: {
    onLoad: async function() {
      let code: string = this.$route.query.code;
      let result = await codeToToken(code);
      if (result.length == 2){
        this.success = true;
      } else {
        this.success = false;
      }
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