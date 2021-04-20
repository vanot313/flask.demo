<template>
  <div>
    <cost v-if="$route.query.method === '1' && detail" :detail="detail" />
    <earning v-else-if="$route.query.method === '2' && detail" :detail="detail" />
    <comprehensive v-else-if="$route.query.method === '3' && detail" :detail="detail" />
    <market v-else-if="$route.query.method === '4' && detail" :detail="detail " />
  </div>
</template>

<script>
import Cost from './cost/index'
import Earning from './earning/index'
import Comprehensive from './comprehensive/index'
import Market from './market/index'
import { searchDetailWorkOrder } from '@/api/expert'

export default {
  components: {
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
      searchDetailWorkOrder(this.$route.query.order_id).then(response => {
        this.base = response.data.base
        this.detail = response.data.detail
      })
    }
  }
}
</script>
