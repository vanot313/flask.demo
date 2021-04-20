<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.id" placeholder="ID" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.username" placeholder="用户名" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.email" placeholder="邮箱" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.location" placeholder="地区" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />

      <el-button v-waves class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-search" @click="handleFilter">
        搜索
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        添加用户
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
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>

      <el-table-column label="用户名" width="120px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.username |noneFilter }}</span>
        </template>
      </el-table-column>

      <el-table-column label="邮箱" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.email |noneFilter }}</span>
        </template>
      </el-table-column>

      <el-table-column label="联系方式" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.mobile |noneFilter }}</span>
        </template>
      </el-table-column>

      <el-table-column label="地址" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.location |noneFilter }}</span>
        </template>
      </el-table-column>

      <el-table-column label="生日" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.birth }}</span>
        </template>
      </el-table-column>

      <el-table-column label="简介" width="200px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.description |noneFilter2 }}</span>
        </template>
      </el-table-column>

      <el-table-column label="创建时间" width="180px" align="center" sortable>
        <template slot-scope="{row}">
          <span>{{ row.create_time }}</span>
        </template>
      </el-table-column>

      <el-table-column label="上次登录时间" width="180px" align="center" sortable>
        <template slot-scope="{row}">
          <span>{{ row.last_login_time }}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center" min-width="230" class-name="small-padding fixed-width">
        <template slot-scope="{row,$index}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">
            编辑
          </el-button>
          <el-button type="danger" size="mini" @click="handleFreeze(row,$index)">
            冻结
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.per_page" @pagination="getList" />

    <CreateForm ref="createForm" :temp="temp" :rules="rules" :create-form-visible="createFormVisible" />

    <EditForm ref="editForm" :temp="temp" :rules="rules" :edit-form-visible="editFormVisible" />
  </div>
</template>

<script>
import { searchUserInfo, updateUserInfo, register } from '@/api/admin'
import waves from '@/directive/waves' // waves directive
// import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import CreateForm from './CreateForm'
import EditForm from './EditForm'

export default {
  name: 'ComplexTable',
  components: {
    Pagination,
    CreateForm,
    EditForm
  },
  directives: { waves },
  filters: {
    noneFilter: function(value) {
      if (!value || value === 'None') return '暂无'
      return value
    },
    noneFilter2: function(value) {
      if (!value || value === 'None') return ''
      return value
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
    handleCreate() {
      this.resetTemp()
      this.createFormVisible = true
      this.$nextTick(() => {
        this.$refs['createForm'].$refs['form'].clearValidate()
      })
    },
    addUser() {
      this.$refs['createForm'].$refs['form'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          register(tempData).then(() => {
            this.listQuery.page = 1
            this.getList()

            this.createFormVisible = false
            this.$notify({
              title: 'Success',
              message: '添加成功',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    closeCreateDialog() {
      this.createFormVisible = false
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      if (row.birth === 'None') {
        this.temp.birth = null
      }
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
              message: '修改成功',
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
