<template>
  <div>
    <!--gutter：间距-->
    <el-row :gutter="20" class="mgb20">
      <!--共24，故可分2列-->
      <el-col :span="24">
        <h3 class="mgb20">分析结果：</h3>
        <div style="background-color: white">
          <!--ve-pie：饼图-->
          <ve-pie :data="companyType" :theme="options1" ></ve-pie>
        </div>
      </el-col>

    </el-row>
    <div align="center">
      <el-button @click="gotoDetail" type="primary">查看详情</el-button>
    </div>

  </div>
</template>

<script>
  import {mapGetters} from 'vuex';
  import Loading from "../components/Loading";

  export default {
    components:{
      Loading
    },
    mounted() {
      this.loadPageData();
    },
    computed: {
      ...mapGetters([
        'result',
      ])
    },
    data(){
      return{
        companyCount: 0,
        company: [],
        res: [],
        companyType: {  //按性别分类,colums与rows对应
          columns: ['类型','总数'],
          rows: [
            {'类型': '僵尸企业','总数': 0},
            {'类型': '非僵尸企业','总数': 0}
          ]
        },
        options1: {
          color: ['#ffc0cb','#87cefa']
        },
        isLoading: true,
      }
    },
    created() {
      this.res = this.result;
      this.getCompany();
    },
    methods: {
      //统计数量
      getCompany(){
        this.companyCount = this.res.length;
        this.companyType.rows[0]['总数'] = this.setCompanyType(true,this.res['data']);
        this.companyType.rows[1]['总数'] = this.setCompanyType(false,this.res['data']);
      },
      setCompanyType(type,company){
        let count = 0;
        for(let item of company){
          if(type == item.flag){
            count++;
          }
        }
        return count;
      },
      //跳转到详情页面
      gotoDetail(){
        let res = this.res;
        this.$router.push({path: `/detail`,query:{res}});
      },

      loadPageData: function() {
        // axios 请求页面数据 .then 中将状态值修改
        this.isLoading = false
      },
    }
  }
</script>

<style scoped>
  .grid-content {
    display: flex;
    align-items: center;/*垂直方向居中*/
    height: 50px;
  }

  .grid-cont-center {
    flex: 1;
    text-align: center;/*水平方向居中*/
    font-size: 14px;
    color: #a9a9a9;
  }

  .grid-num {
    font-size: 30px;
    font-weight: bold;
  }
</style>
