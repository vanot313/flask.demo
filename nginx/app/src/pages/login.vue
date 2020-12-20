<template>
  <div>
    <el-form ref="loginForm" :model="form" :rules="rules" lable-width="80px" class="login-box">
      <h3 class="login-title">欢迎登陆</h3>
      <el-form-item label="账号" prop="username">
        <!--v-model绑定表单-->
        <el-input type="text" placeholder="请输入账号" v-model="form.username"/>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" placeholder="请输入密码" v-model="form.password"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">登录</el-button>
      </el-form-item>
    </el-form>

    <el-dialog
      title="温馨提示"
      :visible.sync="dialogVisible"
      width="30%">
      <span>请输入账号和密码</span>
      <span slot="footer" class="dialog-footer">
            <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
          </span>
    </el-dialog>
  </div>
</template>

<script>
  import {getLoginStatus} from '../api/index';

  export default {
    name: "Login",
    data: function () {
      return {
        form: {
          username: 'admin',
          password: 'admin'
        },
        // 表单验证，在 el-form-item 元素添加 prop 属性
        rules: {
          //飙泪ur:失焦
          username: [
            {required: true,message: '账号不可为空', trigger: 'blur'}
          ],
          password: [
            {required: true,message: '密码不能为空', trigger: 'blur'}
          ]
        },

        //对话显示和隐藏
        dialogVisible: false
      };
    },
    methods: {
      onSubmit(){
        if (!this.form.username) {this.dialogVisible=true;return false;}
        getLoginStatus()
          .then((res) => {
            console.log(res.title)
          });
      }
    }
  }
</script>

<style lang="scss" scoped>
  .login-box {
    border: 1px solid #DCDFE6;
    width: 350px;
    margin: 180px auto;
    padding: 35px 35px 15px 35px;
    border-radius: 5px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    box-shadow: 0 0 25px #909399;
  }

  .login-title {
    text-align: center;
    margin: 0 auto 40px auto;
    color: #303133;
  }
</style>
