import request from '@/utils/request'

export function register(data) {
  return request({
    url: '/user/register',
    method: 'post',
    data
  })
}

export function login(data) {
  return request({
    url: '/user/login',
    method: 'post',
    data
  })
}

export function getInfo() {
  return request({
    url: '/user/detail',
    method: 'get'
  })
}

export function updateInfo(data) {
  return request({
    url: '/user/update',
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: '/user/logout',
    method: 'get'
  })
}

export function new_cost(data) {
  return request({
    url: '/user/new_cost',
    method: 'post',
    data
  })
}

export function new_earning(data) {
  return request({
    url: '/user/new_earning',
    method: 'post',
    data
  })
}

export function new_comprehensive(formData) {
  return request({
    url: '/user/new_comprehensive',
    method: 'post',
    data: formData,
    processData: false, // 告诉axios不要去处理发送的数据(重要参数)
    contentType: 'multipart/form-data' // 告诉axios不要去设置Content-Type请求头
  })
}

export function new_market(formData) {
  return request({
    url: '/user/new_market',
    method: 'post',
    data: formData,
    processData: false, // 告诉axios不要去处理发送的数据(重要参数)
    contentType: 'multipart/form-data' // 告诉axios不要去设置Content-Type请求头
  })
}

export function get_work_order(data) {
  return request({
    url: '/user/get_work_order',
    method: 'post',
    data
  })
}

export function detail_work_order(order_id) {
  return request({
    url: '/user/detail_work_order',
    method: 'post',
    data: {
      order_id: order_id
    }
  })
}

export function get_log(data) {
  return request({
    url: '/user/get_log',
    method: 'get',
    data
  })
}

export function apply_expert(data) {
  return request({
    url: '/user/apply_for_expert',
    method: 'post',
    data
  })
}
