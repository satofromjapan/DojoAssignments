$(document).ready(function(){
  //Adding images to the page dynamically
  for(var i = 1; i <= 151; i++){
    $(".pokemon").append("<img src='http://pokeapi.co/media/img/" + i + ".png' id="+i+">")
  }
  //When the Pokemon image is clicked...
  $(document).on("click", "img", function(){
    // console.log("it's working!");
    var pnum = $(this).attr("id"); //holds numerical value for each pokemon clicked from their id tag
    // console.log(pnum);

    //API call to pokeapi to get info on clicked pokemon
    $.get("http://pokeapi.co/api/v1/pokemon/"+ pnum+"/", function(res){
      var name = res.name;
      var height = res.height;
      var weight = res.weight;
      // for(var i = 0; i < res.types.length; i++) {
        // console.log(res.name);
        var type1 = res.types[0].name;

        //if the pokemon only has 1 type
        if(res.types.length == 1){

          $(".info").html("<h2>"+name+"</h2>" + "<img src='http://pokeapi.co/media/img/" + pnum + ".png'  id='deximg'><h5>Types</h5><ul><li>"+type1+"</li></ul><h5>Height</h5><p>"+height+"</p><h5>Weight</h5><p>"+weight+"</p>");
        }

        //if the pokemon has more than 1 type
        else {
          var type2 = res.types[1].name;
          $(".info").html("<h2>"+name+"</h2>" + "<img src='http://pokeapi.co/media/img/" + pnum + ".png'  id='deximg'><h5>Types</h5><ul><li>"+type1+"</li><li>"+type2+"</li></ul><h5>Height</h5><p>"+height+"</p><h5>Weight</h5><p>"+weight+"</p>");

        }

        console.log("name:",name,"height:", height, "weight", weight,"type1", type1, "type2", type2);
      // }
    }, "json");

    // $(".info").append("<h3>"+res.name+"</h3>")
  })

})
