// Показывает правильные ответы на странице для зарегистрированного пользователя
function ShowAnswer(){
  var answer;
  answer=$(this).next().text();
  $(this).val(answer);
  $(this).removeClass( "green-right-answer red-wrong-answer answer" ).addClass('darker');  


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


// function handler( event ) {
//   var target = $( event.target );
//   if ( target.is( "li.oge_menu" ) ){
//     target.children().toggle();
//   };
// };

// var urlString=window.location.toString();

// if (urlString.indexOf('/test18_26/')===-1){
//   $( "ul.oge_menu" ).click( handler ).find( "ul.oge_menu" ).hide();
// } else {
//   $( "ul.oge_menu" ).click( handler );
// }
//Проставляет номер задания в главной колонке:

window.onload = function () {
var t=$('li.darker').text();
console.log('text='+t);
var reg=/[0-9]/;
var testNumber=t.match(reg);
$('h3.test-header').append('<span> '+testNumber+'</span>');
};

//  ОГЭ МЕНЮ

function handler( event ) {
  var target = $( event.target );
  if ( target.is( "a.oge-test-type" ) ){
    $( ".breadcrumb" ).children().removeClass( "active" ).html('<a href="/oge/fipi/">ОГЭ</a>');
  $( ".breadcrumb" ).append( "<li class='active'>"+target.text()+"</li>" );
    target.siblings('.oge-test-type').toggle();
    target.next().toggle();
    target.toggle(); 

  };
};

function handler18_26( event ) {
  var target = $( event.target );
  if ( target.is( "a.oge-test-test" ) ){
    $( ".breadcrumb" ).find().last().removeClass( "active" ).html('<a href="#">Языковой материал</a>'); 
    $( ".breadcrumb" ).append( "<li class='active'>"+target.text()+"</li>" ); 
  };
};


window.onload = function () {
   var urlString=window.location.toString();
  if (urlString.indexOf('/test18_26/')===-1){

    // если /oge/fipi/
    $('.list-of-tests').hide();
    $( "a.oge-test-type" ).click( handler );
  } else {

    //если /test18_26/
    $('.oge-test-type').hide();
    $('.list-of-tests').hide();

    $( ".breadcrumb" ).children().removeClass( "active" ).html('<a href="/oge/fipi/">ОГЭ</a></li>');
    $( ".breadcrumb" ).append( "<li class='lang-test'><a href='#'>Языковой материал</a></li>" );
    $( ".breadcrumb" ).append( "<li class='active darker'>"+$( "span.darker" ).text().replace('задание','№')+"</li>" );    

    $('li.lang-test').click(function(){
      $('div.lang-test').toggle();
    });
  };
  
    };