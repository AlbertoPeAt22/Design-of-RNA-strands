const enlace = document.getElementById("enlace");

enlace.addEventListener("click", function(e) {

  e.preventDefault();

  const seccion = document.getElementById("section");

  window.scrollTo({
    top: seccion.offsetTop,
    left: 0, 
    behavior: "smooth",
    duration: 2000 // 10 segundos
  });

});