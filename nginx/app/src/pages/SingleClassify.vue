<template>
  <div>
    <Header/>
    <Aside/>
    <div style="margin-top: 100px;margin-left: 300px">
      单个企业分类
      <br>
      {{text}}
    </div>
  </div>
</template>

<script>
    import Aside from "../components/Aside";
    import Header from "../components/Header";

    export default {
        name: "SingleClassify",
        components: {
          Aside,
          Header,
        },
        data(){
          return{
            id: '0',
            res: [],
            text: '',
          }
        },
        created() {
          this.res = this.$route.query.res;
          console.log(this.res);
          if(this.res == 'true') this.text='是僵尸企业';
          else this.text = '非僵尸企业';
        }
    }
</script>

<style scoped>

</style>
