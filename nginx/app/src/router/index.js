import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '../pages/Home';
import SingleClassify from "../pages/SingleClassify";
import MultipleClassify from "../pages/MultipleClassify";
import Detail from "../pages/Detail";
import Analysis from "../pages/Analysis";

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
    {
      path: '/detail',
      component: Detail,
    },
    {
      path: '/analysis',
      component: Analysis,
    },
  ]
})
