import Fornecedor from './Fornecedor.js';

class FornecedorPessoa extends Fornecedor{
    constructor(nome = 'sem-nome', rg, cpf, fone =' '){
        super(nome, fone)
        this.rg = rg
        this.cpf = cpf
    }

    setrg(rg){
        this.rg = rg
    }

    getnome(rg){
        return this.rg
    }

    setfone(cpf){
        this.cpf = cpf
    }

    getnome(cpf){
        return this.cpf
    }
}

export default FornecedorPessoa