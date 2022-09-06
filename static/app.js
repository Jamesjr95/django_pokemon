const vm = new Vue({
    el: '#app',
    delimiters: ['[[',']]'],
    data: {
        pokemon: []
    },

    methods: {
        loadPokemon: function(){
            axios({
                method:'get',
                url:'api/v1/pokemon/'
            }).then(response => {
                this.pokemon = response.data
            }).catch(error => {
                console.log(error);
            })
        }
    },

    mounted: function(){
        this.csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value
    },
    created: function(){
        this.loadPokemon()
    }

})
