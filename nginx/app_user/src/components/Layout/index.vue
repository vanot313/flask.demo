<template>
  <div>
    <!-- Loader -->
    <div id="preloader"><div id="status"><div class="spinner" /></div></div>

    <div class="header-bg">
      <!-- Navigation Bar-->
      <header id="topnav">
        <div class="topbar-main">
          <div class="container-fluid">
            <!-- Logo container-->
            <!-- Text Logo -->
            <router-link tag="a" class="logo" to="/index">
              数据资产估值平台
            </router-link>
            <!-- End Logo container-->

            <div class="menu-extras topbar-custom">
              <ul class="list-inline float-right mb-0">
                <!-- User-->
                <li class="list-inline-item dropdown notification-list">
                  <a
                    class="nav-link dropdown-toggle arrow-none waves-effect nav-user"
                    data-toggle="dropdown"
                    href="#"
                    role="button"
                    aria-haspopup="false"
                    aria-expanded="false"
                  >
                    <img src="@/assets/avatar/default.jpg" alt="user" class="rounded-circle">
                  </a>
                  <div class="dropdown-menu dropdown-menu-right profile-dropdown ">
                    <router-link class="dropdown-item" to="/profile"><i class="dripicons-user text-muted" /> 个人中心</router-link>
                    <div class="dropdown-divider" />
                    <router-link class="dropdown-item" to="" @click.native="logout"><i class="dripicons-exit text-muted" /> 注销</router-link>
                  </div>
                </li>
                <li class="menu-item list-inline-item">
                  <!-- Mobile menu toggle-->
                  <a class="navbar-toggle nav-link">
                    <div class="lines">
                      <span />
                      <span />
                      <span />
                    </div>
                  </a>
                  <!-- End mobile menu toggle-->
                </li>
              </ul>
            </div>
            <!-- end menu-extras -->

            <div class="clearfix" />
          </div>
          <!-- end container -->
        </div>
        <!-- end topbar-main -->

        <!-- MENU Start -->
        <div class="navbar-custom">
          <div class="container-fluid">
            <div id="navigation">
              <!-- Navigation Menu-->
              <ul class="navigation-menu">
                <li class="has-submenu">
                  <router-link to="/dashboard"><i class="dripicons-device-desktop" />主页 </router-link>
                </li>

                <li class="has-submenu">
                  <router-link to="/order/list"><i class="dripicons-to-do" />资产评估 <i class="mdi mdi-chevron-down mdi-drop" /></router-link>
                  <ul class="submenu megamenu">
                    <li>
                      <ul>
                        <li><router-link to="/order/new">新的评估 </router-link> </li>
                        <li><router-link to="/order/list">评估历史 </router-link> </li>
                      </ul>
                    </li>
                  </ul>
                </li>

                <li class="has-submenu">
                  <router-link to="/expert/apply"><i class="dripicons-user" />专家资格申请 </router-link>
                </li>
              </ul>
              <!-- End navigation menu -->
            </div>
            <!-- end #navigation -->
          </div>
          <!-- end container -->
        </div>
        <!-- end navbar-custom -->
      </header>
      <!-- End Navigation Bar-->

      <div class="container-fluid">
        <!-- Page-Title -->
        <div class="row">
          <div class="col-sm-12">
            <div class="page-title-box">
              <form class="float-right app-search">
                <input type="text" placeholder="搜索" class="form-control">
                <button type="submit"><i class="fa fa-search" /></button>
              </form>
              <h4 class="page-title">{{ title }}</h4>
            </div>
          </div>
        </div>
        <!-- end page title end breadcrumb -->
      </div>
    </div>
  </div>
</template>

<script>
import { loadJs } from '@/utils/loadJS'

export default {
  props: {
    title: {
      type: String,
      default: undefined
    }
  },
  mounted() {
    loadJs('../assets/js/app.js')
  },
  methods: {
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/index`)
    }
  }
}
</script>
