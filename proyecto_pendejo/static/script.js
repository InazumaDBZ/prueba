<<<<<<< HEAD
var btnAbrirPopup = document.getElementById('btn-abrir-popup'),
	btnOpenPopup = document.getElementById('btn-open-popup')
	overlay = document.getElementById('overlay'),
	popup = document.getElementById('popup'),
	btnCerrarPopup = document.getElementById('btn-cerrar-popup');

btnAbrirPopup.addEventListener('click', function () {
=======
var btnAbrirPopup = document.getElementById('btn-open'),
	overlay = document.getElementById('overlay'),
	popup = document.getElementById('popup'),
	btnCerrarPopup = document.getElementById('btn-close');

btnAbrirPopup.addEventListener('click', function(){
>>>>>>> master
	overlay.classList.add('active');
	popup.classList.add('active');
});

<<<<<<< HEAD
btnOpenPopup.addEventListener('click', function () {
	overlay.classList.add('active');
	popup.classList.add('active');
});

btnCerrarPopup.addEventListener('click', function (e) {
	e.preventDefault(); overlay.classList.remove('active');
	popup.classList.remove('active');
});

//Menú responsivo
function toggleMenu() {
	const toggleMenu = document.querySelector('.toggleMenu');
	const nav = document.querySelector('.nav');
	toggleMenu.classList.toggle('active')
	nav.classList.toggle('active')
}

let AbrirSideMenu = document.querySelector('.btn-abrir-sidemenu'),
	sidemenu = document.querySelector('.sidebar-menu')
	CerrarSideMenu = document.querySelector('.toggle');

	AbrirSideMenu.addEventListener('click', function(){
		sidemenu.classList.add('active');
	});

	CerrarSideMenu.addEventListener('click', function(){
		sidemenu.classList.remove('active');
	});


=======
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
>>>>>>> master
