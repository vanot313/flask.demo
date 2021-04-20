<template>
  <div>
    <el-dialog :title="edit" :visible.sync="editFormVisible" :before-close="closeEditDialog">
      <el-form ref="form" :rules="rules" :model="temp" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
        <el-form-item label="ID" prop="id">
          <el-input v-model="temp.id" :disabled="true" />
        </el-form-item>

        <el-form-item label="用户名" prop="username">
          <el-input v-model="temp.username" :disabled="true" />
        </el-form-item>

        <el-form-item label="邮箱" prop="email">
          <el-input v-model="temp.email" />
        </el-form-item>

        <el-form-item label="联系方式" prop="mobile">
          <el-input v-model="temp.mobile" />
        </el-form-item>

        <el-form-item label="地址" prop="location">
          <el-input v-model="temp.location" />
        </el-form-item>

        <el-form-item label="生日" prop="birth">
          <el-date-picker
            v-model="temp.birth"
            type="date"
            format="yyyy-MM-dd"
            value-format="yyyy-MM-dd"
            placeholder="请选择您的生日"
            :picker-options="pickerOptions"
          />
        </el-form-item>

        <el-form-item label="简介">
          <el-input v-model="temp.description" :autosize="{ minRows: 2, maxRows: 4}" type="textarea" placeholder="" />
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
    editFormVisible: {
      type: Boolean
    }
  },
  data() {
    return {
      edit: '编辑用户',
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
