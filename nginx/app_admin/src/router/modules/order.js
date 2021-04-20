/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

const orderRouter = {
  path: '/order',
  component: Layout,
  redirect: '/order/manage',
  children: [{
    path: 'manage',
    name: 'OrderManage',
    component: () => import('@/views/order-manage/index'),
    meta: {
      title: '工单管理',
      icon: 'gongdanguanli'
    }
  }]
}

export default orderRouter
