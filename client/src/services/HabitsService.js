import Api from '@/services/Api'

export default {
<<<<<<< HEAD
  index() {
    return Api().get('habits')
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
  }
=======
    index() {
        return Api().get('habits')
    },
    create(habit) {
        return Api().post('habits', habit)
    },
    delete(id) {
        return Api().delete('habits/id/' + id)
    }
>>>>>>> Development
}