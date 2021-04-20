/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

const crawlerRouter = {
  path: '/crawler',
  component: Layout,
  redirect: '/crawler/run',
  name: 'Crawler',
  meta: {
    title: '数据爬取',
    icon: 'crawler',
    roles: ['admin']
  },
  children: [
    {
      path: 'run',
      component: () => import('@/views/crawler-run/index'),
      name: 'CrawlerRun',
      meta: { title: '爬虫运行' }
    },
    {
      path: 'list',
      component: () => import('@/views/crawler-list/index'),
      name: 'CrawlerList',
      meta: { title: '爬虫管理' },
      hidden: true
    }
  ]
}

export default crawlerRouter
