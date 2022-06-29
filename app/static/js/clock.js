$(document).ready(function() {
    // Hora
    setInterval(function() {
        $('#reloj').html(moment().format('HH:mm:ss'))
    });

    // Botón para subir
    $('.subir').click(function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: 0,
        }, 200);
        return false;
    });
});