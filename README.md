# Bottle+sqlite3 backend CRUD service example

## Implemented methods

- {get} /users - list of users
- {get} /users/:id - find user by id
- {post} /users/add - add user
- {put} /users/:id - update user by id
- {delete} /users/:id - delete user by id

## Run
docker build -t cs-rest-crud . && docker run -p 5000:5000 --rm cs-rest-crud 