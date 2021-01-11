<template>
  <div class="sidebar">
    <!--router，使得el-menu-item的index可以作为索引，
    再通过索引去router中查找-->
    <el-menu
      class="sidebar-e1-menu"
      :default-active="onRoutes"
      :collapse="collapse"
      background-color="#334256"
      text-color="#fff"
      active-text-color="#20a0ff"
      router
    >
      <template v-for="item in items">
        <template>
          <el-menu-item :index="item.index" :key="item.index">
            <i :class="item.icon"></i>
            <div style="font-size: 16px;display: inline-block"> {{item.title}}</div>
          </el-menu-item>
        </template>
      </template>
    </el-menu>
  </div>
</template>

<script>

  export default {
    data(){
      return{
        collapse: false,
        items: [
          {
            icon: 'el-icon-document',
            index: 'analysis',
            title: '企业基本信息'
          },
          {
            icon: 'el-icon-document',
            index: 'main',
              title: '企业融资数据'
          },
          {
            icon: 'el-icon-document',
            index: 'main',
            title: '企业年报数据'
          },
        ]
      }
    },
    computed: {
      //登陆后使得首页处于active状态
      onRoutes(){
        //获取当前路由地址
        return this.$route.path.replace('/','');
      }
    },
    methods: {
      handleSelect(index){
        this.activeIndex = index;
      }
    },
  }
</script>

<style scoped>
  .sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 100px;
    bottom: 0;
    background-color: #334256;
    overflow-y: scroll;
    height: 700px;
  }

  .sidebar::-webkit-scrollbar{
    width: 0;
  }

  /*collapse为false时生效*/
  .sidebar-e1-menu:not(.el-menu--collapse) {
    width: 185px;
  }

  .sidebar >ul {
    height: 100%;
  }

</style>
