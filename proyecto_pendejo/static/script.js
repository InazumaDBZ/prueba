// var btnAbrirPopup = document.getElementById('btn-abrir-popup'),
// var	btnOpenPopup = document.getElementById('btn-open-popup'),
// 	overlay = document.getElementById('overlay')
// 	popup = document.getElementById('popup'),
// 	btnCerrarPopup = document.getElementById('btn-cerrar-popup');

// btnAbrirPopup.addEventListener('click', function () {
// 	overlay.classList.add('active');
// 	popup.classList.add('active');
// });

// btnOpenPopup.addEventListener('click', function () {
// 	overlay.classList.add('active');
// 	popup.classList.add('active');
// });

// btnCerrarPopup.addEventListener('click', function (e) {
// 	e.preventDefault(); overlay.classList.remove('active');
// 	popup.classList.remove('active');
// });



//Menú responsivo
function toggleMenu() {
	const toggleMenu = document.querySelector('.toggleMenu');
	const nav = document.querySelector('.nav');
	toggleMenu.classList.toggle('active')
	nav.classList.toggle('active')
}

window.addEventListener('scroll', function () {
	var header = document.querySelector('header');
	header.classList.toggle('sticky', window.scrollY > 0);
});

var btnAbrirProfile = document.querySelector(".btn-abrir-profile");
btnAbrirProfile.addEventListener("click", function () {
	document.querySelector(".wrapper").classList.toggle("active");
})