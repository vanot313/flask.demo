<template>
  <div class="fonik">
    <layout />
    <div class="wrapper">
      <div class="container-fluid">

        <div class="row">
          <div class="col-12">
            <left-bar />

            <!-- Right Sidebar -->
            <div class="email-rightbar mb-3">
              <right-bar />
              <div class="card m-t-20">
                <div class="card-body">

                  <el-form :label-position="labelPosition">
                    <h2 style="padding-bottom: 30px;font-weight: 500;font-family: 'Microsoft YaHei',sans-serif">新建工单</h2>

                    <el-form-item label="评估方法" label-width="80px">
                      <el-radio v-model="method" label="1" border>成本法</el-radio>
                      <el-radio v-model="method" label="2" border>收益法</el-radio>
                      <el-radio v-model="method" label="3" border>综合估值法</el-radio>
                      <el-radio v-model="method" label="4" border>市场法</el-radio>
                    </el-form-item>

                    <el-form-item label="备注" label-width="80px">
                      <el-input
                        v-model="form.remarks"
                        :autosize="{ minRows: 4, maxRows: 8}"
                        type="textarea"
                        :placeholder="placeholder[method]"
                        style="width: 90%"
                      />
                    </el-form-item>

                    <el-form-item v-if="method === '3' || method === '4'" label="附件" label-width="80px">
                      <el-upload
                        ref="upload"
                        class="upload-demo"
                        drag
                        action=""
                        multiple
                        :auto-upload="false"
                        :file-list="formFileList"
                        :http-request="handleUploadForm"
                        :on-exceed="formHandleExceed"
                        :on-remove="formHandleRemove"
                        :before-upload="beforeUploadForm"
                        accept=".csv,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel"
                      >
                        <i class="el-icon-upload" />
                        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                      </el-upload>
                    </el-form-item>

                    <el-form-item label-width="80px">
                      <button type="button" class="btn btn-primary waves-effect waves-light" @click="submit">提 交</button>
                    </el-form-item>
                  </el-form>
                </div>
              </div>
            </div>
            <!-- end Col-9 -->
          </div>
        </div>
        <!-- End row -->
      </div>
      <!-- end container -->
    </div>
    <!-- end wrapper -->
  </div>
</template>

<script>
import Layout from '@/components/Layout/index'
import LeftBar from '@/components/LeftBar/index'
import RightBar from '@/components/RightBar/index'
import { new_cost, new_earning, new_comprehensive, new_market } from '@/api/user'

export default {
  components: {
    Layout,
    LeftBar,
    RightBar
  },
  data() {
    return {
      labelPosition: 'left',
      placeholder: [
        '请先选择评估方法',
        '请输入您需要考察的公司名称，和任何您想留给专家的备注',
        '请输入您需要考察的公司名称，和任何您想留给专家的备注',
        '我们评估的是您上传的文件，此处为用户备注，选填',
        '我们评估的是您上传的文件，此处为用户备注，选填'
      ],
      method: '0',
      form: {
        remarks: ''
      },
      formMaxSize: 100, // 上传文件大小(MB)
      formFileList: [], // 显示上传文件
      uploadFormFileList: [] // 确定上传文件
    }
  },
  methods: {
    reset() {
      this.method = '0'
      this.form.remarks = ''
      this.formFileList = []
      this.uploadFormFileList = []
    },
    // 开始上传前验证
    beforeUploadForm(file) {
      // 验证文件大小
      if (file.size / 1024 / 1024 > this.formMaxSize) {
        this.$message({
          message: `上传文件大小不能超过${this.formMaxSize}M!`,
          type: 'warning'
        })
        return false
      }
      // 中文乱码处理
      if (file.raw) {
        const reader = new FileReader() // 读取文件内容
        reader.readAsText(file.raw, 'gb2312') // 防止中文乱码问题，不加reader.onload方法都不会触发
        reader.onload = function(e) {
          this.contentHtml = e.target.result // txt文本内容，接下来就可以对其进行校验处理了
        }
      }
      // 验证文件类型
      var testmsg = file.name.substring(file.name.lastIndexOf('.') + 1)
      const extension = testmsg === 'xlsx' || testmsg === 'xls' || testmsg === 'csv'
      if (!extension) {
        this.$message({
          message: '上传文件只能是xlsx/xls/csv格式!',
          type: 'warning'
        })
      }
      return extension
    },
    // 移除上传列表中文件
    formHandleRemove(file, formFileList) {
      const thiz = this
      for (let i = 0; i < thiz.uploadFormFileList.length; i++) {
        if (thiz.uploadFormFileList[i].pname === file.name) {
          thiz.uploadFormFileList.splice(i, 1)
          break
        }
      }
    },
    // 允许上传文件个数验证
    formHandleExceed(files, formFileList) {
      this.$message.warning(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + formFileList.length} 个文件`)
    },
    // 上传文件
    handleUploadForm(param) {
      let thiz = this
      let formData = new FormData()
      formData.append('remarks', this.form.remarks) // 额外参数
      formData.append('file', param.file)
      // let loading = thiz.$loading({
      //   lock: true,
      //   text: '上传中，请稍候...',
      //   spinner: 'el-icon-loading',
      //   background: 'rgba(0, 0, 0, 0.7)'
      // })
      if (this.method === '3') {
        new_comprehensive(formData).then(() => {
          this.$notify({
            title: 'Success',
            message: '提交成功',
            type: 'success',
            duration: 2000
          })
          this.reset()
        })
      } else if (this.method === '4') {
        new_market(formData).then(() => {
          this.$notify({
            title: 'Success',
            message: '提交成功',
            type: 'success',
            duration: 2000
          })
          this.reset()
        })
      }
      // loading.close()
    },
    submit() {
      if (this.method === '0') {
        this.$notify({
          title: 'Error',
          message: '请先选择评估方法！',
          type: 'error',
          duration: 2000
        })
      } else if (this.method === '1') {
        new_cost(this.form).then(() => {
          this.$notify({
            title: 'Success',
            message: '提交成功',
            type: 'success',
            duration: 2000
          })
          this.reset()
        })
      } else if (this.method === '2') {
        new_earning(this.form).then(() => {
          this.$notify({
            title: 'Success',
            message: '提交成功',
            type: 'success',
            duration: 2000
          })
          this.reset()
        })
      } else {
        this.$refs.upload.submit()
      }
    }
  }
}
</script>
