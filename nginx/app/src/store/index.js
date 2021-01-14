/*状态管理，存放全局变量*/
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    result: [],
  },
  getters: {//getter类似于vue的computed
    result: state => state.result,

  },
  mutations: {
    setResult: (state, result) => {state.result = result},
  }
})

export default store
