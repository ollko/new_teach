function ShowAnswer(){
  var answer;
  answer=$(this).next().text();
  $(this).val(answer);
  $(this).removeClass( "green-right-answer red-wrong-answer answer" ).addClass('darker');  
  $(this).parent().siblings().children().addClass('sign-out');

};

$('#show-answer').on('click',function() {
  $('.answer').each(ShowAnswer);
  $('#show-answer').remove();
  $('#pass_again').removeClass("col-md-6").addClass("col-md-12");
  
});

function handler( event ) {
  var target = $( event.target );
  if ( target.is( "li" ) ){
    target.children().toggle();
  }
}
// $( "ul" ).click( handler ).find( "ul" ).hide();