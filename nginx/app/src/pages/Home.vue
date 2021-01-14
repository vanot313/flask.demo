<template>
  <div>
    <div class="home">
      <Swiper/>
    </div>
    <el-row :gutter="20" class="mgb20">
      <!--共24，故可分2列-->
      <!--<el-col :span="12">
        <el-card>
          <div class="grid-content">
            <div class="grid-cont-center">
              <div><i class="el-icon-document"></i></div>
              <br>
              <div style="font-size: 20px">单个企业分类</div>
              <div style="text-align: left">
                通过手动输入或csv文件上传单个企业信息，我们将给出企业是否可能成为僵尸企业的结果，并给出可视化分析报告
              </div>
              <el-upload
                action="http://49.235.73.129/uploader/upload"
                :before-upload="beforeDocumentUpload"
                :on-success="handleDocumentSuccess">
                <el-button size="mini" type="primary">
                  <i class="el-icon-upload" style="font-size: 14px"></i>
                  上传文件
                </el-button>
              </el-upload>
            </div>
          </div>
        </el-card>
      </el-col>-->

      <el-col :span="24" >
        <el-card>
          <div class="grid-content">
            <div class="grid-cont-center">
              <div><i class="el-icon-document-copy"></i></div>
              <br>
              <div style="font-size: 20px">批量企业分类</div>
              <div style="text-align: center">
                通过手动输入或csv文件批量上传企业信息，其中包含每个企业的ID以及是否可能成为僵尸企业的结果
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
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import Header from "../components/Header";
  import Aside from "../components/Aside";
  import Swiper from "../components/Swiper";
  import {mixin} from "../mixins";
  import {multipleClassify,singleClassify} from "../api";
  import {mapGetters} from 'vuex';

  export default {
    mixins: [mixin],
    components: {
      Aside,
      Header,
      Swiper,
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
      }
    },
    created(){

    },
    methods: {
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
        multipleClassify()
        .then(res => {
          this.res = res;
          console.log(res);
          this.$store.commit('setResult',this.res);
          this.$router.push({path: `/multipleClassify`,query:{res}});
        })
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
