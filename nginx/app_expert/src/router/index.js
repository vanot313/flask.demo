import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/* Router Modules */

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/redirect/:path(.*)',
        component: () => import('@/views/redirect/index')
      }
    ]
  },

  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/error-page/404'),
    hidden: true
  },

  {
    path: '/401',
    component: () => import('@/views/error-page/401'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: {
        title: '首页',
        icon: 'dashboard'
        // noCache: true // 如果设置为true，则不会被 <keep-alive> 缓存(默认 false)
        // breadcrumb: false //  如果设置为false，则不会在breadcrumb面包屑中显示(默认 true)
        // affix: true // 如果设置为true，它则会固定在tags-view中(默认 false)
      }
    }]
  },

  {
    path: '/profile',
    component: Layout,
    redirect: '/profile/index',
    hidden: true,
    children: [
      {
        path: 'index',
        component: () => import('@/views/profile/index'),
        name: 'Profile',
        meta: { title: '个人中心', icon: 'user', noCache: true }
      }
    ]
  },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [
  {
    path: '/order/assess',
    component: Layout,
    redirect: '/order/assess',
    children: [{
      path: '',
      name: 'OrderAssess',
      component: () => import('@/views/order-assess/index'),
      meta: {
        title: '工单评估',
        icon: 'pinggu',
        roles: ['expert'],
        noCache: true
      }
    }]
  },

  {
    path: '/order/history',
    component: Layout,
    redirect: '/order/history',
    children: [{
      path: '',
      name: 'OrderHistory',
      component: () => import('@/views/order-history/index'),
      meta: {
        title: '历史工单',
        icon: 'gongdanguanli',
        roles: ['expert']
      }
    }]
  },

  {
    path: '/order',
    component: Layout,
    redirect: '/order/detail',
    hidden: true,
    children: [
      {
        path: 'detail',
        name: 'OrderDetail',
        component: () => import('@/views/order-detail/index'),
        meta: {
          title: '工单详情',
          roles: ['expert'] }
      }]
  }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  base: '/exp/',
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
