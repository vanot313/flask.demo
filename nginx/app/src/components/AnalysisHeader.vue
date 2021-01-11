<template>
  <div class="header">
    <!--折叠-->
    <div class="collapse-btn" @click="collapseChange">
      <i class="el-icon-edit"></i>
    </div>
    <div class="logo" align="center">可视化分析</div>
    <div class="header-right">

    </div>
    <div class="header-right">
      <div class="btn-fullscreen" @click="handleFullScreen">
        <el-tooltip :content="fullscreen?`取消全屏`:`全屏`" placement="bottom">
          <i class="el-icon-rank"></i>
        </el-tooltip>
      </div>
    </div>
  </div>
</template>

<script>
  import bus from "../assets/js/bus";
  export default {
    data() {
      return{
        collapse:false,
        fullscreen:false
      }
    },
    computed: {
      userName(){
        return localStorage.getItem('username');
      }
    },
    methods: {
      //侧边栏折叠
      collapseChange(){
        this.collapse = !this.collapse;
        /*第一个参数为标志变量，第二个参数为通信的值*/
        bus.$emit('collapse',this.collapse);
      },
      //全屏
      handleFullScreen(){
        if(this.fullscreen){
          if(document.exitFullscreen)
            document.exitFullscreen();
          else if(document.webkitCancelFullSreeen)
            document.webkitCancelFullSreeen();
        }else{
          let element = document.documentElement;
          if(element.requestFullscreen)
            element.requestFullscreen();
          else if(element.webkitRequestFullScreen)
            element.webkitRequestFullScreen();
        }
        this.fullscreen = !this.fullscreen;
      },
      handleCommand(command){
        if(command == 'logout'){
          localStorage.removeItem('username');
          this.$router.push("/");
        }
      }
    }
  }
</script>

<style scoped>
  .header {
    position: absolute;
    top: 0;
    left: 0;
    background-color: #253041;
    width: 100%;
    height: 100px;
    font-size: 22px;
    color: #fff;
  }

  .collapse-btn {
    position: absolute;
    left: 580px;
    top: 16px;
    padding: 0 21px;
    cursor: pointer;
    line-height: 70px;
    font-size: 30px;
  }

  /*float属性很重要！！*/
  .header .logo{
    position: absolute;
    left: 640px;
    top: 16px;
    line-height: 70px;
    font-size: 30px;
  }

  .header-right {
    float: right;
    position: absolute;
    top: 0px;
    right: 10px;
    padding-right: 20px;
    display: flex;
    height: 70px;
    align-items: center;
  }

  .btn-fullscreen {
    transform: rotate(45deg);
    margin-right: 5px;
    font-size: 24px;
  }

  .user-avator {
    margin-left: 20px;
  }

  .user-avator img {
    display: block;
    width: 40px;
    height: 40px;
    border-radius: 50%;
  }

  .user-name {
    margin:10px;
  }

  .el-dropdown-link{
    color: #fff;
    cursor: pointer;
  }
</style>
