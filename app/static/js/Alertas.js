function noADNObj() {
  Swal.fire({});

  Swal.fire({
    icon: "error",
    confirmButtonText: "De acuerdo",
    confirmButtonColor: "#0085A1",
    title:
      "El ADN objetivo que ingresaste no se ha encontrado. Por favor, intenta de nuevo.",
  }).then((result) => {
    if (result.isConfirmed) {
      location.href = "inicio";
    }
  });
}

function noARNs() {
  Swal.fire({
    icon: "error",
    confirmButtonText: "De acuerdo",
    confirmButtonColor: "#0085A1",
    title:
      "No se han detectado secuencias de ARN en la cadena de ADN objetivo que proporcionaste. Por favor, intenta con una nueva cadena de ADN.",
  }).then((result) => {
    if (result.isConfirmed) {
      location.href = "inicio";
    }
  });
}

function noNombreGen() {
  Swal.fire({
    icon: "error",
    confirmButtonText: "De acuerdo",
    confirmButtonColor: "#0085A1",
    title:
      "No se ha encontrado el nombre del gen ingresado. Por favor, intenta de nuevo.",
  }).then((result) => {
    if (result.isConfirmed) {
      location.href = "inicio";
    }
  });
}

/*

window.addEventListener("popstate", () => {
    Swal.fire({
        icon: "warning",
        title: "¿Seguro que quieres regresar?",
        text: "Hay cambios sin guardar que se perderán",
        confirmButtonText: "Regresar",
        cancelButtonText: 'Cancelar',
        confirmButtonColor: "#0085A1",
        showCancelButton: true,
    }).then((result) => {
        if (result.isConfirmed) {
            location.href = "inicio";
        } else {
            // Quedarse en la página actual
        }
    });
});

*/
