jQuery(document).ready(function() {
 
    $('.dismiss, .overlay').on('click', function() {
        $('.sidebar').removeClass('active');
        $('.overlay').removeClass('active');
        $('.open-menu').show();
    });
 
    $('.open-menu').on('click', function(e) {
        e.preventDefault();
        $('.sidebar').addClass('active');
        $('.overlay').addClass('active');
        $('.open-menu').hide();
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