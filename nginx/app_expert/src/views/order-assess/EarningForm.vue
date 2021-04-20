<template>
  <div>
    <el-dialog :title="title" :visible.sync="earningFormVisible" :before-close="closeEarningDialog">
      <el-form ref="form" :rules="rules" :model="temp" label-position="left" label-width="170px" style="width: 400px; margin-left:50px;">
        <el-form-item label="工单ID">
          <span>{{ temp.order_id }}</span>
        </el-form-item>

        <el-form-item label="评估方法">
          <span>收益法</span>
        </el-form-item>

        <el-form-item label="折现率">
          <el-input v-model="temp.r " />
        </el-form-item>

        <el-form-item label="预期获利持续年限">
          <el-input v-model.number.lazy="temp.n " />
        </el-form-item>

        <div v-for="mount of temp.n" :key="mount">
          <el-form-item :label="'第'+mount+'年预计获利'">
            <el-input
              v-model.lazy="temp.RI[mount-1]"
              placeholder="请输入内容"
              required=""
            /></el-form-item>
        </div>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="closeEarningDialog">
          取消
        </el-button>
        <el-button type="primary" @click="assessEarning">
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
    earningFormVisible: {
      type: Boolean
    }
  },
  data() {
    return {
      title: '收益法评估',
      rules: {}
    }
  },
  methods: {
    assessEarning() {
      this.$parent.assessEarning()
    },
    closeEarningDialog() {
      this.$parent.closeEarningDialog()
    }
  }
}
</script>
