<template>
  <div style="width: 90%;margin: 3% 0 0 5%">
    <el-row :gutter="12" style="padding: 50px 40px 20px 40px">
      <el-col :span="8">
        <el-card shadow="always" style="text-align: center;font-size: 30px;background-color: #7B68EE;color: #FFFFFF;border-radius: 25px;">
          评估价值：￥{{ detail.P }}
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="always" style="text-align: center;font-size: 30px;background-color: #1E90FF;color: #FFFFFF;border-radius: 25px;">
          预期收益持续年限：{{ parseInt(detail.n) }}年
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="always" style="text-align: center;font-size: 30px;background-color: #2dba2d;color: #FFFFFF;border-radius: 25px;">
          折现率：{{ detail.r * 100 }}%
        </el-card>
      </el-col>
    </el-row>
    <!-- end row -->
    <LineSmooth :detail="detail" style="margin-top: 40px" />
  </div>
</template>

<script>
import LineSmooth from './Line'

export default {
  components: {
    LineSmooth
  },
  props: {
    detail: {
      type: Object,
      default: () => {}
    }
  }
}
</script>
