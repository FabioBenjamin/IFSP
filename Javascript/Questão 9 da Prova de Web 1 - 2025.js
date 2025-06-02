let val = 1;
if (val < 5){
    val += 2;
    if (val === 3){
        val ++;
        if (val < 5){
            console.log("Menor que 5");
        }
        else {
            console.log("Valor 5");
        }
    }
    else {
        console.log("Não é 3");
    }
}
else {
    console.log("sMaior ou igual a 5");
}