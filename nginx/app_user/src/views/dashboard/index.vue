<template>
  <div class="fonik">
    <layout />

    <div class="wrapper">
      <div class="container-fluid">

        <div class="row">
          <div class="col-md-6 col-xl-3">
            <div class="card text-center m-b-30">
              <div class="mb-2 card-body text-muted">
                <h3 class="text-info">20</h3>
                消息
              </div>
            </div>
          </div>

          <div class="col-md-6 col-xl-3">
            <div class="card text-center m-b-30">
              <div class="mb-2 card-body text-muted">
                <h3 class="text-purple">142</h3>
                已评估
              </div>
            </div>
          </div>

          <div class="col-md-6 col-xl-3">
            <div class="card text-center m-b-30">
              <div class="mb-2 card-body text-muted">
                <h3 class="text-primary">12</h3>
                未评估
              </div>
            </div>
          </div>

          <div class="col-md-6 col-xl-3">
            <div class="card text-center m-b-30">
              <div class="mb-2 card-body text-muted">
                <h3 class="text-danger">5,220</h3>
                我的资产
              </div>
            </div>
          </div>
        </div>
        <!-- end row -->

        <div class="row">
          <div class="col-xl-4">
            <div class="card m-b-30">
              <div class="card-body">
                <h4 class="mt-0 header-title">工单统计</h4>

                <div class="row text-center m-t-20">
                  <div class="col-6">
                    <h5 class="">154</h5>
                    <p class="text-muted font-14">总数量</p>
                  </div>
                  <div class="col-6">
                    <h5 class="">4660</h5>
                    <p class="text-muted font-14">总价值</p>
                  </div>
                </div>

                <pie-chart />
              </div>
            </div>
          </div>

          <div class="col-xl-8">
            <div class="card m-b-30">
              <div class="card-body">
                <h4 class="mt-0 header-title">资产统计</h4>

                <div class="row text-center m-t-20">
                  <div class="col-4">
                    <h5 class="">1220</h5>
                    <p class="text-muted font-14">成本法</p>
                  </div>
                  <div class="col-4">
                    <h5 class="">2530</h5>
                    <p class="text-muted font-14">收益法</p>
                  </div>
                  <div class="col-4">
                    <h5 class="">2410</h5>
                    <p class="text-muted font-14">市场法</p>
                  </div>
                </div>

                <area-stack-gradient />
              </div>
            </div>
          </div>

        </div>
        <!-- end row -->

        <div class="row">
          <div class="col-xl-8">
            <div class="card m-b-30">
              <div class="card-body">
                <h4 class="mt-0 m-b-30 header-title">最近工单</h4>

                <div class="table-responsive">
                  <table class="table m-t-15 mb-0 table-vertical">
                    <tbody>
                      <tr v-for="item in orderList" :key="item.order_id">
                        <td>
                          工单编号：{{ item.order_id }}
                        </td>
                        <td><i class="mdi mdi-checkbox-blank-circle" :class="item.status | statusFilter1" />{{ item.status | statusFilter2 }}</td>
                        <td>
                          {{ item.method | prefixFilter }}{{ item.result | noneFilter }}
                          <p class="m-0 text-muted font-14">Result</p>
                        </td>
                        <td>
                          {{ item.modify_time }}
                          <p class="m-0 text-muted font-14">Modify Time</p>
                        </td>
                        <td>
                          <button type="button" class="btn btn-secondary btn-sm waves-effect">查看</button>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>

          <div class="col-xl-4">
            <div class="card m-b-30">
              <div class="card-body">
                <h4 class="mt-0 m-b-15 header-title">时间线</h4>

                <ol class="activity-feed mb-0">
                  <li v-for="item in logList" :key="item.id" class="feed-item">
                    <span class="date">{{ item.create_time }}</span>
                    <span class="activity-text">{{ item.operation }}</span>
                  </li>
                </ol>
              </div>
            </div>
          </div>

        </div>
        <!-- end row -->
      </div>
      <!-- end container -->
    </div>
    <!-- end wrapper -->

    <Footer />
  </div>
</template>

<script>
import Layout from '@/components/Layout/index'
import Footer from '@/components/Footer/index'
import PieChart from './components/PieChart'
import AreaStackGradient from './components/AreaStackGradient'
import { get_work_order, get_log } from '@/api/user'

export default {
  components: {
    Layout,
    Footer,
    PieChart,
    AreaStackGradient
  },
  filters: {
    statusFilter1(status) {
      const statusMap = {
        '0': 'text-danger',
        '1': 'text-warning',
        '2': 'text-success'
      }
      return statusMap[status]
    },
    statusFilter2(status) {
      const statusMap = {
        '0': '未评估',
        '1': '待确认',
        '2': '已确认'
      }
      return statusMap[status]
    },
    noneFilter: function(value) {
      if (!value || value === 'None') return ''
      return value
    },
    prefixFilter: function(value) {
      if (value === '3') return '评分：'
      return '价值：'
    }
  },
  data() {
    return {
      title: '首页',
      orderList: null,
      logList: null
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      get_work_order().then(response => {
        this.orderList = response.data.data.slice(0, 4)
      })
      get_log().then(response => {
        this.logList = response.data.data.slice(0, 5)
      })
    }
  }
}
</script>
