import Api from '@/services/Api'

export default {
    create(task) {
        return Api().post('grids', task)
    },
}