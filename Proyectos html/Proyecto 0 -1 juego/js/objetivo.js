function moveobjetivo(){

  

  let x = 860; /*estos valores van a interpretar de donde empezaran*/ 
  let y = 400;

  const paso = 20;
  const limite_y = 400; /*Estos valores seran los limites del plano*/
  const limite_x = 860;

  const objetivo = document.getElementById("objetivo");

  document.addEventListener("keydown", (event) => {

    if (event.key === "d" && x < limite_x) {
      x += paso;
  
    } else if (event.key === "a" && x > 0) {
      x -= paso;
  
    } else if (event.key === "w" && y > 0) {
      y -= paso;
  
    } else if (event.key === "s" && y < limite_y) {
      y += paso;
  
    }
  
    objetivo.style.left = x + "px";
    objetivo.style.top = y + "px";
  
  });






}