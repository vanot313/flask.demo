<template>
  <div>
    <el-row style="margin-top: 50px">
      <bar :detail="detail" />
    </el-row>

    <el-row style="margin-top: 50px">
      <el-col :span="12">
        <left-radar :detail="detail" />
      </el-col>
      <el-col :span="12">
        <right-radar :detail="detail" />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Bar from './Bar'
import LeftRadar from './LeftRadar'
import RightRadar from './RightRadar'

export default {
  components: {
    LeftRadar,
    RightRadar,
    Bar
  },
  props: {
    detail: {
      type: Object,
      default: () => {}
    }
  }
}
</script>

<style scoped>

</style>
