$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('#modal1').modal();
    $('#carousel-auto').carousel();
        setInterval(function() {
    $('#carousel-auto').carousel('next');
        }, 2000);   
    $('select').formSelect();
     $('.carousel').carousel({
    fullWidth: false,
    indicators: true,
    pressed: true,
    onCycleTo: null
  });
  });