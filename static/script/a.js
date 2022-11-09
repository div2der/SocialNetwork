var arrayArticle = [];

arrayArticle[0] = {
  title: "&#34;Problem 2022&#34;: Microsoft Exchange servers are not delivering mail",
  data: "<em>2/01/2021 </em>",
  type: "World, IT",
  image: "image/news/n_2.png",
  subtitle: "What is the main problem?",
  article: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi finibus quam vel leo auctor, congue feugiat risus eleifend." +
  " Morbi ac tempor orci. Nullam dignissim id nisi vitae volutpat. Aenean varius cursus libero, et ultricies orci tincidunt non. Etiam id egestas enim." +
   "Etiam quis auctor quam. Nam faucibus risus et molestie pretium. Integer ornare ex vel risus posuere cursus." + "<br> <br>" +
   " In quis elit sit amet ex convallis lobortis vel eu velit. Praesent tincidunt, erat a bibendum convallis, purus mauris viverra diam, ac ornare velit risus ut nunc. In condimentum vulputate lacinia. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut vel condimentum quam. Donec vitae enim a elit commodo molestie. Vivamus tellus nisi, cursus nec tellus sed, ullamcorper faucibus lectus. Suspendisse sit amet convallis velit. Integer sapien mi, congue vitae tincidunt nec, finibus vel magna.",
  inputSubtitle: function () {
      return this.type + " &#176; " + this.data;
  }
};

arrayArticle[2] = {
  title: "Epic Games users can pick up the Tomb Raider: Trilogy collection for free",
  data: "<em>30/12/2021 </em>",
  type: "Free Games",
  image: "image/game/g_!.jpg",
  subtitle: "How did the players react to this?",
  article: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi finibus quam vel leo auctor, congue feugiat risus eleifend." +
  " Morbi ac tempor orci. Nullam dignissim id nisi vitae volutpat. Aenean varius cursus libero, et ultricies orci tincidunt non. Etiam id egestas enim." +
   "Etiam quis auctor quam. Nam faucibus risus et molestie pretium. Integer ornare ex vel risus posuere cursus." + "<br> <br>" +
   " In quis elit sit amet ex convallis lobortis vel eu velit. Praesent tincidunt, erat a bibendum convallis, purus mauris viverra diam, ac ornare velit risus ut nunc. In condimentum vulputate lacinia. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut vel condimentum quam. Donec vitae enim a elit commodo molestie. Vivamus tellus nisi, cursus nec tellus sed, ullamcorper faucibus lectus. Suspendisse sit amet convallis velit. Integer sapien mi, congue vitae tincidunt nec, finibus vel magna.",
  inputSubtitle: function () {
      return this.type + " &#176; " + this.data;
  }
};

arrayArticle[1] = {
  title: "Metacritic rated the best films",
  data: "<em>31/12/2021 </em>",
  type: "Rating, 2021",
  image: "image/movie/m_1.png",
  subtitle: "The results of the critics' assessment are surprising",
  article: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi finibus quam vel leo auctor, congue feugiat risus eleifend." +
  " Morbi ac tempor orci. Nullam dignissim id nisi vitae volutpat. Aenean varius cursus libero, et ultricies orci tincidunt non. Etiam id egestas enim." +
   "Etiam quis auctor quam. Nam faucibus risus et molestie pretium. Integer ornare ex vel risus posuere cursus." + "<br> <br>" +
   " In quis elit sit amet ex convallis lobortis vel eu velit. Praesent tincidunt, erat a bibendum convallis, purus mauris viverra diam, ac ornare velit risus ut nunc. In condimentum vulputate lacinia. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut vel condimentum quam. Donec vitae enim a elit commodo molestie. Vivamus tellus nisi, cursus nec tellus sed, ullamcorper faucibus lectus. Suspendisse sit amet convallis velit. Integer sapien mi, congue vitae tincidunt nec, finibus vel magna.",
  inputSubtitle: function () {
      return this.type + " &#176; " + this.data;
  }
};


var imageHTML = document.getElementById("myImage");
var titleA = document.getElementById("articleTitle");
var typeA = document.getElementById("articleType");
var subTitle = document.getElementById("SubTitle");
var textA = document.getElementById("articleText");
var n = 0;

function offArticle() {
  document.querySelector('.block-1').style.display = "block";
  document.querySelector('.block-2').style.display = "none";
  document.location.href = "#top";
}

function onArticle() {
  document.querySelector('.block-1').style.display = "none";
  document.querySelector('.block-2').style.display = "block";
  document.location.href = "#top";
}

function openArticle(number){
    n = 0;
    imageHTML.src = arrayArticle[number].image;
    titleA.innerHTML = arrayArticle[number].title;
    typeA.innerHTML = arrayArticle[number].inputSubtitle();
    subTitle.innerHTML = arrayArticle[number].subtitle;
    textA.innerHTML = arrayArticle[number].article;
    n = number;
    onArticle();
}

function nextArticle() {
  document.location.href = "#top";
  if (n < arrayArticle.length - 1){
    n++;
    imageHTML.src = arrayArticle[n].image;
    titleA.innerHTML = arrayArticle[n].title;
    typeA.innerHTML = arrayArticle[n].inputSubtitle();
    subTitle.innerHTML = arrayArticle[n].subtitle;
    textA.innerHTML = arrayArticle[n].article;
  }
}
function backArticle() {
  document.location.href = "#top";
  if (n > 0){
    n--;
    imageHTML.src = arrayArticle[n].image;
    titleA.innerHTML = arrayArticle[n].title;
    typeA.innerHTML = arrayArticle[n].inputSubtitle();
    subTitle.innerHTML = arrayArticle[n].subtitle;
    textA.innerHTML = arrayArticle[n].article;
  }
}

document.addEventListener('keypress', (e) => {
  switch (e.key) {
    case ")":
      nextArticle();
      break;
    case "(":
      backArticle();
      break;
  }
});
