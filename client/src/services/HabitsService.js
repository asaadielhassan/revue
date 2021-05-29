import Api from '@/services/Api'

export default {
  index() {
    return Api().get('habits/public')
  },

  create(habit) {
    return Api().post('habits', habit)
  },

  delete(id) {
    return Api().delete('habits/id/' + id)
  },

  item(id) {
    return Api().get('habits/id/' + id)
  },

  user(username) {
    return Api().get('habits/user/' + username)
  },

  update(id){
    return Api().post('habits/update/'+ id)
  }
}