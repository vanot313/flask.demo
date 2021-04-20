<template>
  <div class="fonik">
    <layout :title="title" />

    <div class="wrapper">
      <div class="container-fluid">

        <div class="row">
          <div class="col-12">
            <left-bar />

            <!-- Right Sidebar -->
            <div class="email-rightbar mb-3">
              <right-bar />
              <div class="card m-t-20">
                <el-table
                  :key="tableKey"
                  :data="list"
                  fit
                  highlight-current-row
                  style="padding: 10px 20px 0 20px;"
                >
                  <el-table-column label="工单编号" width="80" align="center">
                    <template slot-scope="{row}">
                      <span>{{ row.order_id }}</span>
                    </template>
                  </el-table-column>

                  <el-table-column label="评估方法" width="120px" align="center">
                    <template slot-scope="{row}">
                      <el-tag :color="row.method | methodFilter2" effect="dark">
                        {{ row.method | methodFilter1 }}
                      </el-tag>
                    </template>
                  </el-table-column>

                  <el-table-column label="修改时间" width="150" align="center">
                    <template slot-scope="{row}">
                      <span>{{ row.modify_time }}</span>
                    </template>
                  </el-table-column>

                  <el-table-column label="用户备注" width="200" align="center">
                    <template slot-scope="{row}">
                      <span>{{ row.u_remarks | noneFilter }}</span>
                    </template>
                  </el-table-column>

                  <el-table-column label="文件" width="250" align="center">
                    <template slot-scope="{row}">
                      <span>{{ row.file_name | noneFilter }}</span>
                    </template>
                  </el-table-column>

                  <el-table-column label="操作" align="center" min-width="80" class-name="small-padding fixed-width">
                    <template slot-scope="{row}">
                      <el-button v-if="row.status !== '0'" type="primary" size="mini" @click="detail(row.order_id,row.method)">
                        查看
                      </el-button>
                      <el-button v-else type="danger" size="mini">
                        待评估
                      </el-button>
                    </template>
                  </el-table-column>
                </el-table>

                <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.per_page" @pagination="getList" />
              </div>
              <!-- panel -->
            </div>
            <!-- end Col-9 -->
          </div>
        </div>
        <!-- End row -->
      </div>
      <!-- end container -->
    </div>
    <!-- end wrapper -->
  </div>
</template>

<script>
import Layout from '@/components/Layout/index'
import LeftBar from '@/components/LeftBar/index'
import RightBar from '@/components/RightBar/index'
import Pagination from '@/components/Pagination'
import { get_work_order } from '@/api/user'

export default {
  components: {
    Layout,
    LeftBar,
    RightBar,
    Pagination
  },
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
    noneFilter: function(value) {
      if (!value || value === 'None') return ''
      return value
    }
  },
  data() {
    return {
      hit: false,
      title: '资产评估',
      tableKey: 0,
      list: null,
      total: 0,
      listQuery: {
        page: 1,
        per_page: 10,
        order_id: ''
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      get_work_order(this.listQuery).then(response => {
        this.list = response.data.data
        this.total = response.data.total
      })
    },
    detail(order_id, method) {
      // 如果使用params，则要用name并在router中配置name
      this.$router.push({ path: '/order/detail', query: { order_id, method }})
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~@/styles/element-variables.scss";

.pagination-container {
  margin-top: 15px;
}

.el-tag {
  border: 0;
}
</style>
