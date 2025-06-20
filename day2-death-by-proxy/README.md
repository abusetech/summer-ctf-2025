# Death by Proxy
### It's microservices all the way down

This app actually contains *two* apps! One user-facing site, and one backend app that provides APIs to the public site. The backend app has an interesting API endpoint not exposed to the public. Can you find a way to access it? (For the purposes of this challenge, you cannot connect directly to the backend application running on port 15000)

You can run this app with Docker by running `docker-compose up` in this directory, which should bring up a web server you can access at [http://localhost:5000](http://localhost:5000).