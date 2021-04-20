<template>
  <div :class="className" :style="{height:height,width:width}" style="z-index: 20" />
</template>

<script>
import echarts from 'echarts'
require('@/assets/js/walden')
import resize from '@/mixins/resize'
import { formatWeight } from '@/utils/common'

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
          text: '质量价值',
          top: '0',
          left: '25'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          data: ['质量价值参数', '质量价值权重']
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
            { name: '完整性', max: 1 },
            { name: '正确性', max: 1 },
            { name: '一致性', max: 1 },
            { name: '重复性', max: 1 }
          ],
          radius: 100,
          center: ['50%', '55%']
        }],
        series: [{
          name: '质量价值',
          type: 'radar',
          tooltip: {
            trigger: 'item'
          },
          areaStyle: { normal: {}},
          data: [
            {
              value: [
                this.detail.full,
                this.detail.correct,
                this.detail.uniformity,
                this.detail.repeatability
              ],
              name: '质量价值参数'
            },
            {
              value: formatWeight(this.detail.quality_weight),
              name: '质量价值权重'
            }
          ]
        }]
      })
    }
  }
}
</script>
