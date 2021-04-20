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
              <div class="card m-t-20">
                <cost v-if="$route.query.method === '1' && detail" :detail="detail" />
                <earning v-else-if="$route.query.method === '2' && detail" :detail="detail" />
                <comprehensive v-else-if="$route.query.method === '3' && detail" :detail="detail" />
                <market v-else-if="$route.query.method === '4' && detail" :detail="detail " />
              </div>
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
import Cost from './cost/index'
import Earning from './earning/index'
import Comprehensive from './comprehensive/index'
import Market from './market/index'
import { detail_work_order } from '@/api/user'

export default {
  components: {
    Layout,
    LeftBar,
    Cost,
    Earning,
    Comprehensive,
    Market
  },
  data() {
    return {
      title: '工单详情',
      base: undefined,
      detail: undefined
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      detail_work_order(this.$route.query.order_id).then(response => {
        this.base = response.data.base
        this.detail = response.data.detail
      })
    }
  }
}
</script>
