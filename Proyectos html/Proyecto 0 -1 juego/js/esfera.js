
let x = 400; //horizontal 
let y = 300; //vertical
let yendo = true;  // true = derecha , false = izquierda

const limite_y = 560; 
const limite_x = 860;

let dx =1;
let dy =1;

const objeto = document.getElementById("esfera");
const obstaculo1 = document.getElementById("cuadro");
const obstaculo2 = document.getElementById("objetivo");


function detectarColision(a, b) {
    const rectA = a.getBoundingClientRect();
    const rectB = b.getBoundingClientRect();
    

    return !(
      rectA.right < rectB.left || rectA.left > rectB.right ||
      rectA.bottom < rectB.top || rectA.top > rectB.bottom );
  }



  function reboteAleatorio() {
    let r = (Math.random() - 0.5) * 4; // entre -2 y 2
    if (Math.abs(r) < 0.5) r = r < 0 ? -1 : 1; // evitar casi cero
    return r;
  }


function esfera(){
    x += dx;
    y += dy;
 

// Movimiento normal
if (x <= 0 || x >= limite_x) {
    dx *= -1;
    dy = reboteAleatorio();
  }

  if (y <= 0 || y >= limite_y) {
    dy *= -1;
    dx = reboteAleatorio();
  }

  // Aplicar posición
  objeto.style.left = x + "px";
  objeto.style.top = y + "px";

  // Detectar colisión
  if (detectarColision(objeto, obstaculo1) || detectarColision(objeto, obstaculo2)) {
    yendo = !yendo; // Cambiar dirección
    dx *=-1;
    dy = reboteAleatorio();
  }

  // Cambiar dirección en los extremos
  if (x >= limite_x) {
    yendo = false;

  } else if (x <= 0) {
    yendo = true;
  }

  
    

}

setInterval(esfera,5)