<template>
  <div>
    单个企业分类
    {{id}}
  </div>
</template>

<script>
    export default {
        name: "SingleClassify",
        data(){
          return{
            id: '2',
          }
        },
        created() {
          this.id = this.$route.query.id;
        }
    }
</script>

<style scoped>

</style>
