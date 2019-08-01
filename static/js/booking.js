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
var daysDifference = 1;

$( document ).ready(function() {
  $( "#dep_date" ).change(function() {
  	var valDep = $('#dep_date').val();
  	var valArv = $('#arval_date').val();
  	console.log(valDep);
  	console.log(valArv);
  	var dep=Math.round(new Date(valDep).getTime()/1000);
  	var arv=Math.round(new Date(valArv).getTime()/1000);
    var difference = dep - arv;
    daysDifference = Math.ceil(difference/60/60/24);

    console.log(daysDifference);
    updatePrice();

	});
	  $( "#arval_date" ).val(dateTime);
	  $( "#dep_date" ).val(tomorowdateTime );

});

$('#room_type').change(function(){
  updatePrice();
});
  
function updatePrice(){
  if (document.getElementById('room_type').value == "Double Deluxe Room") {
    document.getElementById("spanprice").textContent = DoubleDeluxeRoom*daysDifference;
    document.getElementById('price').value = document.getElementById('spanprice').innerHTML;
  }
  if (document.getElementById('room_type').value == "Single Deluxe Room") {
    document.getElementById("spanprice").textContent = SingleDeluxeRoom*daysDifference;
    document.getElementById('price').value = document.getElementById('spanprice').innerHTML;
  }
  if (document.getElementById('room_type').value == "Honeymoon Suit") {
    document.getElementById("spanprice").textContent = HoneymoonSuit*daysDifference;
    document.getElementById('price').value = document.getElementById('spanprice').innerHTML;
  }
  if (document.getElementById('room_type').value == "Economy Double") {
    document.getElementById("spanprice").textContent = EconomyDouble*daysDifference;
    document.getElementById('price').value = document.getElementById('spanprice').innerHTML;
  }
}




