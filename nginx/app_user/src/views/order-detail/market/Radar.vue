<template>
  <div :class="className" :style="{height:height,width:width}" />
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
      default: '230px'
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
          text: '数据维度',
          top: '40'
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
            { name: '颗粒度', max: 10 },
            { name: '多维度', max: 10 },
            { name: '活性度', max: 10 },
            { name: '规模度', max: 10 },
            { name: '关联度', max: 10 }
          ],
          radius: 90,
          center: ['50%', '60%']
        }],
        series: [{
          name: '数据维度',
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
          data: [
            {
              value: [this.detail.graininess, this.detail.dimension, this.detail.activity, this.detail.scale, this.detail.correlation],
              name: '数据维度'
            }
          ]
        }]
      })
    }
  }
}
</script>
