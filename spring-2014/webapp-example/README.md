# Web app example

We've talked about the two major components of any good web application: the backend (which we wrote in Python/Flask), and the frontend (HTML, CSS and Javascript). All of the code we used for the example in class is stored in this folder.

You'll remember that we used Flask to generate a JSON file by accessing a SQLite database. When we're building an application, we have the option to connect our frontend directly to the Flask backend and the JSON it generates, but that takes a bit of extra effort if we're going to launch it into the wild. Instead, we went with a simpler approach: creating a raw JSON file that could power our application on its own. This is a popular approach used by The New York Times, NPR and many other news organizations because it eliminates the complex server configuration required to host an application dynamically. It's also much, much cheaper. Your bosses someday will thank you.

## Running the backend and frontend applications ##

Of course, for the purposes of this class we're not running our apps on the Internet -- we're running them on our own machines. Because we haven't set them up to connect directly, the frontend and backend parts of the app each have to be launched in slightly different ways.

To run the Flask app that generates the JSON, we can simply navigate into the directory containing the app and type: ```python app.py``` (assuming your file is called app.py). That will start the built-in Flask server and allow you to see the site in your web browser at the address 127.0.0.1:8000.

Python also comes with a generic server you can use to render static HTML files, like the one we're building for our frontend. You may have noticed that if you open your static HTML files in your web browser, it might look as though they are rendering correctly. However *this is a bad idea*. Many Javascript calls, including anything involving AJAX, will not work properly unless you are viewing your HTML file through a server. That's why Python's built-in server is so useful.

To launch it, navigate into the directory where the HTML file for your frontend application is stored and type: ```python -mSimpleHTTPServer```. Once again, a local server will be launched at the IP address 127.0.0.1:8000. To view your file, just add its name to the end of the IP address. So if your file is called incidents.html, you could view it by going to 127.0.0.1:8000/incidents.html. This is the easiest environment in which to do your frontend development.

## Connecting the frontend to a data source ##

Because all we're doing is loading a JSON file, the easiest way to set this up is to be sure the JSON file we're using is in the same directory as the HTML file containing our frontend application. In order to be loaded via AJAX, a JSON file also has to be accessible at a URL. In this case, it'll be at 127.0.0.1:8000. If our web application and our JSON file are in the same directory, they'll just magically work when we run the ```python -mSimpleHTTPServer``` command above.