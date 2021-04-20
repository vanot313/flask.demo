import Vue from 'vue'

import Cookies from 'js-cookie'

import 'normalize.css/normalize.css' // A modern alternative to CSS resets

import Element from 'element-ui'
import '@/styles/element-variables.scss'
// import 'element-ui/lib/theme-chalk/index.css'
// import enLang from 'element-ui/lib/locale/lang/en'// 如果使用中文语言包请默认支持，无需额外引入，请删除该依赖

import Scrollspy from 'vue2-scrollspy'
import BootstrapVue from 'bootstrap-vue'
import VueYoutube from 'vue-youtube'
import VueParticles from 'vue-particles'
const VueScrollTo = require('vue-scrollto')

import '@/styles/index.scss' // global css
import '@/styles/fonik/css/fonik.css'

import App from './App'
import router from './router'
import store from './store'

import '@/permission' // permission control

/**
 * If you don't want to use mock-server
 * you want to use MockJs for mock api
 * you can execute: mockXHR()
 *
 * Currently MockJs will be used in the production environment,
 * please remove it before going online ! ! !
 */
// if (process.env.NODE_ENV === 'production') {
//   const { mockXHR } = require('../mock')
//   mockXHR()
// }

Vue.use(Element, {
  size: Cookies.get('size') || 'medium' // set element-ui default size
})

Vue.use(VueParticles)
Vue.use(VueYoutube)
Vue.use(VueScrollTo)
Vue.use(BootstrapVue)
Vue.use(Scrollspy)

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
