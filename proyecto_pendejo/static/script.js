var btnAbrirPopup = document.getElementById('btn-open'),
	overlay = document.getElementById('overlay'),
	popup = document.getElementById('popup'),
	btnCerrarPopup = document.getElementById('btn-close');

btnAbrirPopup.addEventListener('click', function(){
	overlay.classList.add('active');
	popup.classList.add('active');
});

btnCerrarPopup.addEventListener('click', function(e){
	e.preventDefault();
	overlay.classList.remove('active');
	popup.classList.remove('active');
});



// function toogleMenu(){
//     const toggleMenu() = document.querySelector('.toggle');
//     const nav = document.querySelector('.nav');
//     toggleMenu.classList.toggle('active')
//     nav.classList.toggle('active')
// }