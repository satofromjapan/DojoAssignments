$(document).ready(function(){

  $(document).on("submit","form", function(){
    $(".contactcard").append("<div class='card'></div>");
    var first_name = $("#first_name").val();
    var last_name = $("#last_name").val();
    var description = $("#description").val();
    // console.log("first name is:", first_name);
    // console.log("last name is:", last_name);
    // console.log("description is:", description);

    $(".contactcard").children(".card:last").append("<span><h3>"+ first_name + " " + last_name + "</h3><p>Click for description!</p></span><p id=desc>"+description+"</p>");

    //To clear the text boxes
    $("#first_name, #last_name, #description").val("");


    return false;
  });
  $(document).on("click",".card", function(){
    $(this).children().toggle();
  })
})
