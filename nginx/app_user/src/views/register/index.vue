<template>
  <div class="hiric">
    <div class="bg-account-pages py-4 py-sm-0">
      <div class="account-home-btn d-none d-sm-block">
        <router-link to="/index" class="text-white">
          <i class="mdi mdi-home h1" />
        </router-link>
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

                      <div class="p-2">
                        <form>
                          <div class="form-group" style="height: 65px">
                            <label for="firstname">用户名</label>
                            <input
                              id="firstname"
                              v-model="form.username"
                              type="text"
                              class="form-control"
                              placeholder="请输入用户名"
                            >
                          </div>

                          <div class="form-group" style="height: 65px">
                            <label for="userpassword">密码</label>
                            <input
                              id="userpassword"
                              v-model="form.password"
                              type="password"
                              class="form-control"
                              placeholder="请输入密码"
                            >
                          </div>

                          <div class="form-group" style="height: 65px">
                            <label for="email">邮箱</label>
                            <input
                              id="email"
                              v-model="form.email"
                              type="text"
                              class="form-control"
                              placeholder="请输入邮箱"
                            >
                          </div>

                          <div class="form-group" style="height: 65px">
                            <label for="email">联系方式</label>
                            <input
                              id="mobile"
                              v-model="form.mobile"
                              type="text"
                              class="form-control"
                              placeholder="请输入联系方式"
                            >
                          </div>

                          <div class="mt-5">
                            <button type="submit" class="btn btn-custom btn-block" @click="submit">注册</button>
                          </div>

                          <div class="mt-4 mb-0 text-center">
                            <p class="mb-0">
                              已有账号 请
                              <router-link tag="a" to="/login" class="text-danger">登录</router-link>
                            </p>
                          </div>
                        </form>
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
import { register } from '@/api/user'

export default {
  name: 'Register',
  data() {
    return {
      form: {
        username: '',
        password: '',
        email: '',
        mobile: ''
      }
    }
  },
  methods: {
    submit() {
      const tempData = Object.assign({}, this.form)
      register(tempData).then(() => {
        this.$notify({
          title: '注册成功！',
          message: '即将为您跳转登录页面',
          type: 'success',
          duration: 2000
        })
        setTimeout(() => {
          this.$router.push('/login')
        }, 1.5 * 1000)
      })
    }
  }
}
</script>

<style scoped>
@import "~@/styles/hiric/css/hiric.css";
</style>
