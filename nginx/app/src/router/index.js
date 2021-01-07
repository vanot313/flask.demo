import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '../pages/Home';
import SingleClassify from "../pages/SingleClassify";
import MultipleClassify from "../pages/MultipleClassify";

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Home,
    },
    {
      path: '/main',
      component: Home,
    },
    {
      path: '/singleClassify',
      component: SingleClassify,
    },
    {
      path: '/multipleClassify',
      component: MultipleClassify,
    },
  ]
})
