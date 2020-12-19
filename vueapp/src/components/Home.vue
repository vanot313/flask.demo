<template>
  <div>
    <Header></Header>
    <Aside></Aside>
    <div class="content-box" :class="{'content-collapse':collapse}">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import Header from "./Header";
  import Aside from "./Aside";
  import bus from "../assets/js/bus";

  export default {
    components: {
      Aside,
      Header
    },
    data(){
      return {
        collapse: false
      }
    },
    created(){
      /*bus进行组件间通信*/
      bus.$on('collapse',msg => {
        this.collapse = msg
      })
    }
  }
</script>

<style>

</style>
