<template>
  <div class="fonik">
    <layout />

    <div class="wrapper">
      <div class="container-fluid">

        <div class="row">
          <div class="col-12">
            <!-- Left sidebar -->
            <div class="email-leftbar mb-3">
              <router-link to="/profile" class="btn btn-danger btn-rounded btn-custom btn-block waves-effect waves-light">个人中心</router-link>

              <div class="mail-list m-t-20">
                <router-link to="/profile" class="active">个人信息</router-link>
                <a href="#">我的头像</a>
                <a href="#">账号安全</a>
                <router-link to="/expert/apply">专家资格申请</router-link>
              </div>
            </div>
            <!-- End Left sidebar -->

            <!-- Right Sidebar -->
            <div class="email-rightbar mb-3">

              <div class="card m-t-20">
                <div class="card-body">

                  <h4 class="mt-0 header-title">个人信息编辑</h4>
                  <p class="text-muted m-b-30 font-14">Information Edit</p>

                  <el-form label-width="100px" :label-position="labelPosition">
                    <el-form-item label="邮箱">
                      <el-input v-model="user.email" />
                    </el-form-item>

                    <el-form-item label="联系方式">
                      <el-input v-model="user.mobile" />
                    </el-form-item>

                    <el-form-item label="地址">
                      <el-input v-model="user.location" />
                    </el-form-item>

                    <el-form-item label="生日">
                      <el-date-picker
                        v-model="user.birth"
                        type="date"
                        format="yyyy-MM-dd"
                        value-format="yyyy-MM-dd"
                        placeholder="请选择您的生日"
                        :picker-options="pickerOptions"
                      />
                    </el-form-item>

                    <el-form-item label="描述">
                      <el-input v-model="user.description" />
                    </el-form-item>

                    <div class="form-group text-center m-b-0 m-t-20">
                      <button type="button" class="btn btn-primary waves-effect waves-light" @click="submit">更 新</button>
                    </div>
                  </el-form>
                </div>
              </div>
            </div>
            <!-- end Col-9 -->
          </div>
        </div>
        <!-- End row -->
      </div>
      <!-- end container -->
    </div>
    <!-- end wrapper -->
  </div>
</template>

<script>
import Layout from '@/components/Layout/index'
import { getInfo, updateInfo } from '@/api/user'
import { Message } from 'element-ui'

export default {
  components: {
    Layout
  },
  data() {
    return {
      user: {
        email: '',
        mobile: '',
        location: '',
        birth: undefined,
        description: ''
      },
      labelPosition: 'right',
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now() - 8.64e6
        }
      }
    }
  },
  created() {
    this.getUser()
  },
  methods: {
    getUser() {
      getInfo().then(response => {
        const { email, mobile, location, birth, description } = response.data

        this.user = {
          email: email,
          mobile: mobile,
          location: location,
          birth: birth === 'None' ? undefined : birth,
          description: description
        }
      }).catch(error => {
        console.log(error)
      })
    },
    submit: function() {
      updateInfo(this.user).then(res => {
        Message({
          message: '修改成功',
          type: 'success',
          duration: 2 * 1000
        })
      })
    }
  }
}
</script>
