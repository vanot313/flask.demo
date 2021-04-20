<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.username" placeholder="用户名" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />

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
      <el-table-column label="用户名" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.username }}</span>
        </template>
      </el-table-column>
      <el-table-column label="角色" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.rolename }}</span>
        </template>
      </el-table-column>
      <el-table-column label="登录时间" width="220px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.login_time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="地址" width="200px" align="center">
        <template slot-scope="{row}">
          <el-tag type="info">
            <span>{{ row.location }}</span>
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="IP" width="200px" align="center">
        <template slot-scope="{row}">
          <el-tag type="info">
            <span>{{ row.ip }}</span>
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="系统" width="200px" align="center">
        <template slot-scope="{row}">
          <el-tag type="info">
            <span>{{ row.login_system }}</span>
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="浏览器" width="200px" align="center">
        <template slot-scope="{row}">
          <el-tag type="info">
            <span>{{ row.browser }}</span>
          </el-tag>
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
import { searchLoginLog } from '@/api/admin'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination

export default {
  name: 'ComplexTable',
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
        username: ''
      },
      temp: {
        id: undefined,
        username: '',
        rolename: '',
        login_time: '',
        location: '',
        ip: '',
        login_system: '',
        browser: ''
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
      searchLoginLog(this.listQuery).then(response => {
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
        rolename: '',
        login_time: '',
        location: '',
        ip: '',
        login_system: '',
        browser: ''
      }
    }
  }
}
</script>
