<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
// require('echarts/theme/macarons') // echarts theme
require('@/assets/js/walden')
import resize from './mixins/resize'
import { getWeekDay } from '@/utils'

const animationDuration = 6000

export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '300px'
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'walden')

      this.chart.setOption({
        title: {
          text: '评估方法数量统计',
          subtext: '111'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        grid: {
          top: 10,
          left: '2%',
          right: '2%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [{
          type: 'category',
          data: getWeekDay(),
          axisTick: {
            alignWithLabel: true
          }
        }],
        yAxis: [{
          type: 'value',
          axisTick: {
            show: false
          }
        }],
        series: [{
          name: '成本法',
          type: 'bar',
          stack: 'value',
          barWidth: '60%',
          data: [79, 52, 65, 24, 36, 44, 56],
          animationDuration
        }, {
          name: '收益法',
          type: 'bar',
          stack: 'value',
          barWidth: '60%',
          data: [85, 29, 35, 89, 45, 66, 72],
          animationDuration
        }, {
          name: '综合法',
          type: 'bar',
          stack: 'value',
          barWidth: '60%',
          data: [10, 25, 33, 36, 44, 48, 55],
          animationDuration
        }, {
          name: '市场法',
          type: 'bar',
          stack: 'value',
          barWidth: '60%',
          data: [88, 77, 61, 45, 25, 67, 71],
          animationDuration
        }]
      })
    }
  }
}
</script>
