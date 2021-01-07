<template>
  <div class="swiper">
    <el-carousel :interval="3000" type="card" height="280">
      <el-carousel-item v-for="(item,index) in swiperList" :key="index">
        <img :src="item.img"/>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
  import {swiperList} from "../assets/data/swiper";

  export default {
    name: "Swiper",
    data() {
      return {
        swiperList: [],
      }
    },
    created() {
      this.swiperList = swiperList;
    },
  }
</script>

<style scoped>

</style>
