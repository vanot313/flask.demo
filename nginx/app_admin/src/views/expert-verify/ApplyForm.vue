<template>
  <div>
    <el-dialog :title="apply" :visible.sync="applyFormVisible" :before-close="closeEditDialog">
      <el-form ref="form" :rules="rules" :model="temp" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
        <el-form-item label="申请ID">
          <el-input v-model="temp.apply_id" :disabled="true" />
        </el-form-item>

        <el-form-item label="用户ID">
          <el-input v-model="temp.user_id" :disabled="true" />
        </el-form-item>

        <el-form-item label="用户名">
          <el-input v-model="temp.username" :disabled="true" />
        </el-form-item>

        <el-form-item label="邮箱">
          <el-input v-model="temp.email" :disabled="true" />
        </el-form-item>

        <el-form-item label="联系方式">
          <el-input v-model="temp.mobile" :disabled="true" />
        </el-form-item>

        <el-form-item label="真名">
          <el-input v-model="temp.realname" :disabled="true" />
        </el-form-item>

        <el-form-item label="职称">
          <el-input v-model="temp.job_title" :disabled="true" />
        </el-form-item>

        <el-form-item label="简介">
          <el-input v-model="temp.introduction" :autosize="{ minRows: 2, maxRows: 4}" type="textarea" placeholder="" :disabled="true" />
        </el-form-item>

        <el-form-item label="申请状态">
          <el-select v-model="temp.status">
            <el-option label="未通过" value="0" />
            <el-option label="已通过" value="1" />
            <el-option label="已拒绝" value="2" />
          </el-select>
        </el-form-item>
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="closeEditDialog">
          取消
        </el-button>
        <el-button type="primary" @click="updateData">
          确认
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  props: {
    temp: {
      type: Object,
      default: () => {}
    },
    rules: {
      type: Object,
      default: () => {}
    },
    applyFormVisible: {
      type: Boolean
    }
  },
  data() {
    return {
      apply: '专家审核',
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now() - 8.64e6
        }
      }
    }
  },
  methods: {
    updateData() {
      this.$parent.updateData()
    },
    closeEditDialog() {
      this.$parent.closeEditDialog()
    }
  }
}
</script>
