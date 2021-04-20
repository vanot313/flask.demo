<template>
  <el-form :label-position="labelPosition">
    <el-form-item label="邮箱">
      <el-input v-model="user.email" />
    </el-form-item>

    <el-form-item label="手机号码">
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

    <el-form-item align="middle">
      <el-button type="primary" @click="submit">更新</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { updateInfo } from '@/api/user'

export default {
  props: {
    user: {
      type: Object,
      default: () => {
        return {
          id: '',
          email: '',
          mobile: '',
          location: '',
          birth: undefined,
          description: ''
        }
      }
    }
  },
  data() {
    return {
      labelPosition: 'top',
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now() - 8.64e6
        }
      }
    }
  },
  methods: {
    submit: function() {
      updateInfo(this.user).then(res => {
        this.$notify({
          title: 'Success',
          message: res.msg,
          type: 'success',
          duration: 2000
        })
      })
    }
  }
}
</script>
