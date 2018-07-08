$(document).ready(function() {
   console.log('faaaack')

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
