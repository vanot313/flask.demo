<template>
  <div class="hiric">
    <div class="bg-account-pages py-4 py-sm-0">
      <div class="account-home-btn d-none d-sm-block">
        <a href="/" class="text-white">
          <i class="mdi mdi-home h1" />
        </a>
      </div>

      <section class="height-100vh">
        <div class="display-table">
          <div class="display-table-cell">
            <div class="container">
              <div class="row justify-content-center">
                <div class="col-lg-5">
                  <div class="card account-card">
                    <div class="card-body">
                      <div class="text-center mt-3">
                        <h3 class="font-weight-bold">
                          <a href="/" class="text-dark text-uppercase account-pages-logo">
                            <i class="mdi mdi-android-auto" /> 数据资产估值平台
                          </a>
                        </h3>
                      </div>

                      <div class="p-3 mt-4">
                        <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" auto-complete="on" label-position="left">
                          <div class="form-group">
                            <label for="username">用户名</label>
                            <input
                              id="username"
                              ref="username"
                              v-model="loginForm.username"
                              name="username"
                              type="text"
                              class="form-control"
                              placeholder="请输入用户名"
                              tabindex="1"
                            >
                          </div>

                          <div class="form-group">
                            <label for="userpassword">密码</label>
                            <input
                              id="userpassword"
                              :key="passwordType"
                              ref="password"
                              v-model="loginForm.password"
                              type="password"
                              class="form-control"
                              placeholder="请输入密码"
                              name="password"
                              tabindex="2"
                              auto-complete="on"
                              @keyup.enter.native="handleLogin"
                            >
                          </div>

                          <div class="mt-5">
                            <el-button
                              :loading="loading"
                              class="btn btn-custom btn-block"
                              type="primary"
                              style="width:100%;margin-bottom:30px;"
                              @click.native.prevent="handleLogin"
                            >登录</el-button>
                          </div>
                        </el-form>
                      </div>
                    </div>
                  </div>
                <!-- end card -->
                </div>
              <!-- end col -->
              </div>
            <!-- end row -->
            </div>
          </div>
        </div>
      </section>
    <!-- end account-pages  -->
    </div>
  </div>
</template>

<script>
import { validUsername } from '@/utils/validate'

export default {
  name: 'Login',
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        callback(new Error('Please enter the correct username'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 1) {
        callback(new Error('The password can not be less than 6 digits'))
      } else {
        callback()
      }
    }
    return {
      loginForm: {
        username: '',
        password: ''
      },
      loginRules: {
        username: [{ required: true, trigger: 'blur', validator: validateUsername }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }]
      },
      loading: false,
      passwordType: 'password',
      redirect: undefined
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  methods: {
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          this.loading = true
          this.$store.dispatch('user/login', this.loginForm).then(() => {
            this.$router.push({ path: this.redirect || '/' })
            this.loading = false
          }).catch(() => {
            this.loading = false
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>

<style scoped>
  @import "~@/assets/css/hiric.css";
</style>
