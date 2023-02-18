# savannah-takeaway


### Test Coverage

<img src="./coverage.svg">

### What I managed to achieve
- This take away assignment is testing may areas, that I maneged to do;
##### They include:
- creating RESFful APIs.
- authentication and authorization via OpenID Connect
- Using APIs to connect to external services, eg Africa's Talking.
- Testing my endpoints using unit tests.
- Application hosting coupled with CI + CD
- Automatic Deployment to AWS elasticbeanstalk


### What I could have done better
- More authentication funtionality like verifying users, password reset, admin login.
- More functionality on order like admin viewing orders for different customers.
- Admin deleting and approving customer orders.
- Using ansible to help automate applicatin deployement.

### Project's name
## _`Savannah Informatics Take Away Test`_

### Preliquisite before you start off the project

##### For you to fire up this project locally, you should have the following installed.
- Python: You should have Python installed on your system.
- Django: You should have Django installed on your system.
- Text Editor: You should have a text editor of your choice installed on your system, in this case I am using VS code.
- Database: Django requires a database to store and retrieve data. Here I am using PostgreSQL.
- Create an account in African's Talking.
- You need Docker.

### Project description
- This is a web that allows users to:
    - Resgister Users,
    - Users to login
    - Users to make orders
    - Users to update orders
    - Users to retrieve a single order
    - Allow users to delete their orders,
## Requirements
- [Python 3.8](https://www.python.org/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [Postgres](https://www.postgresql.org/)

## How to set this manualy

- `git clone https://github.com/dunnyk/savannah-takeaway.git`
- `cd savannah-takeaway` to navigate to the project folder
- `pipenv shell` to create and activate virtual env
- `pip install -r requirements.txt` to install the dependencies
- `touch .env` to create a new env file
- `source .env` to source env variables
- copy and paste the sample env and replace with your actual credentials
- `python manage.py migrate` to apply all the migrations
- `python manage.py runserver` to start the server
- Navigate to `http://127.0.0.1:8000` to visit the site

## Sample env
- export DB_NAME=<your_db_name>
- export DB_USER=<your_db_user>
- export DB_PASS=<your_db_pass>
- export DB_HOST=<your_db_host>
- export DB_PORT=<your_db_port>
- Note: There is no space next to '='



### docker
- Install Docker: You can download and install Docker for your operating system from the Docker website
- Create a Dockerfile: A Dockerfile is a configuration file that specifies the instructions for building a Docker image.
- Build the Docker image: You can build a Docker image using the Dockerfile by running the docker build command
- Run a Docker container: You can run a Docker container using the docker run command, which will create a new container from the specified image. You can specify options such as ports to expose and environment variables to set.

### Why ebs
- AWS EBS integrates seamlessly with other AWS services.
- Amazon Elastic Compute Cloud (EC2)
- Amazon Relational Database Service (RDS)
- It's also easy to configure a load balancer to balance traffic across multiple instances.