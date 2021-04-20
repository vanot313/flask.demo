const getters = {
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  name: state => state.user.name,
  introduction: state => state.user.introduction,
  roles: state => state.user.roles,
  id: state => state.user.id,
  permission_routes: state => state.permission.routes
}

export default getters
