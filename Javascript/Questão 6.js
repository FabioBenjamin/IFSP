let vendas = 7;
let bonus = 0;
let superVendedor = false;

if (vendas >= 5) {
    bonus += 10;
    if (vendas > 10){
        bonus += 20;
        superVendedor = true;
    }
    
    else if (vendas >= 8){
    bonus += 10;
    }
    else if (vendas === 7){
    bonus += 5;
    }
else if (vendas >= 3){
    bonus == 3;
}
else {
    bonus -+ 2;
}
if (!superVendedor && vendas % 2 === 1){
    bonus ++;
}
console.log("Total de bônus: " + bonus);
}
