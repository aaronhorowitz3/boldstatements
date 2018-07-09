$(document).ready(function() {
   console.log('faaaack')

   $.sortByDate = function(elements, order) {
      var arr = [];
      elements.each(function() {
         var obj = {},
            $el = $(this),
            time = $el.find(".prediction-date").text(),
            date = new Date($.trim(time)),
            timestamp = date.getTime();

            obj.html = $el[0].outerHTML;
            obj.time = timestamp;
            arr.push(obj);
      });

      var sorted = arr.sort(function(a,b) {
         if(order == "ASC") {
            return a.time > b.time;
         } else {
            return b.time > a.time;
         }
      });
      return sorted;
   };

   $(function() {
		var $newer = $("#newer"),
			$older = $("#older"),
			$content = $("#sorted-feed"),
			$elements = $(".in-sort-order");

			$newer.click(function() {
				var elements = $.sortByDate($elements, "DESC");
				var html = "";
				for(var i = 0; i < elements.length; ++i) {
					html += elements[i].html;
				}
				$content[0].innerHTML = html;
				// $(this).addClass("selected").
				// siblings().
				// removeClass("selected");
				// return false;

			});

			$older.click(function() {
				var elements = $.sortByDate( $elements, "ASC" );
				var html = "";
				for( var i = 0; i < elements.length; ++i ) {
					html += elements[i].html;
				}
				$content[0].innerHTML = html;
				// $( this ).addClass( "selected" ).
				// siblings().
				// removeClass( "selected" );
				// return false;

			});
	});




   let statementContainer = $('#single-statement')
   let trueRadio = $('#true-radio')
   let falseRadio = $('#false-radio')

   trueRadio.change(function() {
      statementContainer.addClass('true')
      statementContainer.removeClass('false')
   })

   falseRadio.change(function() {
      statementContainer.addClass('false')
      statementContainer.removeClass('true')
   })


})
