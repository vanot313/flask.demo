<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.id" placeholder="ID" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />

      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        搜索
      </el-button>
    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 95%;"
    >
      <el-table-column label="ID" prop="id" align="center" width="80" sortable>
        <template slot-scope="{row}">
          <span>{{ row.order_id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="方法" width="150px" align="center">
        <template slot-scope="{row}">
          <el-tag :color="row.method | methodFilter2" effect="dark">
            {{ row.method | methodFilter1 }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="创建时间" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.create_time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="修改时间" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.modify_time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="状态" width="150px" align="center">
        <template slot-scope="{row}">
          <el-tag :type="row.status | statusFilter1">
            {{ row.status |statusFilter2 }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="用户备注" width="350px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.u_remarks }}</span>
        </template>
      </el-table-column>
      <el-table-column label="专家备注" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.e_remarks |noneFilter }}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center" min-width="230" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="(row)">
            编辑
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.per_page" @pagination="getList" />
  </div>
</template>

<script>
import { searchWorkOrder } from '@/api/admin'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination

export default {
  name: 'ComplexTable',
  components: { Pagination },
  directives: { waves },
  filters: {
    noneFilter: function(value) {
      if (!value || value === 'None') return '暂无'
      return value
    },
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
    methodFilter1(status) {
      const statusMap = {
        '1': '成本法',
        '2': '收益法',
        '3': '综合法',
        '4': '市场法'
      }
      return statusMap[status]
    },
    methodFilter2(status) {
      const statusMap = {
        '1': '#17a2b8',
        '2': '#ffc107',
        '3': '#8862e0',
        '4': '#e6487e'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        per_page: 20,
        order_id: ''

      },
      temp: {
        order_id: undefined,
        method: '',
        create_time: '',
        modify_time: '',
        status: '',
        u_remarks: '',
        e_remarks: ''
      },
      rules: {}
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      searchWorkOrder(this.listQuery).then(response => {
        this.list = response.data.data
        this.total = response.data.total

        // Just to simulate the time of the request
        setTimeout(() => {
          this.listLoading = false
        }, 0.5 * 1000)
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    resetTemp() {
      this.temp = {
        order_id: undefined,
        method: '',
        create_time: '',
        modify_time: '',
        status: '',
        u_remarks: '',
        e_remarks: ''
      }
    }
  }
}
</script>

<style lang="scss" scoped>
  .el-tag {
    border: 0;
  }
</style>
