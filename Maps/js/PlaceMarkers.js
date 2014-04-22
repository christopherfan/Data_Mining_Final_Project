var myCenter=new google.maps.LatLng(40.79795821,-73.96370172);

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
	
	
var pinColor = "FE7569";
var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor,
        new google.maps.Size(21, 34),
        new google.maps.Point(0,0),
        new google.maps.Point(10, 34)); 
  
var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

// var marker=new google.maps.Marker({
  // position:myCenter,
  // icon:pinImage
  // });
// marker.setMap(map);
  
     var marker1 = new MarkerWithLabel({
       position: myCenter,
       draggable: true,
       raiseOnDrag: true,
       map: map,
       labelContent: "$425K",
       labelAnchor: new google.maps.Point(22, 0),
       labelClass: "labels", // the CSS class for the label
       labelStyle: {opacity: 0.75}
     });
	// marker1.setMap(map);


$.getJSON( "js/jsonAddress.json", function( data ) {
  var items = [];
  console.log(">>>>>>>>>>>>>>>>>>>>>>>");
  $.each( data, function( key, val ) {
    // items.push( "<li id='" + key + "'>" + val + "</li>" );
	console.log(val['address']);
	codeAddress(val['address'], val['time']);
  });
});


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
