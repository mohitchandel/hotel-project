//rooms values

var SingleDeluxeRoom  = 200;	
var EconomyDouble     = 200;
var DoubleDeluxeRoom  = 250;
var HoneymoonSuit     = 750;

var today = new Date();
var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
var time = today.getHours() + ":" + today.getMinutes();
var ampm = time >= 12 ? 'PM' : 'AM';
var dateTime = date+' '+time+' '+ampm;

var tomorrow = new Date();
tomorrow.setDate(tomorrow.getDate()+1);
var tomorowdate = tomorrow.getFullYear()+'-'+(tomorrow.getMonth()+1)+'-'+tomorrow.getDate();
var tomorowtime = tomorrow.getHours() + ":" + tomorrow.getMinutes();
var tomorowampm = time >= 12 ? 'PM' : 'AM';
var tomorowdateTime = tomorowdate+' '+tomorowtime+' '+tomorowampm;


$( document ).ready(function() {
  $( "#dep_date" ).change(function() {
  	var valDep = $('#dep_date').val();
  	var valArv = $('#arval_date').val();
  	console.log(valDep);
  	console.log(valArv);
  	var dep=Math.round(new Date(valDep).getTime()/1000);
  	var arv=Math.round(new Date(valArv).getTime()/1000);
    var difference = dep - arv;
    var daysDifference = Math.ceil(difference/60/60);

    console.log(daysDifference);

	});

	  $( "#arval_date" ).val(dateTime);
	  $( "#dep_date" ).val(tomorowdateTime );

});

function myFunction() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}