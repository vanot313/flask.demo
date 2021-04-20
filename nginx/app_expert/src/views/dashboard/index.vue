<template>
  <div class="dashboard-editor-container">
    <panel-group @handleSetLineChartData="handleSetLineChartData" />

    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
      <line-chart :chart-data="lineChartData" />
    </el-row>

    <el-row :gutter="8">
      <el-col :xs="{span: 48}" :sm="{span: 36}" :md="{span: 36}" :lg="{span: 18}" :xl="{span: 18}" style="padding-right:8px;margin-bottom:30px;">
        <div class="chart-wrapper">
          <HeatmapChart />
        </div>
      </el-col>
      <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 6}" :xl="{span: 6}" style="margin-bottom:30px;">
        <div class="chart-wrapper">
          <todo-list />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import PanelGroup from './components/PanelGroup'
import LineChart from './components/LineChart'
import TodoList from './components/TodoList'
import HeatmapChart from './components/HeatmapChart'

const lineChartData = {
  newUsers: {
    thisWeek: [100, 120, 161, 134, 105, 160, 165],
    lastWeek: [120, 82, 91, 154, 162, 140, 145]
  },
  newViews: {
    thisWeek: [200, 192, 120, 144, 160, 130, 140],
    lastWeek: [180, 160, 151, 106, 145, 150, 130]
  },
  newEvaluations: {
    thisWeek: [80, 100, 121, 104, 105, 90, 100],
    lastWeek: [120, 90, 100, 138, 142, 130, 130]
  },
  newAssets: {
    thisWeek: [130, 140, 141, 142, 145, 150, 160],
    lastWeek: [120, 82, 91, 154, 162, 140, 130]
  }
}

export default {
  name: 'DashboardAdmin',
  components: {
    PanelGroup,
    LineChart,
    TodoList,
    HeatmapChart
  },
  data() {
    return {
      lineChartData: lineChartData.newUsers
    }
  },
  methods: {
    handleSetLineChartData(type) {
      this.lineChartData = lineChartData[type]
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .github-corner {
    position: absolute;
    top: 0px;
    border: 0;
    right: 0;
  }

  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
