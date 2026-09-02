import Fornecedor from './Fornecedor.js';

class FornecedorEmpresa extends Fornecedor {
    #cnpj;
    #ie;

    constructor(nome, fone, cnpj, ie) {
        super(nome, fone);
        this.#cnpj = cnpj;
        this.#ie = ie;
    }

    get_cnpj() {
        return this.#cnpj;
    }

    set_cnpj(cnpj) {
        this.#cnpj = cnpj;
    }

    get_ie() {
        return this.#ie;
    }

    set_ie(ie) {
        this.#ie = ie;
    }
}

export default FornecedorEmpresa;