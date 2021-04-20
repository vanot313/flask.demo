<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item
        v-for="(item,index) of timeline"
        :key="index"
        :timestamp="item.timestamp"
        placement="top"
      >
        <el-card>
          <h4>{{ item.title }}</h4>
          <p>{{ item.content }}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
export default {
  data() {
    return {
      timeline: [
        {
          timestamp: '2021-03-11',
          title: '更新管理员页面',
          content: ''
        },
        {
          timestamp: '2021-03-10',
          title: '修复部分bug',
          content: '修复切换账号后内容依旧停留在上一账号的问题'
        }
      ]
    }
  }
}
</script>
