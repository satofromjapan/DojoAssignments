function table(){
  var value = 0;
  var string = "";
  for(var i = 1; i <= 12; i++) {
    for(var j = 1; j <= 12; j++){
      value = i*j;
      string = string + " " + value.toString();
    }
    console.log(string);
    string = "";
  }


}


// arr =[1,2,3,4,5,6,7,8,9,10,11,12]
