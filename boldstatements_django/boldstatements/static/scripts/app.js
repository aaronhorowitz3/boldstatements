$(document).ready(function() {
   console.log('faaaack')

   let newestFirst = $('#sorted-feed')
   let oldestFirst = $('#reverse-sorted-feed')
   let newer = $('#newer')
   let older = $('#older')

   older.click(function() {
      newestFirst.addClass('hidden')
      oldestFirst.removeClass('hidden')
      older.addClass('selected')
      newer.removeClass('selected')
   })

   newer.click(function() {
      newestFirst.removeClass('hidden')
      oldestFirst.addClass('hidden')
      older.removeClass('selected')
      newer.addClass('selected')
   })

   // let singleStatement = $('#single-statement')
   // let userConf = $('#user-conf')
   // 
   // if userConf.innerHTML === "True!" function() {
   //    singleStatement.addClass("true")
   //    singleStatement.removeClass("false")
   // }
   //
   // if (userConf.innerHTML === "False!") function() {
   //    singleStatement.addClass("false")
   //    singleStatement.removeClass("true")
   // }

})
