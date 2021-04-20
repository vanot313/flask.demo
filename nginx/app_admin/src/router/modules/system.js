/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

const systemRouter = {
  path: '/system',
  component: Layout,
  redirect: '/system/userInfo',
  name: 'System',
  meta: {
    title: '用户管理',
    icon: 'user',
    roles: ['admin']
  },
  children: [
    {
      path: 'userInfo',
      component: () => import('@/views/user-info/index'),
      name: 'UserInfo',
      meta: { title: '信息管理' }
    },
    {
      path: 'verify',
      component: () => import('@/views/expert-verify/index'),
      name: 'ExpertVerify',
      meta: { title: '专家审核' }
    }
  ]
}

export default systemRouter
