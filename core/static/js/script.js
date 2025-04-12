//console.log('¡JavaScript cargado!');

const mostrarBtn = document.getElementById('btn-agregar-gasto')
const cerrarBtn = document.getElementById('cerrarFormularioBtn')
const overlay = document.getElementById('formularioOverlay')

mostrarBtn.addEventListener('click', () => {
    overlay.style.display = 'flex';
});

cerrarBtn.addEventListener('click', () => {
    overlay.style.display = 'none';
});