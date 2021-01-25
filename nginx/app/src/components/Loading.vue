<template>
  <div>
    <div class="loading"></div>
    <div>
      <span class="title" >正在分析...</span>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Loading' // 定义的组件名称 使用时写法：loading
  }
</script>

<style scoped>
  .loading {
    position: fixed;
    left: 0;
    top: -10px;
    background: url('~@/assets/img/loading-ball.gif') center center no-repeat #fff;
    width: 100vw;
    height: 100vh;
    z-index: 1000;
  }
  .title {
    position: absolute;
    left: 630px;
    top: 420px;
    z-index: 1001;
    font-size: 20px;
    font-family: "微软雅黑 Light";
    font-weight: bold;
  }
</style>
