// Показывает правильные ответы на странице для зарегистрированного пользователя
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
  $('#next-test').children().css('display','block');
});


$('#show-answer-anonymous').on('click',function(){
  $('.answer').each(ShowAnswer);
   
});

// Проверяет ответы незарегистрированного пользователя с помощью цвета
//(зеленый - верно, красный не верно):
function CheckAnswer(){
  var anonymousAnswer, rightAnswer;
  var ogeModal;
  anonymousAnswer=$(this).val().toLowerCase();
  console.log('anonymousAnswer=',anonymousAnswer)
  rightAnswer=$(this).siblings('.right-answer').text();
  console.log('rightAnswer=',rightAnswer)
  if (anonymousAnswer===rightAnswer){

    $(this).addClass('green-right-answer ');
    }
  else {
      $(this).addClass('red-wrong-answer ');
      score=2;
    }
};
var score;
$('#check-answer').on('click',function() {
  score=1;
  $('.anonymous-answer').each(CheckAnswer);
  if (score===1){
  // правильный ответ
    $('#check-answer').remove();
    $('#next-test').children().css('display','block');
  };
  
  if (score===2){
  // ответ с ошибками
    $('#show-answer').css('display','block');
    $('#check-answer').remove();
    $('#pass-test-again').css('display','block');
  };  
});

// После клика по input окну если есть текст, он исчезает, 


$( 'input.anonymous-answer' ).on( 'select click', function( evt ) {
  if ($(evt.target).val()!==0){
    $(evt.target).val('');
  };

// удаляются классы 'red-wrong-answer green-right-answer':
  $( evt.target ).removeClass( 'red-wrong-answer green-right-answer' );
  
});

//Показывает/скрывает подменю в левой колонке:

function handler( event ) {
  var target = $( event.target );
  if ( target.is( "li.oge_menu" ) ){
    target.children().toggle();
  };
};
$( "ul.oge_menu" ).click( handler ).find( "ul.oge_menu" ).hide();

