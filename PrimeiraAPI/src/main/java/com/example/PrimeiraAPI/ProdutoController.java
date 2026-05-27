package com.example.PrimeiraAPI;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class ProdutoController {

    @GetMapping("/produto")
    public Produto produto(){
        return new Produto(1L, "Notebook", 35000.00);
    }

    @GetMapping("/produtos")
    public List<Produto> listanarProdutos(){
        return List.of(
                new Produto(1L, "Notebook", 3500),
                new Produto(2L, "Mouse", 89),
                new Produto(3L, "Teclado", 150)
        );
    }
}
