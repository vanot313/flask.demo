<template>
  <div :class="className" :style="{height:height,width:width}" style="z-index: 20" />
</template>

<script>
import echarts from 'echarts'
require('@/assets/js/walden')
import resize from '@/views/dashboard/components/mixins/resize'
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
          text: '应用价值',
          top: '0',
          left: '25'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          data: ['应用价值参数', '应用价值权重']
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
            { name: '稀缺性', max: 1 },
            { name: '时效性', max: 1 },
            { name: '多维性', max: 1 },
            { name: '经济性', max: 1 }
          ],
          radius: 100,
          center: ['50%', '55%']
        }],
        series: [{
          name: '应用价值',
          type: 'radar',
          tooltip: {
            trigger: 'item'
          },
          areaStyle: { normal: {}},
          data: [
            {
              value: [
                this.detail.rareness,
                this.detail.timeliness,
                this.detail.dimensional,
                this.detail.economy
              ],
              name: '应用价值参数'
            },
            {
              value: formatWeight(this.detail.applied_weight),
              name: '应用价值权重'
            }
          ]
        }]
      })
    }
  }
}
</script>
