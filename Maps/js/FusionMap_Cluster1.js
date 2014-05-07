 
var map;
var layer_0;
var layer_1;



/* Initialize
	1) Google Maps
	2) Default Query
	3) Legend
*/
function initialize() {
  map = new google.maps.Map(document.getElementById('map-canvas'), {
	center: new google.maps.LatLng(40.72039940933483, -74.00116651619265),
	zoom: 13,
	mapTypeId: google.maps.MapTypeId.ROADMAP
  });
  layer_0 = new google.maps.FusionTablesLayer({
	query: {
	  select: "col9",
	  // from: "1rqIGtxbFqXFlq0IdeRyxmQlcAaPQd_ZdvkyYYyWb"
	  from: "1CRk1NfA8UPxXjPyST8B6UkHs17o3gtPag-qHQaeO"
	},
	map: map,
	styleId: 3,
	templateId: 5,
      options: {
        styleId: 2,
        templateId: 2
      }	
  });

	// Create the legend and display on the map
	var legend = document.createElement('div');
	legend.id = 'legend';
	legendContent(legend);
	legend.index = 1;
	map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(legend);  
  
}
/** 
	Change Map Forms Fusion API Query and makes request to Google Maps API
**/
function changeMap_0() {
  var whereClause;
  var searchString_issuer = document.getElementById('search-string_issuer').value.replace(/'/g, "\\'");
  var searchString_dateFrom = document.getElementById('search-string_dateFrom').value.replace(/'/g, "\\'");
  var searchString_dateTo = document.getElementById('search-string_dateTo').value.replace(/'/g, "\\'");
  
  var searchString_code = document.getElementById('search_violation_code').value.replace(/'/g, "\\'");
  
  if (searchString_dateFrom != '--Select--') {    
	whereClause = "'issue_date' >= '" + searchString_dateFrom + "'";
  }
  if (searchString_dateTo != '') {
	whereClause = whereClause +" AND 'issue_date' <= '" + searchString_dateTo + "'";
  }

  //Extract Violation Codes
  if (searchString_code != '--Select--') {
	var searchCode_array = $("#search_violation_code ").val()
	var searchCode_string = "'" + searchCode_array[0] + "'";
	if( searchCode_array.length >1){
		$.each(searchCode_array.slice(1,searchCode_array.length), function(key, value){			
			searchCode_string +=  ",'"+ value + "'";
			console.log("Adding Code String", searchCode_string );
		});
	}
	console.log("Code String", searchCode_string );
	whereClause = whereClause   + " AND " + "'violation_code' IN (" +searchCode_string+ " )";
	// whereClause = whereClause  + " AND 'violation_code'='" + searchString_code + "'";
  }  

  // Extract Issuer
  if (searchString_issuer != '--Select--') {
	var searchIssuer_array = $("#search-string_issuer").val()
	var searchIssuer_string = "'" + searchIssuer_array[0] + "'";
	if( searchIssuer_array.length >1){
		$.each(searchIssuer_array.slice(1,searchIssuer_array.length), function(key, value){			
			searchIssuer_string +=  ",'"+ value + "'";
			console.log("Adding Code String", searchIssuer_string );
		});
	}
	console.log("Code String", searchIssuer_string );
	whereClause = whereClause   + " AND " + "'issuer_code' IN (" +searchIssuer_string+ " )";
	// whereClause = whereClause  + " AND 'violation_code'='" + searchString_code + "'";
  }  

  // if (searchString_issuer != '--Select--') {
	// whereClause = whereClause  +" AND 'issuer_code'='" + searchString_issuer + "'";
  // }    
  
  
  /* Make Google Fusion API Query */
  console.log(">>>>>>>>>>>>>", whereClause);
  layer_0.setOptions({
	query: {
	  select: "col9",
	  from: "1CRk1NfA8UPxXjPyST8B6UkHs17o3gtPag-qHQaeO",
	  where: whereClause
	}
  });
  
}


google.maps.event.addDomListener(window, 'load', initialize);

