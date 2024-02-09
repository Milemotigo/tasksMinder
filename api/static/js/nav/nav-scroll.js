let prevScrollPos = window.pageYOffset;

window.onscroll = function() {
	let currentScrollPos = window.pageYOffset;
	if (prevScrollPos > currentScrollPos) {
		document.querySelector('.navbar-transition').style.top = '0px';
		document.querySelector('.navbar-transition2').style.bottom = '0px';
	} else {
		document.querySelector('.navbar-transition').style.top = '-100px'
		document.querySelector('.navbar-transition2').style.bottom = '-70px';
}
prevScrollPos = currentScrollPos;
}

