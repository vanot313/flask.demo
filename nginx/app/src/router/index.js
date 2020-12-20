import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '../components/Home';
import Login from '../pages/login';

Vue.use(VueRouter);

export default new VueRouter({
  routes: [
    {
      path: '/',
      component: Login
    }
  ]
})
