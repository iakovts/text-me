# text-me
A simple aiohttp web based app, which takes user input from a form and passes it to a db. New posts
are naively served through a different endpoint. Created as a joke site for a friend's going-away party
where people connected to wifi could send messages appearing on a wall etc.

## Start the db

`docker compose -f docker-compose-db.yml up`


## Build & start the server

`docker build -t textm .` # On the root directory of the project
`docker run --net=host textm` # Running on localhost
