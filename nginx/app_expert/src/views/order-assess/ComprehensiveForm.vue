<template>
  <div>
    <el-dialog :title="title" :visible.sync="comprehensiveFormVisible" :before-close="closeComprehensiveDialog">
      <el-form ref="form" :rules="rules" :model="temp" label-position="left" label-width="170px" style="width: 600px; margin-left:50px;">
        <el-form-item label="工单ID" prop="order_id">
          <span>{{ temp.order_id }}</span>
        </el-form-item>

        <el-form-item label="评估方法" prop="method">
          <span>综合估值法</span>
        </el-form-item>

        <el-form-item label="稀缺性">
          <el-input v-model="temp.rareness" />
        </el-form-item>
        <el-form-item label="时效性">
          <el-input v-model="temp.timeliness" />
        </el-form-item>
        <el-form-item label="多维性">
          <el-input v-model="temp.dimensional" />
        </el-form-item>
        <el-form-item label="经济性">
          <el-input v-model="temp.economy" />
        </el-form-item>

        <el-form-item label="质量价值矩阵">
          <el-row type="flex" :gutter="10" class="title">
            <el-col :span="4" :offset="4"><el-tag>完整性</el-tag></el-col>
            <el-col :span="4"><el-tag>正确性</el-tag></el-col>
            <el-col :span="4"><el-tag>一致性</el-tag></el-col>
            <el-col :span="4"><el-tag>重复性</el-tag></el-col>
            <el-col :span="4" />
          </el-row>
          <el-row :gutter="10">
            <el-col :span="4"><el-tag>完整性</el-tag></el-col>
            <el-col :span="4">
              <el-input placeholder="1" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="input1" v-model="temp.quality_weight[0]" @change="getReciprocal('input1','uninput1')" />
            </el-col>
            <el-col :span="4">
              <el-input id="input2" v-model="temp.quality_weight[1]" @change="getReciprocal('input2','uninput2')" />
            </el-col>
            <el-col :span="4">
              <el-input id="input3" v-model="temp.quality_weight[2]" @change="getReciprocal('input3','uninput4')" />
            </el-col>
          </el-row>
          <el-row :gutter="10">
            <el-col :span="4"><el-tag>正确性</el-tag></el-col>
            <el-col :span="4">
              <el-input id="uninput1" value="" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input placeholder="1" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="input4" v-model="temp.quality_weight[3]" @change="getReciprocal('input4','uninput3')" />
            </el-col>
            <el-col :span="4">
              <el-input id="input5" v-model="temp.quality_weight[4]" @change="getReciprocal('input5','uninput5')" />
            </el-col>
          </el-row>
          <el-row :gutter="10">
            <el-col :span="4"><el-tag>一致性</el-tag></el-col>
            <el-col :span="4">
              <el-input id="uninput2" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="uninput3" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input placeholder="1" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="input6" v-model="temp.quality_weight[5]" @change="getReciprocal('input6','uninput6')" />
            </el-col>
          </el-row>
          <el-row :gutter="10">
            <el-col :span="4"><el-tag>重复性</el-tag></el-col>
            <el-col :span="4">
              <el-input id="uninput4" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="uninput5" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="uninput6" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input placeholder="1" :disabled="true" />
            </el-col>
          </el-row>
        </el-form-item>

        <el-form-item label="应用价值矩阵">
          <el-row type="flex" :gutter="10" class="title">
            <el-col :span="4" :offset="4"><el-tag>稀缺性</el-tag></el-col>
            <el-col :span="4"><el-tag>时效性</el-tag></el-col>
            <el-col :span="4"><el-tag>多维性</el-tag></el-col>
            <el-col :span="4"><el-tag>经济性</el-tag></el-col>
            <el-col :span="4" />
          </el-row>
          <el-row :gutter="10">
            <el-col :span="4"><el-tag>稀缺性</el-tag></el-col>
            <el-col :span="4">
              <el-input placeholder="1" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="input7" v-model="temp.applied_weight[0]" @change="getReciprocal('input7','uninput7')" />
            </el-col>
            <el-col :span="4">
              <el-input id="input8" v-model="temp.applied_weight[1]" @change="getReciprocal('input8','uninput8')" />
            </el-col>
            <el-col :span="4">
              <el-input id="input9" v-model="temp.applied_weight[2]" @change="getReciprocal('input9','uninput10')" />
            </el-col>
          </el-row>
          <el-row :gutter="10">
            <el-col :span="4"><el-tag>时效性</el-tag></el-col>
            <el-col :span="4">
              <el-input id="uninput7" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input placeholder="1" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="input10" v-model="temp.applied_weight[3]" @change="getReciprocal('input10','uninput9')" />
            </el-col>
            <el-col :span="4">
              <el-input id="input11" v-model="temp.applied_weight[4]" @change="getReciprocal('input11','uninput11')" />
            </el-col>
          </el-row>
          <el-row :gutter="10">
            <el-col :span="4"><el-tag>多维性</el-tag></el-col>
            <el-col :span="4">
              <el-input id="uninput8" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="uninput9" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input placeholder="1" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="input12" v-model="temp.applied_weight[5]" @change="getReciprocal('input12','uninput12')" />
            </el-col>
          </el-row>
          <el-row :gutter="10">
            <el-col :span="4"><el-tag>经济性</el-tag></el-col>
            <el-col :span="4">
              <el-input id="uninput10" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="uninput11" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input id="uninput12" :disabled="true" />
            </el-col>
            <el-col :span="4">
              <el-input placeholder="1" :disabled="true" />
            </el-col>
          </el-row>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="closeComprehensiveDialog">
          取消
        </el-button>
        <el-button type="primary" @click="assessComprehensive">
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
    comprehensiveFormVisible: {
      type: Boolean
    }
  },
  data() {
    return {
      title: '综合法评估',
      rules: {}
    }
  },
  methods: {
    assessComprehensive() {
      this.$parent.assessComprehensive()
    },
    closeComprehensiveDialog() {
      this.$parent.closeComprehensiveDialog()
    },
    getReciprocal(id1, id2) {
      document.getElementById(id2).value = parseFloat(1 / parseInt(document.getElementById(id1).value)).toFixed(2)
      if (document.getElementById(id1).value === '') { document.getElementById(id2).value = '' }
    }
  }
}
</script>

<style scoped>
.el-row {
  margin-bottom: 10px;
}
.el-col {
  border-radius: 4px;
}
.title .el-tag{
  display:flex;
  justify-content:center;/*主轴上居中*/
  align-items:center;/*侧轴上居中*/
}
</style>

