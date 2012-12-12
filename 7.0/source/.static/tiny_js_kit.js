
$(document).ready(function(){
  $('div.js-kit-comments').each(function(i, elem) {
    var jelem = $(elem);
    if (jelem.attr('permalink') != null) {
      jelem.css(
        {
          'position': 'static',
          'float': 'left',
          'top': '0px',
          'right': '0px',
          'width': '25%',
        }
      );
      jelem.after('<br />');
    }
  }
  );
});

