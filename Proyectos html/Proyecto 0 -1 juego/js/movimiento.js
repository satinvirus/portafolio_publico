function move(){

  let panel = document.getElementById("juego");

  let x = 0;
  let y = 0;

  const paso = 20;
  const limite_y = 400; 
  const limite_x = 860;

  const jugador = document.getElementById("cuadro");

  document.addEventListener("keydown", (event) => {

    if (event.key === "ArrowRight" && x < limite_x) {
      x += paso;
  
    } else if (event.key === "ArrowLeft" && x > 0) {
      x -= paso;
  
    } else if (event.key === "ArrowUp" && y > 0) {
      y -= paso;
  
    } else if (event.key === "ArrowDown" && y < limite_y) {
      y += paso;
  
    }
  
    jugador.style.left = x + "px";
    jugador.style.top = y + "px";
  
  });






}

