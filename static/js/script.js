$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    $('.datepicker').datepicker({
        format: "yyyy",
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
  });