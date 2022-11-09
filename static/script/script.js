function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

$("#dark-mode, #dark-mode-sidebar").click(function(){
    $("body, .form-control, input").toggleClass("dark-mode");
    $("footer").toggleClass("dark-mode-footer");
    $('header').toggleClass("dm-header");
    $('nav').toggleClass("navbar-dark");
    $('main').toggleClass("dm-main");
    $(".wrapper").toggleClass("dm-wrapper");
    $(".card, .card-body").toggleClass("dm-card");
    $("#article h5, h3, .panel").toggleClass("dm-text");
    $(".btn-light").toggleClass("btn-dark");
    $(".modal-content").toggleClass("dm-md-content");
});

$("#registr-sidebar, #registr").click(function() {
  $("#myModal").css("display","block",closeNav());
});

$("#button_signup").click(function(){
    if ($("#inputLogin").val() == "" || $("#inputPassword").val() == "") {
      $('#danger').css("visibility" ,'visible');
      $("#danger p").text("Enter login or password");
      setTimeout(function() {
        $('#danger').css("visibility", "hidden")}, 2000);
    }
    else{
      $("#inputLogin").val("");
      $("#inputPassword").val("");
      $('#success').css("visibility" ,'visible');
      $("#success p").text("You have logged in");
      setTimeout(function() {
        $('#success').css("visibility", "hidden")}, 2000);
      $("#myModal").css("display","none");
      var audio_send = new Audio('sound/sound_send.wav')
      audio_send.play();
    }
});

$("#button_reg").click(function(){
    if ($("#regLogin").val() == "" || $("#regPassword").val() == "" || $("#retRegPassword").val() == "" || $("#regEmail").val() == "") {
      $('#danger').css("visibility" ,'visible');
      $("#danger p").text("Fill in all the fields");
      setTimeout(function() {
        $('#danger').css("visibility", "hidden")}, 2000);
    }
    else if ($("#regPassword").val() != $("#retRegPassword").val()) {
      $('#danger').css("visibility" ,'visible');
      $("#danger p").text("The repeated password was entered incorrectly.");
      setTimeout(function() {
        $('#danger').css("visibility", "hidden")}, 2000);
    }
    else{
      $("#regLogin").val("");
      $("#regEmail").val("");
      $("#regPassword").val("");
      $("#retRegPassword").val("");
      $('#success').css("visibility" ,'visible');
      $("#success p").text("Registration was successful!!!");
      setTimeout(function() {
        $('#success').css("visibility", "hidden")}, 2000);
      $("#myModal").css("display","none");
      var audio_send = new Audio('sound/sound_send.wav')
      audio_send.play();
    }
});

$("#button-toRegistr").click(function() {
  $(".sign-up").css("display","none");
  $(".form-registration").css("display","block");
});

$("#button-Auth").click(function() {
  $(".form-registration").css("display","none");
  $(".sign-up").css("display","block");
});



var span = document.getElementsByClassName("close")[0];
var modal = document.getElementById("myModal");

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(ev) {
  if (ev.target == modal) {
    modal.style.display = "none";
  }
}

//modal contenr

//Sidebar
const icons = document.querySelectorAll('.icon');

let i = 0;

function clickNavBtn() {
  icons.forEach (icon => {
    icon.addEventListener('click', () => {
      icon.classList.toggle("open");
      if (i == 0){
        openNav();
        i = 1;
      }
      else{
        closeNav();
        i = 0;
      }
  });
  });
}

//button from footer
let nameEmail = document.getElementById('exampleFormControlInput1');
let btn = document.getElementById('button_send');


function buttonClick(){

if (nameEmail.value == ""){
  buttonMouseout();
  var audio_error = new Audio('sound/sound_error.wav')
  audio_error.play();
  document.querySelector('#danger').style.visibility = 'visible';
  setTimeout(function() {
  document.querySelector('#danger').style.visibility = "hidden"; }, 2000);

}
else{
    nameEmail.value="";
    var audio_send = new Audio('sound/sound_send.wav')
    audio_send.play();
    document.getElementById('exampleFormControlTextarea1').value="";
    document.querySelector('#success').style.visibility = 'visible';
    setTimeout(function() {
    document.querySelector('#success').style.visibility = "hidden";}, 2000);

}
}

function buttonMouseover(){
    if (nameEmail.value == ""){
      document.querySelector('#warning').style.visibility = 'visible';}
}
function buttonMouseout(){
      document.querySelector('#warning').style.visibility = 'hidden';
}
btn.addEventListener('click', buttonClick);
btn.addEventListener('mouseover', buttonMouseover);
btn.addEventListener('mouseout', buttonMouseout);


document.addEventListener('keypress', (e) => {
  switch (e.key) {
    case "#":
      document.location.href = "index.html";
      break;
    case "$":
      document.location.href = "index_news.html";
      break;
    case "%":
      document.location.href = "index_dev.html";
      break;
    case "^":
      document.location.href = "index_games.html";
      break;
    case "&":
      document.location.href = "index_movie.html";
      break;
  }
});
