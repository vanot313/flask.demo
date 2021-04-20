<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.id" placeholder="ID" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.name" placeholder="爬虫名称" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />

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
      style="width: 96%;"
    >
      <el-table-column label="ID" prop="id" width="80" align="center" sortable>
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>

      <el-table-column label="爬虫名称" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.username }}</span>
        </template>
      </el-table-column>

      <el-table-column label="创建时间" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.create_time }}</span>
        </template>
      </el-table-column>

      <el-table-column label="结束时间" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.last_login_time }}</span>
        </template>
      </el-table-column>

      <el-table-column label="描述" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.description |noneFilter }}</span>
        </template>
      </el-table-column>

      <el-table-column label="数据量" width="180px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.msg_num }}</span>
        </template>
      </el-table-column>

      <el-table-column label="数据大小" width="180px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.data_assets }}</span>
        </template>
      </el-table-column>

      <el-table-column label="状态" width="150px" align="center">
        <template slot-scope="{row}">
          <el-tag :type="row.finished_num | statusFilter1">
            {{ row.finished_num |statusFilter2 }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center" min-width="230" class-name="small-padding fixed-width">
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
import { searchUserInfo, updateUserInfo, register } from '@/api/admin'
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
        '0': '未开始',
        '1': '已完成',
        '2': '进行中'
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
        id: '',
        username: '',
        email: '',
        location: ''
      },
      temp: {
        id: undefined,
        username: '',
        password: '',
        email: '',
        mobile: '',
        location: '',
        birth: undefined,
        description: ''
      },
      createFormVisible: false,
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
      searchUserInfo(this.listQuery).then(response => {
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
        password: '',
        email: '',
        mobile: '',
        location: '',
        birth: undefined,
        description: ''
      }
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.editFormVisible = true
      this.$nextTick(() => {
        this.$refs['editForm'].$refs['form'].clearValidate()
      })
    },
    updateData() {
      this.$refs['editForm'].$refs['form'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          updateUserInfo(tempData).then(() => {
            const index = this.list.findIndex(v => v.id === this.temp.id)
            this.list.splice(index, 1, this.temp)
            this.editFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Update Successfully',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    closeEditDialog() {
      this.editFormVisible = false
    },
    handleFreeze(row, index) {
      this.$notify({
        title: 'Success',
        message: 'Freeze Successfully',
        type: 'success',
        duration: 2000
      })
    }
  }
}
</script>
