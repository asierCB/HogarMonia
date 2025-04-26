//Overlay gastos formulario
const mostrarBtnG = document.getElementById('btn-agregar-gasto')
const cerrarBtnG = document.getElementById('cerrarFormularioBtnG')
const overlayG = document.getElementById('formularioOverlayG')

if (mostrarBtnG && cerrarBtnG && overlayG) {
    mostrarBtnG.addEventListener('click', () => {
        overlayG.style.display = 'flex';
    });

    cerrarBtnG.addEventListener('click', () => {
        overlayG.style.display = 'none';
    });
}

//Overlays lista de la compra formulario
    //Añadir elemento
const mostrarBtnElemLC = document.getElementById('btn-agregar-elemento-lista')
const cerrarBtnElemLC = document.getElementById('cerrarFormularioBtnElemLC')
const overlayElemLC = document.getElementById('formularioOverlayElemLC')

if (mostrarBtnElemLC && cerrarBtnElemLC && overlayElemLC) {
    mostrarBtnElemLC.addEventListener('click', () => {
        overlayElemLC.style.display = 'flex';
    });

    cerrarBtnElemLC.addEventListener('click', () => {
        overlayElemLC.style.display = 'none';
    });
}

    //Añadir lista
const mostrarBtnLC = document.getElementById('btn-agregar-lista')
const cerrarBtnLC = document.getElementById('cerrarFormularioBtnLC')
const overlayLC = document.getElementById('formularioOverlayLC')

if (mostrarBtnLC && cerrarBtnLC && overlayLC) {
    mostrarBtnLC.addEventListener('click', () => {
        overlayLC.style.display = 'flex';
    });

    cerrarBtnLC.addEventListener('click', () => {
        overlayLC.style.display = 'none';
    });
}


//Overlay Tarea
const mostrarBtnT = document.getElementById('btn-agregar-tarea')
const cerrarBtnT = document.getElementById('cerrarFormularioBtnT')
const overlayT = document.getElementById('formularioOverlayT')

if (mostrarBtnT && cerrarBtnT && overlayT) {
    mostrarBtnT.addEventListener('click', () => {
        overlayT.style.display = 'flex';
    });

    cerrarBtnT.addEventListener('click', () => {
        overlayT.style.display = 'none';
    });
}

//Boton opciones desplegable
document.addEventListener('DOMContentLoaded', () => {
    const opcionesTareasBotones = document.querySelectorAll('.opciones-tareas');

    opcionesTareasBotones.forEach(button => {
        const listaOpciones = button.nextElementSibling; // Asume que la lista sigue al botón
        if (listaOpciones && listaOpciones.classList.contains('lista-acciones')) {
            button.addEventListener('click', () => {
                listaOpciones.classList.toggle('show');
            });

            const listItems = listaOpciones.querySelectorAll('li');
            listItems.forEach(item => {
                item.addEventListener('click', (event) => {
                    event.stopPropagation(); // Detiene la propagación del clic
                    listaOpciones.classList.remove('show');
                    console.log('Opción seleccionada:', item.dataset.value);
                    // Aquí puedes agregar la lógica para eliminar o editar la tarea
                });
            });
        }
    });

    // Cerrar las listas cuando se hace clic fuera
    document.addEventListener('click', (event) => {
        const listasActivas = document.querySelectorAll('.lista-acciones.show');
        listasActivas.forEach(lista => {
            const botonAsociado = lista.previousElementSibling; // Asume que el botón está antes de la lista
            if (botonAsociado && !botonAsociado.contains(event.target) && !lista.contains(event.target)) {
                lista.classList.remove('show');
            }
        });
    });
});

//Perfil
// Ocultar mensajes de las notificaciones despues de 3s
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(function () {
        const messages = document.getElementById('messages');
        if (messages) {
            messages.style.display = 'none';
        }
    }, 3000);
});

