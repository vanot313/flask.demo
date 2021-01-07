import Vue from 'vue'
import App from './App'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import VueAxios from'vue-axios'
import router from './router'
import VCharts from 'v-charts'

Vue.use(VueAxios,axios);
Vue.use(router);
Vue.use(ElementUI);
Vue.use(VCharts);


new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
