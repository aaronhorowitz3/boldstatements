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
