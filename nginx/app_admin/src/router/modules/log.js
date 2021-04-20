/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

const logRouter = {
  path: '/log',
  component: Layout,
  redirect: '/log/loginLog',
  name: 'Log',
  meta: {
    title: '日志管理',
    icon: 'xitongrizhi',
    roles: ['admin']
  },
  children: [
    {
      path: 'loginLog',
      component: () => import('@/views/login-log/index'),
      name: 'LoginLog',
      meta: { title: '登录日志' }
    },
    {
      path: 'actionLog',
      component: () => import('@/views/action-log/index'),
      name: 'ActionLog',
      meta: { title: '操作日志' }
    }
  ]
}

export default logRouter
