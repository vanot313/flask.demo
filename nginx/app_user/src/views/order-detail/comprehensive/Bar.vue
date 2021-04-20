<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('@/assets/js/walden')
import resize from '@/mixins/resize'

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
          text: '价值估分',
          // padding: [5, 5, 5, 10],
          left: '2%'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        grid: {
          top: 50,
          left: '2%',
          right: '2%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [{
          type: 'value',
          position: 'left',
          axisTick: {
            show: false
          },
          max: 100
        }],
        yAxis: [{
          type: 'category',
          data: ['资产价值估分', '质量价值估分', '应用价值估分'],
          axisTick: {
            show: false
          },
          axisLabel: {
            interval: 0,
            fontSize: 16
          }
        }],
        series: [{
          type: 'bar',
          itemStyle: {
            normal: {
              label: {
                show: true, // 开启显示
                position: 'right', // 在上方显示
                textStyle: { // 数值样式
                  fontSize: 16,
                  padding: [0, 0, 10, 0]
                }
              }
            }
          },
          name: '分数',
          barWidth: '40%',
          data: [
            parseFloat(this.detail.S).toFixed(2),
            parseFloat(this.detail.Sq).toFixed(2),
            parseFloat(this.detail.Sa).toFixed(2)
          ],
          animationDuration
        }]
      })
    }
  }
}
</script>
