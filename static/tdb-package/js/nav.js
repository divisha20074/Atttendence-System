/*sidebar*/
$(document).ready(function() {
$(".fa-bars").click(function() {
    $(".fa-times").toggle(500);
    $(".fa-bars").toggle(500);
$(".sidebar").toggle();
});
$(".fa-times,section").click(function() {
    $(".fa-times").hide(500);
    $(".fa-bars").show(500);
$(".sidebar").fadeOut(300);
});
});
