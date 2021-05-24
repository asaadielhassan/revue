import Api from '@/services/Api'

export default {
  index() {
    return Api().get('grids/public')
  },

  create(grid) {
    return Api().post('grids', grid)
  },

  delete(id) {
    return Api().delete('grids/id/' + id)
  },

  item(id) {
    return Api().get('grids/id/' + id)
  },

  user(username) {
    return Api().get('grids/user/' + username)
  }
}