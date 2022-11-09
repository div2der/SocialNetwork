var creator = [];

creator[0] = {
  firstName: "Ilya",
  surname: "Rogov",
  age: 18,
  place: "Nur-Sultan",
  fullName: function() {
      return this.firstName + " " + this.surname;
  },
  phrasePerson: function() {
      return "The God of this site";
  },
  aboutMe: function () {
      return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi finibus quam vel leo auctor, congue feugiat risus eleifend." +
        " Morbi ac tempor orci. Nullam dignissim id nisi vitae volutpat. Aenean varius cursus libero, et ultricies orci tincidunt non. Etiam id egestas enim.";
  },
  image: "image/photo_rec.jpg"
};
creator[1] = {
  firstName: "Ilya",
  surname: "Rogov",
  age: 18,
  place: "Nur-Sultan",
  fullName: function() {
      return this.firstName + " " + this.surname;
  },
  phrasePerson: function() {
      return "The God of this site";
  },
  aboutMe: function () {
      return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi finibus quam vel leo auctor, congue feugiat risus eleifend." +
        " Morbi ac tempor orci. Nullam dignissim id nisi vitae volutpat. Aenean varius cursus libero, et ultricies orci tincidunt non. Etiam id egestas enim.";
  },
  image: "image/photo_rec.jpg"
};

var hTitle = document.querySelector("#testimonials .pPost");
var hName = document.querySelector("#testimonials .pName");
var pText = document.querySelector("#testimonials .pText");
var img = document.querySelector("#testimonials img");

function God(num) {
  hTitle.innerHTML = creator[num].phrasePerson();
  hName.innerHTML = creator[num].fullName();
  pText.innerHTML = creator[num].aboutMe();
  img.src = creator[num].image;
}
