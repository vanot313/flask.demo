const tokens = {
  jiang: {
    rolename: 'user'
  }
}

const users = {
  'jiang': {
    id: '3',
    username: 'jiang',
    email: '122222222@qq.com',
    mobile: '1234565',
    create_time: '2021-02-25 14:12:05',
    modify_time: '2021-02-25 14:12:05',
    last_login_time: '2021-03-21 00:10:39',
    avatar: '',
    description: 'I am a super administrator',
    birth: '2001-09-01',
    location: '浙江杭州'
  }
}

module.exports = [
  // user login
  {
    url: '/user/login',
    type: 'post',
    response: config => {
      const { username } = config.body
      const token = tokens[username]

      // mock error
      if (!token) {
        return {
          code: 60204,
          msg: '用户名或密码错误'
        }
      }

      return {
        code: 200,
        data: token,
        msg: '登录成功'
      }
    }
  },

  // get user info
  {
    url: '/user/detail',
    type: 'get',
    response: config => {
      // const { token } = config.query
      const info = users['jiang']

      // mock error
      if (!info) {
        return {
          code: 50008,
          msg: 'Login failed, unable to get user details.'
        }
      }

      return {
        code: 200,
        data: info
      }
    }
  },

  // user logout
  {
    url: '/user/logout',
    type: 'get',
    response: _ => {
      return {
        code: 200,
        data: 'success'
      }
    }
  }
]
