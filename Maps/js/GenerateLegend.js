     /* EDIT THE FOLLOWING LINES */
      // The numeric table id, find this by selecting File > About from the table.
      var tableId = 4161507;
      // The column in your table containing the LOCATIONs.
      var locationColumn = 'geometry';
      // A title for the legend.
      var legendTitle = 'Time Legend';
      // The min / max values for each bucket and the associated color.
      var styles = [
        {
          'min': '6-9',
          // 'max': 1,
          'color': 'yellow'
        },
        {
          'min': '9-Noon',
          'max': 2,
          'color': 'purple'
        },
        {
          'min': 'Noon-3',
          'max': 2,
          'color': 'green'
        },
        {
          'min': '3-6',
          'max': 79999,
          'color': 'blue'
        },
		 {
          'min': '6-',
          'max': 89999,
          'color': 'red'
        }
      ];
      /* DONE EDITING */


function legendContent(legend) {
	var title = document.createElement('p');
	title.innerHTML = legendTitle;
	legend.appendChild(title);

	for (var i in styles) {
	  var bucket = styles[i];

	  var legendItem = document.createElement('div');

	  var color = document.createElement('span');
	  color.setAttribute('class', 'color');
	  color.style.backgroundColor = bucket.color;
	  legendItem.appendChild(color);

	  var minMax = document.createElement('span');
	  minMax.innerHTML = bucket.min ; //+ ' to ' + bucket.max;
	  legendItem.appendChild(minMax);

	  legend.appendChild(legendItem);
	}
}