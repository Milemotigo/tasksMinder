let prevScrollPos = window.pageYOffset;

window.onscroll = function() {
	let currentScrollPos = window.pageYOffset;
	if (prevScrollPos > currentScrollPos) {
		document.querySelector('.navbar-transition').style.top = '0px';
	} else {
		document.querySelector('.navbar-transition').style.top = '-100px'
}
prevScrollPos = currentScrollPos;
}

