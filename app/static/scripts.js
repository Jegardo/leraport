jQuery(document).ready(function() {
 
    $('.dismiss, .overlay').on('click', function() {
        $('.sidebar').removeClass('active');
        $('.overlay').removeClass('active');
        $('.about').css("width","100vw")
        $('.about').css("left","0")
        $('.contact').css("width","100vw")
        $('.contact').css("left","0")
        $('.open-menu').show();
    });
 
    $('.open-menu').on('click', function(e) {
        e.preventDefault();
        $('.sidebar').toggleClass('active');
        $('.overlay').toggleClass('active');
        $('.about').toggleClass('split')
        $('.contact').toggleClass('split')
        $('.koubi').toggleClass('fa-bars fa-times')
        // close opened sub-menus
        $('.collapse.show').toggleClass('show');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
 
    $('.to-top a').on('click', function(e) {
        e.preventDefault();
        if($(window).scrollTop() != 0) {
            $('html, body').stop().animate({scrollTop: 0}, 1000);
        }
    });

    $('a.btn-customized-dark').on('click', function(e) {
        e.preventDefault();
        $('.sidebar').removeClass('light');
    });
 
    $('a.btn-customized-light').on('click', function(e) {
        e.preventDefault();
        $('.sidebar').addClass('light');
    });

    $('.section-container').waypoint(function(direction) {
        if (direction === 'down') {
            $('.menu-elements li').removeClass('active');
            $('.menu-elements a[href="#' + this.element.id + '"]').parents('li').addClass('active');
        }
    },
    {   
        offset: '0'
    });
 
    $('.section-container').waypoint(function(direction) {
        if (direction === 'up') {
         $('.menu-elements li').removeClass('active');
            $('.menu-elements a[href="#' + this.element.id + '"]').parents('li').addClass('active');
        }
    },
    {
        offset: '-5'
    });
 
});