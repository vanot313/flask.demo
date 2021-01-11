<template>
  <div>
    <AnalysisHeader/>
    <AnalysisAside/>
    <div style="margin-left: 200px;margin-top: 110px;box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);border-radius: 4px">
      <p>基本信息概览</p>
      <div class="info">
        <el-row>
          <el-col :span="12">
              <i class="el-icon-s-custom"></i>
              <span style="font-size: 20px"> 企业ID：{{data.id}}</span>
          </el-col>
          <el-col :span="12">
            <i class="el-icon-coin"></i>
            <span style="font-size: 20px"> 注册资本：{{data.regMoney}}</span>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="12">
            <i class="el-icon-postcard"></i>
            <span style="font-size: 20px"> 分类结果：{{data.id}}</span>
          </el-col>
          <el-col :span="12">
            <i class="el-icon-menu"></i>
            <span style="font-size: 20px"> 行业：{{data.industry}}</span>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="12">
            <i class="el-icon-time"></i>
            <span style="font-size: 20px"> 注册时间：{{data.regTime}}</span>
          </el-col>
          <el-col :span="12">
            <i class="el-icon-help"></i>
            <span style="font-size: 20px"> 企业类型：{{data.comType}}</span>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="12">
            <i class="el-icon-user-solid"></i>
            <span style="font-size: 20px"> 控制人类型：{{data.personType}}</span>
          </el-col>
          <el-col :span="12">
            <i class="el-icon-s-marketing"></i>
            <span style="font-size: 20px"> 企业经营状况：</span>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="12">
            <i class="el-icon-s-data"></i>
            <span style="font-size: 20px"> 控制人持股比例：{{rate["rows"][0].percent}}</span>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="12">
            <ve-liquidfill :data="rate"></ve-liquidfill>
          </el-col>
          <el-col :span="12">
            <ve-radar :data="manage" :extend="chartExtends"></ve-radar>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
    import AnalysisHeader from "../components/AnalysisHeader";
    import AnalysisAside from "../components/AnalysisAside";

    export default {
        name: "Analysis",
        components: {
          AnalysisHeader,
          AnalysisAside,
        },
        data() {
          return {
            data: {
              'id': 1,
              'regMoney': 1000,
              'industry': '农业',
              'personType': '企业法人',
              'regTime': '2007',
              'comType': '农民合作社',

            },
            //持股比例
            rate: {
              columns: ['title','percent'],
              rows: [
                {title: '持股比例', percent: 0.56}
              ]
            },
            //经营状况
            manage: {
              columns: ['title','经营风险','政府依赖','资金周转','资产负债率'],
              rows: [
                {title:'经营状况','经营风险':-0.5,'政府依赖': -0.25,'资金周转': 3.7,'资产负债率': 1.7},

              ]
            },

            chartExtends: {
              radar: {
                indicator:[
                  {name: '经营风险', max: 0},
                  {name: '政府依赖', max: 0},
                  {name: '资金周转', max: 20},
                  {name: '资产负债率', max: 20},
                ],
              }
            }
          };
        },
      created() {
          this.data = this.$route.query.res['data'][0];
          this.rate.rows[0]['percent'] = this.data.rate;
          this.manage.rows[0]['经营风险'] = this.data.fengxian;
          this.manage.rows[0]['政府依赖'] = this.data.yilai;
          this.manage.rows[0]['资金周转'] = this.data.zhouzhuan;
          this.manage.rows[0]['资产负债率'] = this.data.fuzhai;
      }
    }
</script>

<style scoped>
  .info{
    font-size: 25px;
  }
</style>
