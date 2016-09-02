


$(document).ready(function() {
	var score = 0;
	function SecondNavOut(){
		var x = $(".second-nav-aa");
		console.log("x=", x[0]);
		if (x){
			for (var i = 0; i < x.length; i++){
				x[i].style.position = "absolute";
				x[i].style.top = "-9999px"; 
			}
		score=0;	
		}

};

	$("#about").click(function() {
		if (score === 1){
			SecondNavOut();
		};
		var x = document.getElementById("nav-about-list");
		x.style.position = "static";
		x.style.transform = "translate(0, 0)";
		x.style.transition ="transform 1s ease";
		score = 1;

		});
	

	$("#for-students").click(function() {
		if (score === 1){
			SecondNavOut();
		};
		var y = document.getElementById("nav-pupils-list");
		y.style.position = "static";
		y.style.transform = "translate(0, 0)";
		y.style.transition ="transform 0.1s ease";
		score = 1;
	});

	$("#for-parents").click(function() {
		if (score === 1){
			SecondNavOut();
		};
		var z = document.getElementById("nav-parents-list");
		z.style.position = "static";
		z.style.transform = "translate(0, 0)";
		z.style.transition ="transform 0.1s ease";
		score = 1;
	})

	// Test18_26 validate
var constraint = new RegExp('^[A-Za-z]{1,12}$',"");
var error = 'Задание выполнено не полностью.'


});


