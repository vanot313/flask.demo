<template>
  <div>
    <el-dialog :title="title" :visible.sync="costFormVisible" :before-close="closeCostDialog">
      <el-form ref="form" :rules="rules" :model="temp" label-position="left" label-width="170px" style="width: 400px; margin-left:50px;">
        <el-form-item label="工单ID">
          <span>{{ temp.order_id }}</span>
        </el-form-item>

        <el-form-item label="评估方法">
          <span>成本法</span>
        </el-form-item>

        <el-form-item label="投资收益率">
          <el-input v-model="temp.R " />
        </el-form-item>

        <el-form-item label="重置成本">
          <el-input v-model="temp.C " />
        </el-form-item>

        <el-form-item label="固有价值因素修正系数">
          <el-input v-model="temp.II" />
        </el-form-item>

        <el-form-item label="市场价值因素修正系数">
          <el-input v-model="temp.M" />
        </el-form-item>

        <el-form-item label="环境约束因素修正系数">
          <el-input v-model="temp.E" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="closeCostDialog">
          取消
        </el-button>
        <el-button type="primary" @click="assessCost">
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
    costFormVisible: {
      type: Boolean
    }
  },
  data() {
    return {
      title: '成本法评估',
      rules: {}
    }
  },
  methods: {
    assessCost() {
      this.$parent.assessCost()
    },
    closeCostDialog() {
      this.$parent.closeCostDialog()
    }
  }
}
</script>
