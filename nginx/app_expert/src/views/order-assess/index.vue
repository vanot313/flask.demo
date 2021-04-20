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
      style="width: 75%;"
    >
      <el-table-column label="ID" prop="id" width="80" align="center" sortable>
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

      <el-table-column label="状态" width="100px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.status | statusFilter }}</span>
        </template>
      </el-table-column>

      <el-table-column label="用户备注" width="350px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.u_remarks }}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center" min-width="200" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="downloadFile(row.order_id,row.file_name)">
            文件下载
          </el-button>
          <el-button type="primary" size="mini" @click="handleAssess(row)">
            评估
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.per_page" @pagination="getList" />

    <ComprehensiveForm ref="comprehensiveForm" :temp="comprehensive" :comprehensive-form-visible="comprehensiveFormVisible" />

    <CostForm ref="costForm" :temp="cost" :cost-form-visible="costFormVisible" />

    <EarningForm ref="earningForm" :temp="earning" :earning-form-visible="earningFormVisible" />
  </div>
</template>

<script>
import { getAllWaitWorkOrder, downloadOrderFile, processComprehensive, processCost, processEarning } from '@/api/expert'
import waves from '@/directive/waves' // waves directive
// import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import ComprehensiveForm from './ComprehensiveForm'
import CostForm from './CostForm'
import EarningForm from './EarningForm'

export default {
  name: 'ComplexTable',
  components: {
    Pagination,
    CostForm,
    EarningForm,
    ComprehensiveForm
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
    statusFilter(status) {
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
      },
      comprehensive: {
        order_id: '',
        rareness: '',
        timeliness: '',
        dimensional: '',
        economy: '',
        quality_weight: [],
        applied_weight: []
      },
      cost: {
        order_id: '',
        R: '',
        C: '',
        II: '',
        M: '',
        E: ''
      },
      earning: {
        order_id: '',
        n: '',
        r: '',
        RI: []
      },
      comprehensiveFormVisible: false,
      costFormVisible: false,
      earningFormVisible: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      getAllWaitWorkOrder(this.listQuery).then(response => {
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
    resetComprehensive() {
      this.comprehensive = {
        order_id: '',
        rareness: '',
        timeliness: '',
        dimensional: '',
        economy: '',
        quality_weight: [],
        applied_weight: []
      }
    },
    resetCost() {
      this.cost = {
        order_id: '',
        R: '',
        C: '',
        II: '',
        M: '',
        E: ''
      }
    },
    resetEarning() {
      this.earning = {
        order_id: '',
        n: '',
        r: '',
        RI: []
      }
    },
    handleAssess(row) {
      if (row.method === '1') {
        this.resetCost()
        this.cost.order_id = row.order_id
        this.costFormVisible = true
        this.$nextTick(() => {
          this.$refs['costForm'].$refs['form'].clearValidate()
        })
      }
      if (row.method === '2') {
        this.resetEarning()
        this.earning.order_id = row.order_id
        this.earningFormVisible = true
        this.$nextTick(() => {
          this.$refs['earningForm'].$refs['form'].clearValidate()
        })
      }
      if (row.method === '3') {
        this.resetComprehensive()
        this.comprehensive.order_id = row.order_id
        this.comprehensiveFormVisible = true
        this.$nextTick(() => {
          this.$refs['comprehensiveForm'].$refs['form'].clearValidate()
        })
      }
    },
    assessCost() {
      this.$refs['costForm'].$refs['form'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.cost)
          processCost(tempData).then(() => {
            this.listQuery.page = 1
            this.getList()

            this.costFormVisible = false
            this.$notify({
              title: 'Success',
              message: '评估成功',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    assessComprehensive() {
      this.$refs['comprehensiveForm'].$refs['form'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.comprehensive)
          processComprehensive(tempData).then(() => {
            this.listQuery.page = 1
            this.getList()

            this.comprehensiveFormVisible = false
            this.$notify({
              title: 'Success',
              message: '评估成功',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    assessEarning() {
      this.$refs['earningForm'].$refs['form'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.earning)
          processEarning(tempData).then(() => {
            this.listQuery.page = 1
            this.getList()

            this.earningFormVisible = false
            this.$notify({
              title: 'Success',
              message: '评估成功',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    closeCostDialog() {
      this.costFormVisible = false
    },
    closeComprehensiveDialog() {
      this.comprehensiveFormVisible = false
    },
    closeEarningDialog() {
      this.earningFormVisible = false
    },
    downloadFile(order_id, filename) {
      // this.listLoading = true
      downloadOrderFile(order_id).then(response => {
        this.download(response, filename)
      }).catch(error => {
        console.log(error)
      })
    },
    download(data, filename) {
      if (!data) {
        return
      }
      const url = window.URL.createObjectURL(new Blob([data]))
      const link = document.createElement('a')
      link.style.display = 'none'
      link.href = url
      link.setAttribute('download', filename)

      document.body.appendChild(link)
      link.click()
    }
  }
}
</script>

<style lang="scss" scoped>
  .el-tag {
    border: 0;
  }
</style>
