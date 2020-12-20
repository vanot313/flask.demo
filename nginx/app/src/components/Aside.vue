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
            {{item.title}}
          </el-menu-item>
        </template>
      </template>
    </el-menu>
  </div>
</template>

<script>
  import bus from "../assets/js/bus";
  export default {
    data(){
      return{
        collapse: false,
        items: [
          {
            icon: 'el-icon-document',
            index: 'main',
            title: '系统首页'
          },
          {
            icon: 'el-icon-document',
            index: 'consumer',
            title: '用户管理'
          },
          {
            icon: 'el-icon-document',
            index: 'singer',
            title: '歌手管理'
          },
          {
            icon: 'el-icon-document',
            index: 'songList',
            title: '歌单管理'
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
    created() {
      //通过bus组件间通信进行折叠
      bus.$on('collapse',msg => {
        this.collapse = msg
      })
    }
  }
</script>

<style scoped>
  .sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 0;
    background-color: #334256;
    overflow-y: scroll;
  }

  .sidebar::-webkit-scrollbar{
    width: 0;
  }

  /*collapse为false时生效*/
  .sidebar-e1-menu:not(.el-menu--collapse) {
    width: 150px;
  }

  .sidebar >ul {
    height: 100%;
  }
</style>
