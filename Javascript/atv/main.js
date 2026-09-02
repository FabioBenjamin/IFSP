import Fornecedor from './FornecedorPessoa.js'
import FornecedorPessoa from './Fornecedor.js'
import FornecedorEmpresa from './FornecedorEmpresa.js'

const starGames = new FornecedorEmpresa('StarGame', '(11) 00000-0000', '11.123.123/1234-1')
const Mau = new FornecedorPessoa('Mau', '12.123.113.1', '123456789')

console.log('Nome = ', Mau.get_nome(), '\ntelefone: ', Mau.get_fone())
Mau.set_nome("MAU MAU")
Mau.set_fone("11 11111-1111")
console.log("ababa ababa"); 
console.log("Nome: ", Mau.get_nome(), "\ntelefone: ", Mau.set_fone())

console.log("Nome empresa: ", starGames.get_nome(), "\ncnpj: ", starGames.get_cnpj())