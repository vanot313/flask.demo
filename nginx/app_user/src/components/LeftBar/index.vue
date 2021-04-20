<template>
  <!-- Left sidebar -->
  <div class="email-leftbar mb-3">
    <router-link to="/order/new" class="btn btn-danger btn-rounded btn-custom btn-block waves-effect waves-light">新的评估</router-link>

    <div class="mail-list m-t-20">
      <router-link to="/order/list" class="active">全部工单</router-link>
      <a href="#">已确认</a>
      <a href="#">待确认</a>
      <a href="#">待评估</a>
    </div>

    <h6 class="m-t-30">标签</h6>

    <div class="mail-list m-t-20">
      <a href="#"><span class="mdi mdi-arrow-right-drop-circle text-info float-right mt-1" />成本法</a>
      <a href="#"><span class="mdi mdi-arrow-right-drop-circle text-warning float-right mt-1" />收益法</a>
      <a href="#"><span class="mdi mdi-arrow-right-drop-circle text-purple float-right mt-1" />综合估值法</a>
      <a href="#"><span class="mdi mdi-arrow-right-drop-circle text-pink float-right mt-1" />市场法</a>
    </div>
  </div>
  <!-- End Left sidebar -->
</template>
