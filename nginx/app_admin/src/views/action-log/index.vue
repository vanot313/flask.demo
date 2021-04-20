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
      style="width: 100%;"
    >
      <el-table-column label="ID" prop="id" sortable="custom" align="center" width="80" sortavle>
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作用户" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.username |adminFilter }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作内容" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.operation }}</span>
        </template>
      </el-table-column>
      <el-table-column label="耗时" width="100px" align="center">
        <template slot-scope="{row}">
          <el-tag type="info">
            <span>{{ row.time }}</span>
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作方法" width="150px" align="center">
        <template slot-scope="{row}">
          <el-tag type="info">
            <span>{{ row.method }}</span>
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作者IP" width="150px" align="center">
        <template slot-scope="{row}">
          <el-tag type="info">
            <span>{{ row.ip }}</span>
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="创建时间" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.create_time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="位置" width="150px" align="center">
        <template slot-scope="{row}">
          <el-tag type="info">
            <span>{{ row.location }}</span>
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="原操作者ID" width="120px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.from_id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="目标操作者ID" width="120px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.to_id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="工单ID" width="120px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.order_id |noneFilter }}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center" min-width="200" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">
            编辑
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.per_page" @pagination="getList" />
  </div>
</template>

<script>
import { searchLog } from '@/api/admin'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination

export default {
  name: 'ComplexTable',
  filters: {
    adminFilter: function(value) {
      if (!value || value === 'None') return 'admin'
      return value
    },
    noneFilter: function(value) {
      if (!value || value === 'None') return '暂无'
      return value
    }
  },
  components: {
    Pagination
  },
  directives: { waves },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        per_page: 20,
        from_id: '',
        to_id: '',
        order_id: ''
      },
      temp: {
        id: undefined,
        username: '',
        operation: '',
        time: '',
        method: '',
        params: '',
        ip: '',
        create_time: '',
        location: '',
        from_id: '',
        to_id: '',
        order_id: ''
      },
      editFormVisible: false,
      rules: {}
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      searchLog(this.listQuery).then(response => {
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
        id: undefined,
        username: '',
        operation: '',
        time: '',
        method: '',
        params: '',
        ip: '',
        create_time: '',
        location: '',
        from_id: '',
        to_id: '',
        order_id: ''
      }
    }
  }
}
</script>
