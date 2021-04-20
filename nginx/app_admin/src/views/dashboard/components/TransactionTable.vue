<template>
  <el-table :data="list" style="width: 100%;padding-top: 15px;">
    <el-table-column label="工单ID" width="150" align="center">
      <template slot-scope="scope">
        {{ scope.row.order_id }}
      </template>
    </el-table-column>

    <el-table-column label="评估方法" width="150" align="center">
      <template slot-scope="{row}">
        <el-tag>
          {{ row.method | methodFilter }}
        </el-tag>
      </template>
    </el-table-column>

    <el-table-column label="评估专家" width="150" align="center">
      <template slot-scope="scope">
        {{ scope.row.expert_name }}
      </template>
    </el-table-column>

    <el-table-column label="创建日期" width="220" align="center">
      <template slot-scope="scope">
        {{ scope.row.create_time }}
      </template>
    </el-table-column>

    <el-table-column label="修改日期" width="220" align="center">
      <template slot-scope="scope">
        {{ scope.row.modify_time }}
      </template>
    </el-table-column>

    <el-table-column label="状态" width="150" align="center">
      <template slot-scope="{row}">
        <el-tag :type="row.status | statusFilter1">
          {{ row.status |statusFilter2 }}
        </el-tag>
      </template>
    </el-table-column>

    <el-table-column label="结果" min-width="150" align="center">
      <template slot-scope="scope">
        {{ scope.row.result }}
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import { searchWorkOrder } from '@/api/admin'

export default {
  filters: {
    statusFilter1(status) {
      const statusMap = {
        '0': 'danger',
        '1': 'success',
        '2': 'info'
      }
      return statusMap[status]
    },
    statusFilter2(status) {
      const statusMap = {
        '0': '未评估',
        '1': '已评估',
        '2': '已确认'
      }
      return statusMap[status]
    },
    methodFilter(status) {
      const statusMap = {
        '1': '成本法',
        '2': '收益法',
        '3': '综合法',
        '4': '市场法'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      searchWorkOrder().then(response => {
        this.list = response.data.data.slice(0, 6)
      })
    }
  }
}
</script>
