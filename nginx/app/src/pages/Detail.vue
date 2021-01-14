<template>
  <div>
    <Header/>
    <Aside/>

    <el-table size="mini"
              ref="multipleTable"
              border style="width: 100%;margin-top: 70px;margin-left: 180px" height="680px"
              :data="data"
              :row-style="{height: '60px'}">
      <el-table-column label="企业id" align="center" width="300px" prop="id">

      </el-table-column>
      <el-table-column label="企业类型" width="500" align="center" prop="flag">
        <template slot-scope="scope">
          <div :style="{'color': scope.row.flag == true?'#3cc4ae':'#c63820'}">
            <div v-if="scope.row.flag == true">
              正常企业
            </div>
            <div v-else>
              僵尸企业
            </div>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="350" align="center">
        <template slot-scope="scope">
          <el-button size="mini" @click="gotoAnalysis(scope.row.id)">可视化分析</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="pagination" style="position: absolute;top: 700px;left: 600px">
      <el-pagination
        background
        layout="total,prev,pager,next"
        :current-page="currentPage"
        :page-size="pageSize"
        :total="res.length"
        @current-change="handleCurrentChange"/>
    </div>

  </div>
</template>

<script>
  import Aside from "../components/Aside";
  import Header from "../components/Header";
  import {analysis} from "../api";
  import {mapGetters} from 'vuex';

  export default {
    name: "Deatail",
    components: {
      Aside,
      Header,
    },
    data(){
      return{
        res: [
          {"id": 1500001, "flag":true},
          {"id": 1500002, "flag":false},
          {"id": 1500003, "flag":false},
          {"id": 1500004, "flag":false},
          {"id": 1500005, "flag":true},
          {"id": 1500006, "flag":true},
          {"id": 1500007, "flag":false},
          {"id": 1500008, "flag":false},
          {"id": 1500009, "flag":false},
          {"id": 1500010, "flag":false},
          {"id": 1500011, "flag":false},
          {"id": 1500012, "flag":false},
          {"id": 1500013, "flag":false},
          {"id": 1500014, "flag":false},
          {"id": 1500015, "flag":false},
        ],
        pageSize: 9,  //每页大小
        currentPage: 1,  //当前页
      }
    },
    created() {
      this.res = this.result['data'];
    },
    computed: {
      //计算当前搜索结果数据
      data(){
        return this.res.slice((this.currentPage - 1)* this.pageSize,this.currentPage * this.pageSize);
      },
      ...mapGetters([
        'result',
      ])
    },
    methods: {
      //获取当前页
      handleCurrentChange(val){
        this.currentPage = val;
      },
      //前往可视化分析
      gotoAnalysis(id){
        analysis(id)
        .then(res => {
          this.$router.push({path: `/analysis`,query:{res}});
        })
      },
    }
  }
</script>

<style scoped>

</style>
