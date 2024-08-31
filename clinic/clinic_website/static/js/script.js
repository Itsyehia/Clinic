

$(document).ready(function(){
    $('.feedback-slider').owlCarousel({
        loop: false,
        margin: 10,
        nav: true,
        items: 1,
        autoplay: true,
        navText: ["<i class = 'fas fa-arrow-left'></i>", "<i class = 'fas fa-arrow-right'></i>"]
    });

    // stop animation on resize
    let resizeTimer;
    $(window).resize(function(){
        $(document.body).addClass('resize-animation-stopper');
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            $(document.body).removeClass('resize-animation-stopper');
        }, 400);
    });

    $('.navbar-show-btn').click(function(){
        $('.navbar-box').addClass('navbar-box-show');
    });

    $('.navbar-hide-btn').click(function(){
        $('.navbar-box').removeClass("navbar-box-show");
    })
});


// burger menu
 const header = document.querySelector("header");

    // make footer sticky
    window.addEventListener("scroll", function(){
        header.classList.toggle("sticky" , this.window.scrollY > 0 );
    });
    let menu = document.querySelector('#menu-icon');
    let navmenu = document.querySelector('.navmenu');
    menu.onclick = () =>{
        menu.classList.toggle('bx-x');
        navmenu.classList.toggle('open');
    }


