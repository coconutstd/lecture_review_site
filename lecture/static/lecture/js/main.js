function loadContent(url) {
    $('#main-content').load(url).hide().fadeIn('slow');
}

$(function () {
    $('.nav-link').on('click', function (e) {
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