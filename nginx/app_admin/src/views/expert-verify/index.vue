<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.apply_id" placeholder="ID" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.username" placeholder="用户名" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.email" placeholder="邮箱" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.location" placeholder="地区" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />

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
      <el-table-column label="申请ID" prop="id" width="100" align="center" sortable>
        <template slot-scope="{row}">
          <span>{{ row.apply_id }}</span>
        </template>
      </el-table-column>

      <el-table-column label="用户ID" prop="id" width="100" align="center" sortable>
        <template slot-scope="{row}">
          <span>{{ row.user_id }}</span>
        </template>
      </el-table-column>

      <el-table-column label="用户名" width="120px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.username }}</span>
        </template>
      </el-table-column>

      <el-table-column label="邮箱" width="170px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.email }}</span>
        </template>
      </el-table-column>

      <el-table-column label="联系方式" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.mobile }}</span>
        </template>
      </el-table-column>

      <el-table-column label="真实姓名" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.realname }}</span>
        </template>
      </el-table-column>

      <el-table-column label="职称" width="120px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.job_title }}</span>
        </template>
      </el-table-column>

      <el-table-column label="简介" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.introduction }}</span>
        </template>
      </el-table-column>

      <el-table-column label="创建时间" width="180px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.create_time }}</span>
        </template>
      </el-table-column>

      <el-table-column label="申请状态" width="180px" align="center">
        <template slot-scope="{row}">
          <el-tag :type="row.status | statusFilter1">
            {{ row.status |statusFilter2 }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center" min-width="230" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">
            查看
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.per_page" @pagination="getList" />

    <ApplyForm ref="applyForm" :temp="temp" :rules="rules" :apply-form-visible="applyFormVisible" />
  </div>
</template>

<script>
import { searchExpertApply, updateExpertApply } from '@/api/admin'
import waves from '@/directive/waves' // waves directive
import Pagination from '@/components/Pagination'
import ApplyForm from './ApplyForm'

export default {
  name: 'ComplexTable',
  components: {
    Pagination,
    ApplyForm
  },
  directives: { waves },
  filters: { statusFilter1(status) {
    const statusMap = {
      '0': 'info',
      '1': 'success',
      '2': 'danger'
    }
    return statusMap[status]
  },
  statusFilter2(status) {
    const statusMap = {
      '0': '未通过',
      '1': '已通过',
      '2': '已拒绝'
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
        per_page: 20
      },
      temp: {
        apply_id: '',
        user_id: '',
        username: '',
        email: '',
        mobile: '',
        description: '',
        realname: '',
        job_title: '',
        introduction: '',
        create_time: '',
        finish_time: '',
        status: ''
      },
      applyFormVisible: false,
      rules: {}
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      searchExpertApply(this.listQuery).then(response => {
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
        apply_id: '',
        user_id: '',
        username: '',
        email: '',
        description: '',
        realname: '',
        job_title: '',
        introduction: '',
        create_time: '',
        finish_time: '',
        status: ''
      }
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.applyFormVisible = true
      this.$nextTick(() => {
        this.$refs['applyForm'].$refs['form'].clearValidate()
      })
    },
    updateData() {
      this.$refs['applyForm'].$refs['form'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          updateExpertApply(tempData).then(() => {
            const index = this.list.findIndex(v => v.id === this.temp.id)
            this.list.splice(index, 1, this.temp)
            this.applyFormVisible = false
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
      this.applyFormVisible = false
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
