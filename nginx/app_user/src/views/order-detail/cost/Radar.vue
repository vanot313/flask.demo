<template>
  <div :class="className" :style="{height:height,width:width}" style="z-index: 20" />
</template>

<script>
import echarts from 'echarts'
require('@/assets/js/walden')
import resize from '@/mixins/resize'

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
          text: '修正系数',
          top: '0'
        },
        tooltip: {
          trigger: 'item'
        },
        radar: [{
          shape: 'circle',
          name: {
            textStyle: {
              color: '#fff',
              backgroundColor: '#999',
              borderRadius: 3,
              padding: [3, 5]
            }
          },
          indicator: [
            { text: '固有价值因素', max: 1 },
            { name: '市场价值因素', max: 1 },
            { name: '环境约束因素', max: 1 }
          ],
          radius: 90,
          center: ['50%', '50%']
        }],
        series: [{
          name: '修正系数',
          type: 'radar',
          tooltip: {
            trigger: 'item'
          },
          lineStyle: {
            color: '#a0a7e6'
          },
          areaStyle: {
            color: '#a0a7e6'
          },
          // areaStyle: { normal: {}},
          data: [
            {
              value: [this.detail.II, this.detail.M, this.detail.E],
              name: '修正系数'
            }
          ]
        }]
      })
    }
  }
}
</script>
