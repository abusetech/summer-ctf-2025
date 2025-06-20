# Badcookie

## This one is spoiled!

This app uses [JSON Web Tokens (JWTs)](https://en.wikipedia.org/wiki/JSON_Web_Token) to authenticate the user. 

The app contains two pages, a home page located at the root directory ("/") and a super secret admin page at "/admin." See if you can find a bug to exploit that will let you gain access to the admin page.

You can run this app with Docker by running `docker-compose up` in this directory, which should bring up a web server you can access at [http://localhost:5000](http://localhost:5000).