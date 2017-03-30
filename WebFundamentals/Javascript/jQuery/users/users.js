$(document).ready(function(){
  $("form").submit(function(){
    $("tbody").append("<tr></tr>")
    var first_name = $("#first_name").val();
    var last_name = $("#last_name").val();
    var email = $("#email").val();
    var contact = $("#contact").val();
    //console.log(first_name);

    $("tbody").children("tr:last").append("<td>"+first_name+"</td>")
    $("tbody").children("tr:last").append("<td>"+last_name+"</td>")
    $("tbody").children("tr:last").append("<td>"+email+"</td>")
    $("tbody").children("tr:last").append("<td>"+contact+"</td>")

    $("#first_name, #last_name, #email, #contact").val("");

    return false;
  })
})
