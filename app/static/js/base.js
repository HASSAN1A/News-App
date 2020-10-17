$(document).ready(function() {
  // Transition effect for navbar 
  
  $(window).scroll(function() {
    // checks if window is scrolled more than 500px, adds/removes solid class
    if($(this).scrollTop() > 200) { 
        $('.navbar').addClass('solid');
    } else {
        $('.navbar').removeClass('solid');
    }
  });
});
const blurryImageLoad = new BlurryImageLoad();
blurryImageLoad.load();
window.onload = () => {
  document.querySelector(".header").classList.add("header-bg");
};

