<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
// require('echarts/theme/macarons') // echarts theme
require('@/assets/js/walden')
import resize from './mixins/resize'
import { getWeekDay } from '@/utils'

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
      default: '350px'
    },
    autoResize: {
      type: Boolean,
      default: true
    },
    chartData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      chart: null
    }
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
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
      this.setOptions(this.chartData)
    },
    setOptions({ thisWeek, lastWeek } = {}) {
      this.chart.setOption({
        xAxis: {
          data: getWeekDay(),
          boundaryGap: false,
          axisTick: {
            show: false
          }
        },
        grid: {
          left: 10,
          right: 20,
          bottom: 20,
          top: 30,
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          },
          padding: [5, 10]
        },
        yAxis: {
          axisTick: {
            show: false
          }
        },
        legend: {
          data: ['本周', '上周']
        },
        series: [{
          name: '本周', itemStyle: {
            // normal: {
            //   color: '#FF005A',
            //   lineStyle: {
            //     color: '#FF005A',
            //     width: 2
            //   }
            // }
          },
          smooth: true,
          type: 'line',
          data: thisWeek,
          animationDuration: 2800,
          animationEasing: 'cubicInOut'
        },
        {
          name: '上周',
          smooth: true,
          type: 'line',
          itemStyle: {
            // normal: {
            //   color: '#3888fa',
            //   lineStyle: {
            //     color: '#3888fa',
            //     width: 2
            //   },
            //   areaStyle: {
            //     color: '#f3f8ff'
            //   }
            // }
          },
          data: lastWeek,
          animationDuration: 2800,
          animationEasing: 'quadraticOut'
        }]
      })
    }
  }
}
</script>
