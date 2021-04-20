<template>
  <div class="fonik">
    <layout :title="title" />

    <div class="wrapper">
      <div class="container-fluid">

        <div class="row">
          <div class="col-12">
            <!-- Left sidebar -->
            <div class="email-leftbar mb-3">
              <router-link to="" class="btn btn-danger btn-rounded btn-custom btn-block waves-effect waves-light">个人中心</router-link>

              <div class="mail-list m-t-20">
                <router-link to="/profile">个人信息</router-link>
                <a href="#">我的头像</a>
                <a href="#">账号安全</a>
                <router-link to="/expert/apply" class="active">专家资格申请</router-link>
              </div>
            </div>
            <!-- End Left sidebar -->

            <!-- Right Sidebar -->
            <div class="email-rightbar mb-3">
              <div class="card m-b-20">
                <div class="card-body">

                  <h4 class="mt-0 header-title">专家资格申请</h4>
                  <p class="text-muted m-b-30 font-14">Expert Qualification Application</p>

                  <div class="form-group row">
                    <label class="col-sm-2 col-form-label">姓名</label>
                    <div class="col-sm-10">
                      <input v-model="form.realname" class="form-control" type="text">
                    </div>
                  </div>

                  <div class="form-group row">
                    <label class="col-sm-2 col-form-label">邮箱</label>
                    <div class="col-sm-10">
                      <input v-model="form.email" class="form-control" type="email">
                    </div>
                  </div>

                  <div class="form-group row">
                    <label class="col-sm-2 col-form-label">联系方式</label>
                    <div class="col-sm-10">
                      <input v-model="form.mobile" class="form-control" type="tel">
                    </div>
                  </div>

                  <div class="form-group row">
                    <label class="col-sm-2 col-form-label">职称</label>
                    <div class="col-sm-10">
                      <input v-model="form.job_title" class="form-control" type="text">
                    </div>
                  </div>

                  <div class="form-group row">
                    <label class="col-sm-2 col-form-label">简介</label>
                    <div class="col-sm-10">
                      <input v-model="form.introduction" class="form-control" type="text">
                    </div>
                  </div>

                  <div class="form-group text-center m-b-0 m-t-20">
                    <button type="button" class="btn btn-primary waves-effect waves-light" @click="submit">提 交</button>
                  </div>

                </div>
              </div>
            </div>
          </div>
          <!-- end col -->
        </div>
        <!-- end row -->
      </div>
      <!-- end container -->
    </div>
    <!-- end wrapper -->
  </div>
</template>

<script>
import Layout from '@/components/Layout/index'
import { apply_expert } from '@/api/user'
import { Message } from 'element-ui'

export default {
  components: {
    Layout
  },
  data() {
    return {
      title: '专家资格申请',
      form: {
        realname: '',
        email: '',
        mobile: '',
        job_title: '',
        introduction: ''
      }
    }
  },
  methods: {
    submit() {
      const tempData = Object.assign({}, this.form)
      apply_expert(tempData).then(() => {
        Message({
          message: '提交成功！请等待管理员审核',
          type: 'success',
          duration: 3 * 1000
        })
      })
    }
  }
}
</script>

<style scoped>

</style>
