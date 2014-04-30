var myCenter=new google.maps.LatLng(40.79795821,-73.96370172);
var markersArray = new Array();
var point1 = '251 W 97th St	New York	New York';
var point2 = '101 Manhattan Ave	New York	New York';
var point3 = '622 W 132nd St	New York	New York';
var point4 ='274 W 145th St	New York	New York';
var points = [point1,point2, point3, point4];
var geocoder;

function initialize()
	{
	geocoder = new google.maps.Geocoder();
	var mapProp = {
	center:myCenter,
	zoom:13,
	mapTypeId:google.maps.MapTypeId.ROADMAP
	};
	
$(document).ready(function() { 
	console.log("Ready");
	$.getJSON( "data/json/json_geo3.json", function( data ) {
		$.each(data, function(key, value){
			console.log(key);
			  $('#date_select').append('<option value='+key +'>'+key+ '</option>');
		});
	});
	
});	

var pinColor = "FE7569";
var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor,
        new google.maps.Size(21, 34),
        new google.maps.Point(0,0),
        new google.maps.Point(10, 34)); 
  
var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

$('#date_select').on('change', function() {
  // alert( this.value ); // or $(this).val()
  printMarkers($("#date_select").val());
});
 
function printMarkers(date){ 
	$.getJSON( "data/json/json_geo3.json", function( data ) {
	  console.log(">>>>>>>>>>>>>>>>>>>>>>>", date);
	  var date_entries = data[date]
	  console.log(date_entries);
	  console.log(date_entries);
	  clearOverlays();
	  $.each( date_entries, function( key, val ) {
		// items.push( "<li id='" + key + "'>" + val + "</li>" );
		console.log(val['lat'], val['long']);
		var time_violation = val['time'] + "_" + val['violation']
		var myCenter=new google.maps.LatLng(val['lat'], val['long']);

		// setTimeout(function (){
			var marker=new google.maps.Marker({
				position:myCenter,
				icon:pinImage,
				title:time_violation
				});		
			marker.setMap(map);
             //something you want delayed
         // }, 100);
		
		
		markersArray.push(marker);
	  });
	});	
}

function clearOverlays() {
  if (markersArray) {
    for (i in markersArray) {
      markersArray[i].setMap(null);
    }
  }
  markersArray= new Array();
}

// $.getJSON( "js/jsonAddress.json", function( data ) {
  // var items = [];
  // console.log(">>>>>>>>>>>>>>>>>>>>>>>");
  // $.each( data, function( key, val ) {
    // // items.push( "<li id='" + key + "'>" + val + "</li>" );
	// console.log(val['address']);
	// // codeAddress(val['address'], val['time']);
  // });
// });


function codeAddress(value, time) {
  <!-- var address = document.getElementById('address').value; -->
  address = value;
  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location,
		  title:time
      });    
	} else if (status === google.maps.GeocoderStatus.OVER_QUERY_LIMIT) {    
		setTimeout(function() {
			codeAddress(address);
		}, 200);
	}else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}
}
google.maps.event.addDomListener(window, 'load', initialize);
