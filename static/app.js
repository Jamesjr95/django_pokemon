const vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        csrfToken: '',
        pokemon: [],
        user: [],
        detail: [],
        currentUser: {},
    },

    methods: {
        loadPokemon: function () {
            axios({
                method: 'get',
                url: 'api/v1/pokemon/'
            }).then(response => {
                this.pokemon = response.data
            }).catch(error => {
                console.log(error);
            })
        },
        loadUser: function () {
            axios({
                method: 'get',
                url: 'api/v1/current-user'
            }).then(response => {
                this.currentUser = response.data
            }).catch(error => {
                console.log(error);
            })
        },
        loadDetail: function (item) {
            axios({
                method: 'get',
                url: `api/v1/pokemon/${item.id}`
            }).then(response => {
                this.detail = response.data
                this.pokemon = []
                console.log(response.data);
            }).catch(error => {
                console.log(error)
            })

        },
        catchUncatch : function (pokemon) {
            if (!this.currentUser['caught'].includes(pokemon.id)) {
                this.currentUser['caught'].push(pokemon.id)
            } else {
                this.currentUser['caught'].splice(this.currentUser.caught.indexOf(pokemon.id), 1)
            }
            axios({
                method: 'patch',
                url: 'api/v1/current-user/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data:{
                    'caught': this.currentUser.caught
                }
            }).then(response => {
                console.log(response);
                this.loadUser()
            })
        }
    },
    mounted: function () {
        this.csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value
    },
    created: function () {
        this.loadPokemon()
        this.loadUser()
    }

})
