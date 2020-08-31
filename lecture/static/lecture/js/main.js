function loadContent(url) {
    $('#main-content').hide();
    $('#main-content').load(url).hide().fadeIn('slow');
}

$(function () {
    $('.nav-menu').on('click', function (e) {
        e.preventDefault();
        var href = this.href;
        var $this = $(this);
        loadContent(href);
        history.pushState('', $this.find('span').innerText, href);
    });

    window.onpopstate = function () {
        var href = location.href;
        loadContent(href);
    };
});