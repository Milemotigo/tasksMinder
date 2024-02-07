function toggleBar() {
	let offcanvasBottom = document.getElementById('offcanvasBottom');
	let offcanvasInst = new bootstrap.Offcanvas(offcanvasBottom);
	offcanvasInst.toggle();
}
