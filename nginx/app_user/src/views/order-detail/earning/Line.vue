<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('@/assets/js/walden')
import resize from '@/mixins/resize'

function xYear(n) {
  const x = []
  for (let i = 1; i < parseInt(n) + 1; i++) {
    x.push('第' + i + '年')
  }
  return x
}

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
          text: '每年预期收益',
          left: '30px'
        },
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          type: 'category',
          data: xYear(this.detail.n)
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          // data: [100000, 80000, 90000],
          data: JSON.parse(this.detail.RI),
          type: 'line',
          smooth: true
        }]
      })
    }
  }
}
</script>
