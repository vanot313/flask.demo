<template>
  <div class="rightBar" :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('@/assets/js/walden')
import resize from '@/views/dashboard/components/mixins/resize'

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
      default: '70%'
    },
    height: {
      type: String,
      default: '600px'
    },
    barMax: {
      type: Number,
      default: undefined
    },
    detail: {
      type: Object,
      default: () => {}
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
          text: '评估结果',
          // padding: [5, 5, 5, 10],
          left: '80%'
          // right: '25%'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        grid: {
          top: 50,
          left: '64%',
          right: '9%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [{
          type: 'category',
          data: ['评估结果'],
          axisTick: {
            // alignWithLabel: true
            show: false
          },
          inverse: true
        }],
        yAxis: [{
          type: 'value',
          position: 'right',
          // axisLine: {
          //   show: false
          // },
          axisTick: {
            show: false
          },
          // show: false,
          max: this.barMax
        }],
        series: [{
          type: 'bar',
          itemStyle: {
            normal: {
              label: {
                show: true, // 开启显示
                position: 'top', // 在上方显示
                textStyle: { // 数值样式
                  fontSize: 16,
                  padding: [0, 0, 10, 0]
                }
              }
            }
          },
          name: '价格',
          barWidth: '50%',
          data: [this.detail.P],
          animationDuration
        }]
      })
    }
  }
}
</script>

<style scoped>
.rightBar {
  position: absolute;
  right: 0;
  z-index: 10;
}
</style>
