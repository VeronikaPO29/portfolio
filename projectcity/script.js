let condition = true;
let start = 0;
let end = 0;

function forward(){
    anime({
        targets: '.menu-small',
        translateX: ['-100%', '0'],
        easing: 'easeInOutQuad',
        direction: 'alternate',
        duration: 1000,
        loop: false
     });
     condition = false;
}

function backward(){
    anime({
        targets: '.menu-small',
        translateX: ['0', '-100%'],
        easing: 'easeInOutQuad',
        direction: 'alternate',
        duration: 1000,
        loop: false
     });
     condition = true; 
}

$('.menu_small_icon').click(function(){
if (condition){
    forward();
}else{
    backward();
}
});

$(".container").on("touchstart", function(event){
start = event.originalEvent.touches[0].pageX;
});

$(".container").on("touchend", function(event){
    end = event.originalEvent.changedTouches[0].pageX;
    if(end - start >= 100 && condition){
        forward();
    } else if(start - end >= 100 && !condition){
        backward();
    }
});


        function toggleMenu() {
            if (condition) {
                openMenu();
            } else {
                closeMenu();
            }
        }
    
function updateClock(){
    var now = new Date();
    var hours = now.getHours().toString().padStart(2,'0');
    var minutes = now.getMinutes().toString().padStart(2,'0');
    var seconds = now.getSeconds().toString().padStart(2,'0');
    var timeString = hours + ":" + minutes + ":" + seconds;
    document.getElementById('clock').textContent = timeString;
}    

setInterval(updateClock, 1000);
updateClock();

$('.carousel').slick({
    centerMode: true,
    centerPadding: '60px',
    prevArrow: '<img src="img/left arrow.png" class="hhh">',
    nextArrow: '<img src="img/right arrow .png" class="hhh">',
    slidesToShow: 3,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '40px',
          slidesToShow: 3
        }
      },
      {
        breakpoint: 480,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '40px',
          slidesToShow: 1
        }
      }
    ]
  });
  