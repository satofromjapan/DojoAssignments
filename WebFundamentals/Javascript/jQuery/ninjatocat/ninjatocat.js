$(document).ready(function(){
  $("img").click(function(){
    var alt = $(this).attr('data-alt-src');

      $(this).attr("src", alt);
  });

  $("img").click(function(){
    var ori = $(this).attr('src');
    $(this).attr("src", ori);
  })


});
