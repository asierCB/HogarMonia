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

//Overlay lista de la compra formulario
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