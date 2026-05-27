package com.example.PrimeiraAPI;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HomeController {
    @GetMapping("/") // Rota padrão
    public String inicio(){
        return "API FUNCIONANDO COM SPRING BOOT";
    }

    @GetMapping("/mensagem")
    public String mensagem(){
        return "Bem-vindos à aula prática de spring boot";
    }
}
