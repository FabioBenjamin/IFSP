class Fornecedor {
    #nome;
    #fone;

    constructor(nome = 'sem-nome', fone = '(11) 1111-2222') {
        this.#nome = nome;
        this.#fone = fone;
    }

    set_fone(fone) {
        this.#fone = fone;
    }

    get_fone() {
        return this.#fone;
    }

    set_nome(nome) {
        this.#nome = nome;
    }

    get_nome() {
        return this.#nome;
    }
}

export default Fornecedor;