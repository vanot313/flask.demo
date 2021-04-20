import request from '@/utils/request'

export function getAllWaitWorkOrder(data) {
  return request({
    url: '/expert/all_wait_work_order',
    method: 'post',
    data
  })
}

export function getAllSelfWorkOrder(data) {
  return request({
    url: '/expert/all_self_work_order',
    method: 'post',
    data
  })
}

export function searchDetailWorkOrder(order_id) {
  return request({
    url: '/expert/detail_work_order ',
    method: 'post',
    data: {
      order_id
    }
  })
}

export function downloadOrderFile(order_id) {
  return request({
    url: '/expert/download_order_file',
    method: 'post',
    data: {
      order_id: order_id
    },
    responseType: 'blob'
  })
}

export function processComprehensive(data) {
  return request({
    url: '/expert/process_comprehensive',
    method: 'post',
    data
  })
}

export function processCost(data) {
  return request({
    url: '/expert/process_cost',
    method: 'post',
    data
  })
}

export function processEarning(data) {
  return request({
    url: '/expert/process_earning',
    method: 'post',
    data
  })
}
