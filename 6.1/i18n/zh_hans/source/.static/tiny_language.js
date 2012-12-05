function setup_selection($selector, $options) {
        $options.hide();
        $selector.click(function() {
            $options.toggle();
            return false;
        });
        $(document).keyup(function(e) {
            if (e.keyCode == 27) {
                $options.hide();
            }
        });
        $selector.add($options).mouseenter(function() {
            $options.show();
            clearTimeout($options.data('timeoutId'));
        }).mouseleave(function() {
            var timeoutId = setTimeout(function(){ $options.hide(); }, 500);
            $options.data('timeoutId', timeoutId);
        });
}


if (/openerp\.com$/.test(document.domain)) {
    $(document).ready(function() {
        $('.openerp_website').show();
        setup_selection($('#change_language'),$('#language_links'))
        setup_selection($('#change_version'),$('#version_links'))
    });
}
