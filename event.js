
function positionFunction(){
	var img = document.getElementById('bannerImage');
	var height = img.clientHeight;
 	document.getElementById("position").style.height= height+'px'}


window.addEventListener('load', positionFunction, true)
window.addEventListener('resize', positionFunction, true)

