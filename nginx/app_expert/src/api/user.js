import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/expert/login',
    method: 'post',
    data
  })
}

export function getInfo() {
  return request({
    url: '/expert/detail',
    method: 'get'
  })
}

export function updateInfo(data) {
  return request({
    url: '/expert/update',
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: '/expert/logout',
    method: 'get'
  })
}
