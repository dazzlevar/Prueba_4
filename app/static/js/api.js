
var x = document.getElementById("resultado");

$("#btnLocalizar").ready(function () {
    navigator.geolocation.getCurrentPosition(function (position) {
        let lat = position.coords.latitude;
        let long = position.coords.longitude;

        $.get("https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + long + "&lang=sp&units=metric&appid=e7f7bdc257804d7dd9bc1b7af07e2a26", function (data) {
            console.log(data);
            $("#resultado").empty();
            $("#resultado").append("<ul>");
            $("#resultado").append("<li>" +"T°:"+ Math.round(data.main.temp) +"°C"+"</li>");
            $("#resultado").append("<ul>");
        });
    });
});