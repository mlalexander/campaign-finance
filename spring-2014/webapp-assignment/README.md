# Web app assignment

Your final assignment has a couple parts:

First, you'll have to rig up a frontend application similar to the one we built in class to a different data source: namely, a JSON file of federal campaign contributions made by Columbia residents during the 2014 filing cycle. You can (and should) use the data in the webapp-example folder as a starting point. The JSON data you'll need can be found in two places: either by running the Flask application found in the "flask" directory and navigating to 127.0.0.1:5000/data-dynamic, or by using the static version saved in the "frontend" directory. Specifically, you should build a frontend application to access the data via AJAX, map any records that have coordinate information, and lay out the rest within the table below.

The second part of your assignment is a bit more subjective: Make the application your own. A few ways you might do this: Create a new JSON file from the Flask application based on a more specific query (top 10 donors? large donors? etc.) You could also add/change some functionality in map or table based on the [Leaflet](http://leafletjs.com/examples.html) and [DataTables](https://datatables.net/examples/index) documentation. Or your could add additional styling elements. Use your journalistic judgment and try to use the data to tell a story.

The assignment is due next Monday, May 12, by noon.