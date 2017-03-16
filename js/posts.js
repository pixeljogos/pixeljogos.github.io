$('.switch').on('click', function(e) {
$('#fulljogo').toggleClass('jogo jogofull');
$('#telapequena').toggleClass('switch switch2');
var elem = document.getElementById("myvideo");
if (elem.requestFullscreen) {
  elem.requestFullscreen();
} else if (elem.msRequestFullscreen) {
  elem.msRequestFullscreen();
} else if (elem.mozRequestFullScreen) {
  elem.mozRequestFullScreen();
} else if (elem.webkitRequestFullscreen) {
  elem.webkitRequestFullscreen();
}
});
$('.switch2').on('click', function(e) {
$('#fulljogo').toggleClass('jogofull jogo');
$('#telapequena').toggleClass('switch2 switch');
});
