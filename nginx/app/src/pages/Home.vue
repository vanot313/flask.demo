<template>
  <div>
    <transition name="fade">
      <loading v-if="isLoading"></loading>
    </transition>
    <div class="home">
      <Swiper/>
    </div>
    <el-row :gutter="20" class="mgb20">
      <el-col :span="18" >
        <el-card>
          <div class="grid-content">
            <div class="grid-cont-center">
              <div><i class="el-icon-document-copy"></i></div>
              <br>
              <div style="font-size: 20px">批量企业分类</div>
              <div style="text-align: center">
                批量上传企业信息，其中包含每个企业的ID以及是否可能成为僵尸企业的结果
              </div>
              <br>

              <el-upload
                action="http://49.235.73.129/uploader/uploadmultiple"
                :before-upload="beforeDocumentUpload"
                :on-success="handleDocumentsSuccess"
                multiple
                :auto-upload="false"
                ref="uploadFiles"
                :file-list="fileList"
                accept=".csv"
                :limit="5">
                <el-button size="mini" type="primary" slot="trigger">
                  <i class="el-icon-upload" style="font-size: 14px"></i>
                  上传文件
                </el-button>
                <el-button size="mini" type="success" @click="submitUpload">确定</el-button>
              </el-upload>
            </div>
          </div>
        </el-card>
        <el-card>
          <el-button  @click="goToDetail"  type="info" size="mini" >
              查看分析结果
          </el-button>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card>
<!--        <a href="./../static/1.jpg" download>xiazai</a>-->
          <el-button  @click="download1"  type="primary"size="mini" plain>
            下载企业年度信息总结表导入模板
          </el-button>
        </el-card>
        <el-card>
          <el-button  @click="download2"  type="primary" size="mini" plain>
            下载企业财务情况表导入模板
          </el-button>
        </el-card>
        <el-card>
          <el-button  @click="download3"  type="primary"size="mini" plain>
            下载企业知识产权信息表导入模板
          </el-button>
        </el-card>
        <el-card>
          <el-button  @click="download4"  type="primary"size="mini" plain>
            下载企业基本信息表导入模板
          </el-button>
        </el-card>

      </el-col>
    </el-row>
  </div>
</template>

<script>
  import Header from "../components/Header";
  import Aside from "../components/Aside";
  import Swiper from "../components/Swiper";
  import {mixin} from "../mixins";
  import {multipleClassify,download} from "../api";
  import {mapGetters} from 'vuex';
  import Loading from "../components/Loading";

  export default {
    mixins: [mixin],
    components: {
      Aside,
      Header,
      Swiper,
      Loading
    },
    computed: {
      ...mapGetters([
        'result',
      ])
    },
    data(){
      return {
        collapse: false,
        id: 1,
        res: [],
        fileList: [],
        fileNum: 0,
        isLoading:false,
      }
    },
    created(){

    },
    methods: {
      download1() {
        window.location.href="/static/year_report_test_sum.csv"
      },

      download2() {
        window.location.href="/static/money_report_test_sum.csv"
      },

      download3() {
        window.location.href="/static/knowledge_test_sum.csv"
      },

      download4() {
        window.location.href="/static/base_test_sum.csv"
      },

      //上传前进行校验
      beforeDocumentUpload(file){
        console.log('before upload');
        const isCSV = true;
        //const isCSV = (file.type === 'csv') || (file.type === 'csv');
        if(!isCSV){
          this.$message.error("只能上传csv格式的文件！");
          return false;
        }
        return true;
      },


      handleDocumentsSuccess(res){
          this.fileNum ++;
          console.log(this.fileNum);
           if(this.fileNum == 4){
            console.log('upload success');
            this.notify("上传成功","success");
            this.test();
         }
      },

      test(){
        this.isLoading = true ;
        multipleClassify()
        .then(res => {
          this.res = res;
          console.log(res);
          this.$store.commit('setResult',this.res);
          this.$router.push({path: `/multipleClassify`});
        })
      },

      goToDetail() {
        console.log(this.result);
        if(this.result.length == 0) {
          this.notify("您还没有上传文件","warning");
          console.log(1);
        }
        else this.$router.push({path: `/detail`});
      },

      submitUpload() {
        this.$refs.uploadFiles.submit();
      },
    },
  }
</script>

<style scoped>
  .grid-content {
    display: flex;
    align-items: center;/*垂直方向居中*/
    height: 200px;
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

  .el-icon-document {
    font-size: 70px;
    color: #87cefa;
  }

  .el-icon-document-copy {
    font-size: 70px;
    color: #87cefa;
  }
</style>
