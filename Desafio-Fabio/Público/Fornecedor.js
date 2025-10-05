class Fornecedor {

    constructor(nome = 'sem-nome', fone = '(11) 1111-2222'){
    this.nome = nome
    this.fone = fone}

    set_fone(fone){
        this.fone
    }

    get_fone(fone){
        return this.fone
    }

    set_nome(nome){
        this.nome
    }

    get_nome(nome){
       return this.nome 
    }

}

export default Fornecedor