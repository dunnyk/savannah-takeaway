# Savannah Informatics.

## Test Coverage

<img src="./coverage.svg">

&nbsp;

## What I managed to achieve.

- Creating REST APIs for user authentication and creating orders
- Authentication and Authorization via OpenID Connect
- Sending sms via Africa's Talking.
- Unit testing.
- Implementing CI/CD pipelines
- Automatic Deployment to AWS ElasticBeanStalk

&nbsp;

## What I could have done better

- Extend authentication feature to include more functionalities including:
  - Sending an email to users after signing up to verify the email.
  - Allow users to reset their passwords.
  - Implement Role Based Access control to allow users with different rights to access different functionalities within the app. For instance create an Admin who could have rights to view all orders, approve orders, cancel orders for different customers.
- Using ansible for configurations.
- Increase my test coverage.
- Deploy my docker container.

&nbsp;

## Prerequisites before you start off the project

### For you to fire up this project locally, you should have the following installed.

- [Python 3.8](https://www.python.org/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [Postgres](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- Africa's Talking API key and sandbox username.

&nbsp;

## How to set this manually

- `git clone https://github.com/dunnyk/savannah-takeaway.git`
- `cd savannah-takeaway` to navigate to the project folder
- `pipenv shell` to create and activate virtual env
- `pip install -r requirements.txt` to install the dependencies
- `touch .env` to create a new env file
-  copy and paste the sample env and replace with your actual credentials
- `source .env` to source env variables
- `python manage.py migrate` to apply all the migrations
- `python manage.py runserver` to start the server
- Navigate to `http://127.0.0.1:8000` to visit the site

## Sample env

- export DB_NAME=<your_db_name>
- export DB_USER=<your_db_user>
- export DB_PASS=<your_db_pass>
- export DB_HOST=<your_db_host>
- export DB_PORT=<your_db_port>
- export AT_API_KEY=<your_api_key>
- Note: There is no space next to '='

### docker

- Install Docker: You can download and install Docker for your operating system from the Docker website
- `touch .env.docker` to create a docker .env file
- copy sample env variables from sample_env_docker file, paste them in your `.env.docker` file and replace the empty variable with your credentials
- `docker-compose up --build`


## Project Endpoints

- This is a web app that allows users to:
  - SignUp `{base_url}/authenticate/customers/`
  - Login `{base_url}/authenticate/login/`
  - Make orders `{base_url}/userOrder/orders/`
  - Get all orders `{base_url}/userOrder/orders/`
  - Retrieve a single order `{base_url}/userOrder/retrieve/{{id}}`
  - Update an orders `{base_url}/userOrder/retrieve/{{id}}`
  - Delete orders `{base_url}/userOrder/retrieve/{{id}}`

- [Base Url](http://savannah-env.eba-mmj4dqaz.ap-northeast-1.elasticbeanstalk.com): http://savannah-env.eba-mmj4dqaz.ap-northeast-1.elasticbeanstalk.com

## Postman Collection
[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/14390719-d4f4e8c4-b524-49c7-863b-c4f57279c2b0?action=collection%2Ffork&collection-url=entityId%3D14390719-d4f4e8c4-b524-49c7-863b-c4f57279c2b0%26entityType%3Dcollection%26workspaceId%3D54d3eb26-e499-4a79-bb09-4cb728a78f73)

### AWS Services

- Relation Database Service as a database.
- ElasticBeanStalk
  - AWS ElasticBeanStalk is a Platform As A Service that allows us to quickly deploy our applications without provisioning our server manually.
  - It abstracts most of processes involved in setting up a server saving time when we want to quickly deploy an application.
