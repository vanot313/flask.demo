<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('@/assets/js/walden')
import resize from '@/views/dashboard/components/mixins/resize'

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
    r: {
      type: String,
      default: undefined
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
          text: '投资收益率'
        },
        series: [{
          type: 'gauge',
          center: ['50%', '70%'],
          radius: '80%',
          startAngle: 180,
          endAngle: 0,
          min: 0,
          max: 1,
          splitNumber: 8,
          axisLine: {
            lineStyle: {
              width: 6,
              color: [
                [0.25, '#FF6E76'],
                [0.5, '#FDDD60'],
                [0.75, '#58D9F9'],
                [1, '#7CFFB2']
              ]
            }
          },
          pointer: {
            icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
            length: '75%',
            width: 5,
            offsetCenter: [100, '-60%'],
            itemStyle: {
              color: 'auto'
            }
          },
          axisTick: {
            length: 12,
            lineStyle: {
              color: 'auto',
              width: 2
            }
          },
          splitLine: {
            length: 20,
            lineStyle: {
              color: 'auto',
              width: 5
            }
          },
          axisLabel: {
            color: '#464646',
            fontSize: 20,
            distance: -60,
            formatter: function(value) {
              if (value === 0.75) {
                return '0.75'
              } else if (value === 0.5) {
                return '0.5'
              } else if (value === 0.25) {
                return '0.25'
              }
            }
          },
          title: {
            offsetCenter: [0, '-20%'],
            fontSize: 20
          },
          detail: {
            fontSize: 20,
            offsetCenter: [0, '20%'],
            valueAnimation: true,
            formatter: function(value) {
              return Math.round(value * 100) + '%'
            },
            color: 'auto'
          },
          data: [{
            value: this.r
            // name: '投资收益率'
          }]
        }]
      })
    }
  }
}
</script>
