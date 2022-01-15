<div align="center"> # How to Run </div>

- clone the repository
- create your virtual enviroment in the root directory using virtualenv
- activate the enviroment
- run `pip install requirements.txt` to install the dependencies
- now run the app.py file, the server should start

<div align="center"> # How to make Requests </div>

- To create a user send an POST request to `/users` endpoint with the following request body as show below
![POST_request]("./POST_request.PNG")
- To display a user send a GET request to  `/users/{id}` endpoint, the id of a particular user can be found from the `data.json file`
- To update a user send a PUT request to `/users/{id}` endpoint, the id of a particular user can be found from the `data.json file`, with the following request body
![PUT_request]("./PUT_request.PNG")
- To delete a user send a DELETE request to `/users/{id}` endpoint, the id of a particular user can be found from the `data.json file`