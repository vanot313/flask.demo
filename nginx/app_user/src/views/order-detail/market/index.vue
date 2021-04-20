<template>
  <div>
    <el-row>
      <el-col :span="12">
        <div class="col-lg-10" style="padding: 40px 30px 20px 30px">
          <div class="card m-b-30 text-white card-primary">
            <div class="card-body">
              <blockquote class="card-bodyquote">
                <h4>资产评估建议：￥{{ detail.suggestion }}</h4>
              </blockquote>
            </div>
          </div>
        </div>
      </el-col>

      <el-col :span="12">
        <radar :detail="detail" />
      </el-col>
    </el-row>

    <el-row>
      <bar :detail="detail" />
    </el-row>
  </div>
</template>

<script>
import Radar from './Radar'
import Bar from './Bar'

export default {
  components: {
    Radar,
    Bar
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
