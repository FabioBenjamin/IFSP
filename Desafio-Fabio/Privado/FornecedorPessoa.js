import Fornecedor from './Fornecedor.js';

class FornecedorPessoa extends Fornecedor {
    #rg;
    #cpf;

    constructor(nome = 'sem-nome', rg, cpf, fone = ' ') {
        super(nome, fone);
        this.#rg = rg;
        this.#cpf = cpf;
    }

    setRg(rg) {
        this.#rg = rg;
    }

    getRg() {
        return this.#rg;
    }

    setCpf(cpf) {
        this.#cpf = cpf;
    }

    getCpf() {
        return this.#cpf;
    }
}

export default FornecedorPessoa;