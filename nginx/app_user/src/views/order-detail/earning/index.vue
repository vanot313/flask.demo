<template>
  <div>
    <div class="row" style="padding: 50px 40px 20px 40px">
      <div class="col-lg-4">
        <div class="card m-b-30 text-white card-primary">
          <div class="card-body">
            <blockquote class="card-bodyquote">
              <h4>评估价值：￥{{ detail.P }}</h4>
            </blockquote>
          </div>
        </div>
      </div>

      <div class="col-lg-4">
        <div class="card m-b-30 text-white card-success">
          <div class="card-body">
            <blockquote class="card-bodyquote">
              <h4>预期收益持续年限：{{ parseInt(detail.n) }}年</h4>
            </blockquote>
          </div>
        </div>
      </div>

      <div class="col-lg-4">
        <div class="card m-b-30 text-white card-info">
          <div class="card-body">
            <blockquote class="card-bodyquote">
              <h4>折现率：{{ detail.r * 100 }}%</h4>
            </blockquote>
          </div>
        </div>
      </div>
    </div>
    <!-- end row -->
    <LineSmooth :detail="detail" />
  </div>
</template>

<script>
import LineSmooth from './Line'

export default {
  components: {
    LineSmooth
  },
  props: {
    detail: {
      type: Object,
      default: () => {}
    }
  }
}
</script>

<style scoped>
h4 {
  text-align: center;
  font-family: 黑体,serif;
  font-weight: bold;
}
</style>
