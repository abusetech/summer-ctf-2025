# A Link to the Interpreter
### The flag was in your browser all along!

This challenge doesn't have a flag *per se,* but in many modern web applications, being able to execute Javascript in another user's browser is enough perform actions on their behalf or steal session tokens to impersonate them in another browser.

This app has a link on the main page as well as a form to change the location of the link. Can you find a way to make it execute Javascript instead of taking you somewhere?

You can run this app with Docker by running `docker-compose up` in this directory, which should bring up a web server you can access at [http://localhost:5000](http://localhost:5000).