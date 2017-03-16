$('.switch').on('click', function(e) {
$('#fulljogo').toggleClass('jogo jogofull');
$('#telapequena').toggleClass('switch switch2');
});
$('.switch2').on('click', function(e) {
$('#fulljogo').toggleClass('jogofull jogo');
$('#telapequena').toggleClass('switch2 switch');
});
