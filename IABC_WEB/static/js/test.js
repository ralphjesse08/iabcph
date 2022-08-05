$(document).ready(function () {
	var $TABLE = $('#table');

	$('.table-add').click(function() {
		var $clone = $TABLE.find('tr.hide').clone(true).removeClass('hide').addClass('new');
		
		$TABLE.find('table').append($clone);
	});
	

	$('.table-remove').click(function() {
		$(this).parents('tr').detach();
	});

	$('.table-up').click(function() {
		var $row = $(this).parents('tr');
		if ($row.index() === 1) return;
		$row.prev().before($row.get(0));
	});

	$('.table-down').click(function() {
		var $row = $(this).parents('tr');
		$row.next().after($row.get(0));
	});


	var status = $('.status'),
	    inputs = $('.table input, .table textarea, .table select');

	status.change(function() {
		if (status.val() == "") {
			// inputs.css("box-shadow", "none");
			inputs.removeClass();
		}

		if (status.val() == "Complete") {
			// inputs.css("box-shadow", "0 -5px 0 0 green inset");
			inputs.removeClass();
			inputs.addClass('complete');
		}

		if (status.val() == "Questions") {
			// inputs.css("box-shadow", "0 -5px 0 0 orange inset");
			inputs.removeClass();
			inputs.addClass('questions');
		}

		if (status.val() == "Incomplete") {
			// inputs.css("box-shadow", "0 -5px 0 0 red inset");
			inputs.removeClass();
			inputs.addClass('incomplete');
		}

		if (status.val() == "Errors") {
			// inputs.css("box-shadow", "0 -5px 0 0 #fff200 inset");
			inputs.removeClass();
			inputs.addClass('errors');
		}
	});

	$('.clear-table').click(function() {
		$('input, textarea, select').val('');
		inputs.css("box-shadow", "none");
	});

	$('.show-email').click(function () {
		$('.email-inputs').toggleClass('show');
		if ($('.email-inputs').hasClass('show')) {
			$('.show-email').html('<span class="glyphicon glyphicon-envelope"></span> Hide Email');
		} else {
			$('.show-email').html('<span class="glyphicon glyphicon-envelope"></span> Show Email');
		}
	});

});





// SCREENSHOTS
// Created by STRd6
// MIT License
// jquery.paste_image_reader.js
(function($) {
  var defaults;
  $.event.fix = (function(originalFix) {
    return function(event) {
      event = originalFix.apply(this, arguments);
      if (event.type.indexOf('copy') === 0 || event.type.indexOf('paste') === 0) {
        event.clipboardData = event.originalEvent.clipboardData;
      }
      return event;
    };
  })($.event.fix);
  defaults = {
    callback: $.noop,
    matchType: /image.*/
  };
  return $.fn.pasteImageReader = function(options) {
    if (typeof options === "function") {
      options = {
        callback: options
      };
    }
    options = $.extend({}, defaults, options);
    return this.each(function() {
      var $this, element;
      element = this;
      $this = $(this);
      return $this.bind('paste', function(event) {
        var clipboardData, found;
        found = false;
        clipboardData = event.clipboardData;
        return Array.prototype.forEach.call(clipboardData.types, function(type, i) {
          var file, reader;
          if (found) {
            return;
          }
          if (type.match(options.matchType) || clipboardData.items[i].type.match(options.matchType)) {
            file = clipboardData.items[i].getAsFile();
            reader = new FileReader();
            reader.onload = function(evt) {
              return options.callback.call(element, {
                dataURL: evt.target.result,
                event: evt,
                file: file,
                name: file.name
              });
            };
            reader.readAsDataURL(file);
            snapshoot();
            return found = true;
          }
        });
      });
    });
  };
})(jQuery);



$("html").pasteImageReader(function(results) {
  var dataURL, filename;
  filename = results.filename, dataURL = results.dataURL;
  $data.text(dataURL);
  $size.val(results.file.size);
  $type.val(results.file.type);
  $test.attr('href', dataURL);
  var img = document.createElement('img');
  img.src= dataURL;
  var w = img.width;
  var h = img.height;
  $width.val(w)
  $height.val(h);
  return $(".active").css({
    backgroundImage: "url(" + dataURL + ")"
  }).data({'width':w, 'height':h});
});

var $data, $size, $type, $test, $width, $height;
$(function() {
  $data = $('.data');
  $size = $('.size');
  $type = $('.type');
  $test = $('#test');
  $width = $('#width');
  $height = $('#height');
  $('.target').on('click', function() {
    var $this = $(this);
    var bi = $this.css('background-image');
    if (bi!='none') {
        $data.text(bi.substr(4,bi.length-6));
    }
                    
                    
    $('.active').removeClass('active');
    $this.addClass('active');
    
    $this.toggleClass('contain');
    
    $width.val($this.data('width'));
    $height.val($this.data('height'));
    if ($this.hasClass('contain')) {
      $this.css({'width':$this.data('width'), 'height':$this.data('height'), 'z-index':'10'})
    } else {
      $this.css({'width':'', 'height':'', 'z-index':''})
    }
    
  })
})