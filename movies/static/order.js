function init() {
    console.log("order.js loaded");
    // hook the click from the rent button
    $(".btn-add").click(function(){
        var id = $(this).attr("movie-id");
        console.log("Btn clciked",id);
    });
}


window.onload = init;