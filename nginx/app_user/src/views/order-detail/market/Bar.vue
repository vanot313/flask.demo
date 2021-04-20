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
      default: '400px'
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
          text: '参数评分',
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
          type: 'category',
          data: ['数据量', '数据大小', '数据增长速度', '数据覆盖范围', '数据属性数量', '数据来源种类', '数据维护频率', '流入数据频率', '流出数据频率'],
          axisTick: {
            // alignWithLabel: true
            show: false
          },
          axisLabel: {
            interval: 0,
            fontSize: 16
            // rotate: 45
          }
        }],
        yAxis: [{
          type: 'value',
          position: 'left',
          // axisLine: {
          //   show: false
          // },
          axisTick: {
            show: false
          }
          // show: false,
          // max: 3
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
          barWidth: '40%',
          data: [
            this.detail.amount,
            this.detail.size,
            this.detail.growth,
            this.detail.coverage,
            this.detail.attribute,
            this.detail.source,
            this.detail.maintenance,
            this.detail.incoming,
            this.detail.outgoing
          ],
          animationDuration
        }]
      })
    }
  }
}
</script>
