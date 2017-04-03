function startTime() {
  var today=new Date();
  var h=today.getHours();
  var m=today.getMinutes();
  var s=today.getSeconds();
  var ampm = "";
  m = checkTime(m);

  if (h > 12) {
    h = h - 12;
    ampm = " PM";
  } else if (h == 12){
      h = 12;
    ampm = " AM";
  } else if (h < 12){
      ampm = " AM";
  } else {
      ampm = "PM";
  };

if(h==0) {
  h=12;
}

  document.getElementById('display').innerHTML = h+":"+m+ampm;
  var t = setTimeout(function(){startTime()},500);
}

function checkTime(i) {
if (i <10) {i = "0" + i};
return i;
}

function startDate() {
var d = new Date();
var days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
document.getElementById("date").innerHTML = days[d.getDay()]+" | "+[d.getMonth()+1]+"/"+d.getDate()+"/"+d.getFullYear();
}

$(document).ready(function() {



  //Search function
  $(document).on('click', '#search', function() {
    // console.log("I was clicked!")
    var city = $('input').val();
    console.log(city);
    $.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b47b786a8f42c25d462f9beae847a42f", function(res){
      var ktemp = res.main.temp;
      // console.log(ktemp);
      var ctemp = (ktemp-273.15).toFixed(2);
      var ftemp = ((ktemp*(9/5))-459.67).toFixed(2);
      // console.log(ctemp);

      //changing background image depending on the temperature
      if(ftemp > 90) {
        $('body').css('background-image','url(http://pic1.win4000.com/wallpaper/5/5670d8d50ec41.jpg)')
      }

      else if(ftemp > 80 & ftemp < 90) {
        $('body').css('background-image','url(http://reso3.yiihuu.com/img_1020053.jpg)');
      }

      else if(ftemp > 70 & ftemp < 80) {
        $('body').css('background-image','url(http://pic1.win4000.com/wallpaper/5/57a823a8f0511.jpg)');
      }

      else if(ftemp > 60 & ftemp < 70) {
        $('body').css('background-image','url(http://g.ichang8.com/uploads/img1/20161112/5825f1ce682b2.jpg)');
      }

      else if(ftemp > 50 & ftemp < 60) {
        $('body').css('background-image','url(http://img2.cache.netease.com/photo/0031/2013-06-07/90NQN4FS43UD0031.jpg)');
      }

      else {
        $('body').css('background-image', 'url(http://www.bz55.com/uploads/allimg/140709/1-140FZ92230.jpg)')
      }

      $('.weather_display').html("<div class='temp_display'><h2>"+city+"</h2><p>Temperature: " + ftemp + " F&deg;</p></div>");

      return false;

    }, "json");



    //Add functionality for changing the background-image depending on the temperature



  });
  //Searching input with "enter" key
  $('input').keyup(function(event){
    if(event.keyCode == 13){
      $("#search").click();
    }
  });
});
