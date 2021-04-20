import request from '@/utils/request'

export function getUserInfo() {
  return request({
    url: '/admin/get_user_info',
    method: 'get'
  })
}

export function searchUserInfo(data) {
  return request({
    url: '/admin/get_user_info',
    method: 'post',
    data
  })
}

export function updateUserInfo(data) {
  return request({
    url: '/admin/update_user_info',
    method: 'post',
    data
  })
}

export function getWorkOrder() {
  return request({
    url: '/admin/get_work_order',
    method: 'get'
  })
}

export function searchWorkOrder(data) {
  return request({
    url: '/admin/get_work_order',
    method: 'post',
    data
  })
}

export function getLoginLog() {
  return request({
    url: '/admin/get_login_log',
    method: 'get'
  })
}

export function searchLoginLog(data) {
  return request({
    url: '/admin/get_login_log',
    method: 'post',
    data
  })
}

export function getLog() {
  return request({
    url: '/admin/get_log',
    method: 'get'
  })
}

export function searchLog(data) {
  return request({
    url: '/admin/get_log',
    method: 'post',
    data
  })
}

export function detail_work_order(data) {
  return request({
    url: '/admin/detail_work_order',
    method: 'post',
    data
  })
}

export function searchExpertApply(data) {
  return request({
    url: '/admin/get_expert_apply',
    method: 'post',
    data
  })
}

export function updateExpertApply(data) {
  return request({
    url: '/admin/update_expert_apply',
    method: 'post',
    data
  })
}

export function register(data) {
  return request({
    url: '/user/register',
    method: 'post',
    data
  })
}
