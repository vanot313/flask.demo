<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.id" placeholder="ID" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />

      <el-button v-waves class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-search" @click="handleFilter">
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
      style="width: 100%;"
    >
      <el-table-column label="ID" prop="id" width="80" align="center" sortable>
        <template slot-scope="{row}">
          <span>{{ row.order_id }}</span>
        </template>
      </el-table-column>

      <el-table-column label="用户ID" prop="id" width="100" align="center" sortable>
        <template slot-scope="{row}">
          <span>{{ row.user_id }}</span>
        </template>
      </el-table-column>

      <el-table-column label="评估方法" width="120px" align="center">
        <template slot-scope="{row}">
          <el-tag :color="row.method | methodFilter2" effect="dark">
            {{ row.method | methodFilter1 }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column label="创建时间" width="180px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.create_time }}</span>
        </template>
      </el-table-column>

      <el-table-column label="修改时间" width="180px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.modify_time }}</span>
        </template>
      </el-table-column>

      <el-table-column label="状态" width="100px" align="center">
        <template slot-scope="{row}">
          <el-tag :type="row.status | statusFilter1">
            {{ row.status |statusFilter2 }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column label="用户备注" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.u_remarks }}</span>
        </template>
      </el-table-column>

      <el-table-column label="专家备注" width="160px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.e_remarks }}</span>
        </template>
      </el-table-column>

      <el-table-column label="评估价值" width="140px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.result }}</span>
        </template>
      </el-table-column>

      <el-table-column label="文件名" width="220" align="center">
        <template slot-scope="{row}">
          <span>{{ row.file_name }}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center" min-width="100" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button v-if="row.status !== '0'" type="primary" size="mini" @click="detail(row.order_id,row.method)">
            查看
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.per_page" @pagination="getList" />
  </div>
</template>

<script>
import { getAllSelfWorkOrder, searchDetailWorkOrder } from '@/api/expert'
import waves from '@/directive/waves' // waves directive
// import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination

export default {
  name: 'ComplexTable',
  components: {
    Pagination
  },
  directives: { waves },
  filters: {
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
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      getAllSelfWorkOrder(this.listQuery).then(response => {
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
    detail(order_id, method) {
      // 如果使用params，则要用name并在router中配置name
      this.$router.push({ path: '/order/detail', query: { order_id, method }})
    }
  }
}
</script>

<style lang="scss" scoped>
  .el-tag {
    border: 0;
  }
</style>
