<template>
  <div>
    <el-row style="margin: 8% 0 0 4%;width: 90%">
      <el-col :span="8">
        <left-bar :bar-max="barMax" :detail="detail" />
      </el-col>
      <el-col :span="8">
        <gauge-grade :r="detail.R" />
        <radar :detail="detail" />
      </el-col>
      <el-col :span="8">
        <right-bar :bar-max="barMax" :detail="detail" />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import LeftBar from './LeftBar'
import GaugeGrade from './GaugeGrade'
import Radar from './Radar'
import RightBar from './RightBar'

export default {
  components: {
    LeftBar,
    GaugeGrade,
    Radar,
    RightBar
  },
  props: {
    detail: {
      type: Object,
      default: () => {}
    }
  },
  computed: {
    barMax: function() {
      return 1.2 * Math.max(this.detail.P, this.detail.C)
    }
  }
}
</script>
