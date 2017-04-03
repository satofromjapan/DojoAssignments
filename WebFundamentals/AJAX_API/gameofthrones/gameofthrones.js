$(document).ready(function() {
  $('img').mouseenter(function(){
    $(this).animate({width: '232px', height: '320px'}, '1000');
  });
  $('img').mouseleave(function() {
    $(this).animate({width: '212px', height: '300px'}, '1000');
  });

  $(document).on('click', 'img', function(){
    //number for each house
    var hnum = $(this).attr("id");
    console.log(hnum);
    $.get("http://www.anapioficeandfire.com/api/houses/"+hnum, function(res){
      console.log("Name: ",res.name);
      console.log("Words: ", res.words);
      console.log("Titles: ", res.titles);

      $('.house_info').html("<h3>"+res.name+"</h3></p>Words: "+res.words+"</p><p>Titles: "+res.titles+"</p>")

    }, "json");


  })

});
