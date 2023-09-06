var num1 = undefined;
var num2 = "";
var op = undefined;
var tela = "";

let numeros = document.getElementsByClassName("btn-light");
let operadores = document.getElementsByClassName("operator");
let inverter = document.getElementById("inverter");
let igual = document.getElementById("igual");
let ponto = document.getElementById("ponto");
let limpar = document.getElementById("limpar");

inverter.addEventListener("click", inverter_sinal, false);
igual.addEventListener("click", resultado, false);
ponto.addEventListener("click", decimal, false);
limpar.addEventListener("click", resetar, false);


for (i = 0; i < numeros.length; i++){
  numeros[i].addEventListener('click', inserir_valor, false);
}

for (i = 0; i < operadores.length; i++){
  operadores[i].addEventListener('click', operacao, false);
}

function inserir_valor(e){
  if (num1 == undefined){
    num1 = e.srcElement.value;
    tela = num1;
    document.getElementById("tela").value = tela;    
  }
  else if (op == undefined){   
    if(tela.search(/[.]/g) == tela.length - 1){
      num1 = tela.concat(e.srcElement.value);
    }else{
      num1 += e.srcElement.value;
    }   
    tela = num1
    document.getElementById("tela").value = tela;
  }
  else{
    if(tela.search(/[.]/g) == tela.length - 1){
      num2 = tela.concat(e.srcElement.value);
    }else{
      num2 += e.srcElement.value;
    }
    tela = num2
    document.getElementById("tela").value = tela;
  }  
}

function operacao(e){
  if(num1 != undefined && op == undefined){
    document.getElementById("tela").value = "";
    op = e.srcElement.innerHTML;
    tela = op;
    console.log(op);
    document.getElementById("tela").value = tela;
  }
}

function inverter_sinal(e){
  if(tela != "" && tela != "+" && tela != "-" && tela != "×" && tela != "÷"){
    if(tela[0] == "-"){
      tela = tela.slice(1);
    }
    else{
      tela = "-" + tela;
    }
    document.getElementById("tela").value = tela;
  }
}

function resultado(e){
  if(num1 != undefined && op != undefined && (num2 != undefined || num2 != "")){
    console.log(`Operação: ${op}`);
    if(op == "+"){
      tela = String(parseFloat(num1) + parseFloat(num2)); 
    }else if (op == "-"){
      tela = String(parseFloat(num1) - parseFloat(num2)); 
    }else if (op == "×"){
      tela = String(parseFloat(num1) * parseFloat(num2)); 
    }else if (op == "÷"){
      tela = String(parseFloat(num1) / parseFloat(num2)); 
    }
    document.getElementById("tela").value = tela;
    num1 = tela;
    op = undefined;
    num2 = ""
  }
}

function decimal(e){
  if(!tela.includes(".")){
    tela = tela.concat(".");
    document.getElementById("tela").value = tela;
  }
  
}

function resetar(e){
  num1 = undefined;
  num2 = "";
  op = undefined;
  tela = "";
  document.getElementById("tela").value = tela;
}