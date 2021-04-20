<template>
  <!-- STRAT NAVBAR -->
  <nav id="navbar" class="navbar navbar-expand-lg fixed-top navbar-custom sticky sticky-dark">
    <div class="container">
      <!-- LOGO -->
      <a class="navbar-brand logo text-uppercase" href="/">
        <i class="mdi mdi-android-auto" /> 数据资产估值平台
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarCollapse"
        aria-controls="navbarCollapse"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <i class="mdi mdi-menu" />
      </button>
      <div id="navbarCollapse" class="collapse navbar-collapse">
        <div class="nav-button ml-auto">
          <ul v-if="id !== ''" class="nav navbar-nav navbar-right">
            <el-dropdown>
              <img class="avatar" src="@/assets/avatar/default.jpg">
              <el-dropdown-menu slot="dropdown">
                <router-link to="/dashboard">
                  <el-dropdown-item>主页</el-dropdown-item>
                </router-link>
                <el-dropdown-item divided @click.native="logout">
                  <span style="display:block;">退出</span>
                </el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </ul>
          <ul v-else class="nav navbar-nav navbar-right">
            <li class="li">
              <router-link to="/login">
                <button type="button" class="btn btn-default navbar-btn btn-rounded b1">登录</button>
              </router-link>
            </li>
            <li class="li">
              <router-link to="/register">
                <button type="button" class="btn btn-default navbar-btn btn-rounded b2">注册</button>
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
  <!-- END NAVBAR -->
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters([
      'id'
    ])
  },
  mounted: () => {
    window.onscroll = function() {
      onwindowScroll()
    }
    var navbar = document.getElementById('navbar')
    function onwindowScroll() {
      if (
        document.body.scrollTop > 40 ||
        document.documentElement.scrollTop > 40
      ) {
        navbar.style.backgroundColor = '#272a33'
        navbar.style.padding = '10px'
      } else {
        navbar.style.backgroundColor = ''
        navbar.style.padding = '20px'
      }
    }
  },
  methods: {
    async logout() {
      await this.$store.dispatch('user/logout')
    }
  }
}
</script>

<style scoped>
.btn.btn-default.navbar-btn.btn-rounded {
  color:#FFFFFF;
}

.btn.btn-default.navbar-btn.btn-rounded.b2 {
  border-color: #FFFFFF;
}

.li {
  padding-left: 20px;
}

.nav.navbar-nav.navbar-right {
  float: right;
}

.avatar {
  height: 46px;
  width: 46px;
  border-radius: 50%;
}
</style>
