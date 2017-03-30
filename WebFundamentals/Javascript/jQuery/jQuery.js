$(document).ready(function(){
  $('.slidetoggle button').click(function() {
    $("p").slideToggle();
  });

  $("#show").click(function(){
    $(".hideshow p").show();
  });

  $("#hide").click(function(){
    $(".hideshow p").hide();
  });

  $("#togglebutton").click(function (){
    $(".toggle p").toggle();
  });

  $("#append").click(function(){
    $(".append p").append("to the end of this sentence!")
  });

  $("#slide").click(function(){
    if($(".slide p").is(":hidden")){
      $(".slide p").slideDown();
    } else {
      $(".slide p").slideUp();
    }
  });

  $("#before").click(function(){
    $(".beforeafter p").before("Adding text before")
  });

  $("#after").click(function(){
    $(".beforeafter p").after("Adding text after")
  });

  $("#change").click(function(){
    $("#change").html("New content!")
  });

  $("#class").click(function(){
    $("h2").addClass("selected");
  });

  $("#fadeout").click(function(){
    $(".fade p").fadeOut("slow");
  });

  $("#fadein").click(function(){
    $(".fade p").fadeIn("slow");
  });

  $("input").keyup(function(){
    var value = $(this).val();
    $(".val p").text(value);
  });

});
