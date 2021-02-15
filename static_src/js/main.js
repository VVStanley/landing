$(document).ready(function () {
    svg4everybody({});

    var phoneMask = function () {
        $("input[type=tel]").mask("+7 (999) 999-99-99");
    };

    phoneMask();

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    TweenMax.to('.overlay__title', 2, {
        opacity: 0,
        y: -60,
        easy: Expo.easyInOut
    });
    TweenMax.to('.overlay', 1, {
        delay: 1,
        top: "-100%",
        easy: Expo.easyInOut
    });
    TweenMax.from('.header-center__logo', 1, {
        delay: 1.5,
        opacity: 0,
        y: 20,
        easy: Expo.easyInOut
    });
    TweenMax.from('.header-center__phone', 1, {
        delay: 1.8,
        opacity: 0,
        y: 20,
        easy: Expo.easyInOut
    });
    TweenMax.from('.header-center__callback', 1, {
        delay: 2,
        opacity: 0,
        y: 20,
        easy: Expo.easyInOut
    });
    TweenMax.from('.right', 1, {
        delay: 2,
        opacity: 0,
        y: 20,
        easy: Expo.easyInOut
    });
    TweenMax.from('.one-title.one__title', 1, {
        delay: 2.2,
        opacity: 0,
        y: 20,
        easy: Expo.easyInOut
    });
    TweenMax.from('.one__desc', 1, {
        delay: 2.4,
        opacity: 0,
        y: 20,
        easy: Expo.easyInOut
    });
    TweenMax.from('.one__button', 1, {
        delay: 3,
        opacity: 0,
        y: 20,
        easy: Expo.easyInOut
    });
    TweenMax.staggerFrom('.one_subtitle ul li', 1, {
        delay: 2.5, opacity: 0, y: 20, easy: Expo.easyInOut
    }, 0.2)

    $(".one__button .btn, .price-block .btn, .header-center__callback .btn").click(function (e) {
        e.preventDefault();
        item = $(this).data("item");
        subject = $(this).data("subject");

        $(".form__title").text(subject)
        $(".form input[name='item']").val(item);
        $(".form input[name='subject']").val(subject);
        this.blur();
        $(".form").modal({
            fadeDuration: 100
        });

    });

    $("form").submit(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "sendEmail/",
            data: $(this).serialize()
        }).done(function (responce) {
            console.log(responce)
            if (responce.status == true) {
                swal({
                    title: 'Спасибо за обращение!',
                    text: "Мы вам перезвоним в ближайшее время!",
                    type: 'success',
                    timer: 5000
                });
            } else {
                swal({
                    title: 'Что-то пошло не так!',
                    text: "Попробуйте заполнить форму еще раз или позвоните по номеру в шапке сайта!",
                    type: 'success',
                    timer: 5000
                });
            }
        });
    });


    $('.portfolio-block').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true
                }
            }]
    });
});

$(function () {
    var
        // ACTIVITY INDICATOR

        activityIndicatorOn = function () {
            $('<div id="imagelightbox-loading"><div></div></div>').appendTo('body');
        },
        activityIndicatorOff = function () {
            $('#imagelightbox-loading').remove();
        },


        // OVERLAY

        overlayOn = function () {
            $('<div id="imagelightbox-overlay"></div>').appendTo('body');
        },
        overlayOff = function () {
            $('#imagelightbox-overlay').remove();
        },


        // CLOSE BUTTON

        closeButtonOn = function (instance) {
            $('<button type="button" id="imagelightbox-close" title="Close"></button>').appendTo('body').on('click touchend', function () { $(this).remove(); instance.quitImageLightbox(); return false; });
        },
        closeButtonOff = function () {
            $('#imagelightbox-close').remove();
        },


        // CAPTION

        captionOn = function () {
            var description = $('a[href="' + $('#imagelightbox').attr('src') + '"] img').attr('alt');
            if (description.length > 0)
                $('<div id="imagelightbox-caption">' + description + '</div>').appendTo('body');
        },
        captionOff = function () {
            $('#imagelightbox-caption').remove();
        },


        // NAVIGATION

        navigationOn = function (instance, selector) {
            var images = $(selector);
            if (images.length) {
                var nav = $('<div id="imagelightbox-nav"></div>');
                for (var i = 0; i < images.length; i++)
                    nav.append('<button type="button"></button>');

                nav.appendTo('body');
                nav.on('click touchend', function () { return false; });

                var navItems = nav.find('button');
                navItems.on('click touchend', function () {
                    var $this = $(this);
                    if (images.eq($this.index()).attr('href') != $('#imagelightbox').attr('src'))
                        instance.switchImageLightbox($this.index());

                    navItems.removeClass('active');
                    navItems.eq($this.index()).addClass('active');

                    return false;
                })
                    .on('touchend', function () { return false; });
            }
        },
        navigationUpdate = function (selector) {
            var items = $('#imagelightbox-nav button');
            items.removeClass('active');
            items.eq($(selector).filter('[href="' + $('#imagelightbox').attr('src') + '"]').index(selector)).addClass('active');
        },
        navigationOff = function () {
            $('#imagelightbox-nav').remove();
        },


        // ARROWS

        arrowsOn = function (instance, selector) {
            var $arrows = $('<button type="button" class="imagelightbox-arrow imagelightbox-arrow-left"></button><button type="button" class="imagelightbox-arrow imagelightbox-arrow-right"></button>');

            $arrows.appendTo('body');

            $arrows.on('click touchend', function (e) {
                e.preventDefault();

                var $this = $(this),
                    $target = $(selector + '[href="' + $('#imagelightbox').attr('src') + '"]'),
                    index = $target.index(selector);

                if ($this.hasClass('imagelightbox-arrow-left')) {
                    index = index - 1;
                    if (!$(selector).eq(index).length)
                        index = $(selector).length;
                }
                else {
                    index = index + 1;
                    if (!$(selector).eq(index).length)
                        index = 0;
                }

                instance.switchImageLightbox(index);
                return false;
            });
        },
        arrowsOff = function () {
            $('.imagelightbox-arrow').remove();
        };

    //  WITH ACTIVITY INDICATION

    var instanceC = $('a[data-imagelightbox="c"]').imageLightbox(
        {
            quitOnDocClick: false,
            onStart: function () { closeButtonOn(instanceC); },
            onEnd: function () { closeButtonOff(); activityIndicatorOff(); },
            onLoadStart: function () { activityIndicatorOn(); },
            onLoadEnd: function () { activityIndicatorOff(); }
        });
});