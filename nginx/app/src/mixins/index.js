export const mixin = {
  methods: {
    //提示信息
    notify(title,type){
      this.$notify({
        title: title,
        type: type
      })
    },

    //根据相对地址获取绝对地址
    getUrl(url){
      return `${this.$store.state.HOST}/${url}`
    },


  }
}
