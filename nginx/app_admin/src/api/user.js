import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/admin/login',
    method: 'post',
    data
  })
}

export function getInfo() {
  return request({
    url: '/admin/detail',
    method: 'get'
  })
}

export function updateInfo(data) {
  return request({
    url: '/admin/update',
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: '/admin/logout',
    method: 'get'
  })
}
