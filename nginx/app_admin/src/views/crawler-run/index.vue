<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.id" placeholder="ID" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.username" placeholder="用户名" style="width: 150px;" class="filter-item" @keyup.enter.native="handleFilter" />

      <el-button v-waves class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-search" @click="handleFilter">
        搜索
      </el-button>
    </div>

    <el-row>
      <el-col :span="12">
        <el-table
          :key="tableKey"
          v-loading="listLoading"
          :data="testList"
          fit
          highlight-current-row
          style="width: 95%;"
        >
          <el-table-column
            type="selection"
            style="width: 8px;"
          />

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

          <el-table-column label="爬虫信息" width="200px" align="center">
            <template slot-scope="{row}">
              <span>{{ row.email |noneFilter }}</span>
            </template>
          </el-table-column>

          <el-table-column label="状态" width="150px" align="center">
            <template slot-scope="{row}">
              <el-tag :type="row.finished_num | statusFilter1">
                {{ row.finished_num |statusFilter2 }}
              </el-tag>
            </template>
          </el-table-column>

          <el-table-column label="备注" min-width="150px" align="center">
            <template slot-scope="{row}">
              <span>{{ row.description |noneFilter }}</span>
            </template>
          </el-table-column>
        </el-table>
      </el-col>

      <el-col :span="2">
        <el-divider direction="vertical" />
      </el-col>

      <el-col :span="8">
        <el-form ref="form" label-width="80px" style="border:black;">
          <el-form-item label="爬虫名称">
            <el-input />
          </el-form-item>

          <el-form-item label="备注">
            <el-input type="textarea" />
          </el-form-item>

          <el-upload
            class="upload-demo"
            drag
            action=""
            multiple
            :auto-upload="false"
            style="margin-left: 80px"
          >
            <i class="el-icon-upload" />
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          </el-upload>
          <el-form-item style="margin-top: 20px">
            <el-button type="primary">立即创建</el-button>
            <el-button>重置</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>

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
        '2': 'primary'
      }
      return statusMap[status]
    },
    statusFilter2(status) {
      const statusMap = {
        '0': '未开始',
        '1': '已完成',
        '2': '运行中'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      tableKey: 0,
      list: null,
      testList: [
        {
          id: 1,
          username: '京东万象爬取器',
          email: '',
          finished_num: '2',
          description: ''
        },
        {
          id: 2,
          username: '淘宝数据爬取器',
          email: '',
          finished_num: '1',
          description: ''
        }
      ],
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
    }
  }
}
</script>
<style scoped>
.el-divider--vertical{
  display: inline-block;
  width: 1px;
  height: 55em;
  margin: 0 0 0 60px;
  vertical-align: middle;
  position: relative;
}
</style>
