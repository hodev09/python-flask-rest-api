# python-flask-rest-api
Ready to go rest api written in python using flask micro framework &amp; sqlAlchemy with jwt authentication. 

how to use :

1. install Python, Pipenv and Postgres
2. clone this project. Master branch will always have the latest stable code.
3. navigate to python-flask-rest-api
4. open terminal / cmd prompt at this location **~\python-flask-rest-api** (you can also open up in a ide pycharm is one of the best
   available IDE for python / I also recommend visual studio code)
   
   create a .env file in your root folder & copy the following code.
   
         FLASK_ENV='development'
         DATABASE_URL='postgresql://postgres:{your_password}@localhost/{your_database}'
         JWT_SECRET_KEY='ponnambalpuzhayarukilnammalannadyamkandathormayille'
         CORS_HEADERS='Content-Type'
         PORT=6503
         
   
5. run the following commands :-
    a. pipenv shell -- this creates a virtual environment for our self thriving web app.
    b. pipenv install -- this will install all our project dependencies our app need. You can view these dependencies in Pipfile. It is
       similar to pakage.json in a node application.
6. After the above steps, we can run our api server by typing command :- **python run.py
7. by defualt the port number will be 6503, you can change this in .env file.
8. Next step would be configuring database.

   a. exit from the api server by pressing ctrl+c
   
   b. create a database in your postgres server :- {any name will do}.
   
   c. in .env file change the DATABASE_URL from 'postgresql://postgres:{your passowrd}@localhost/{api}'
   
   d. now run :- **python manage.py db init**      # this will create initial migration folders
   
   e. next run :- **python manage.py db migrate**
   
   f. finally run :- **python manage.py db upgrade**
   
  
 After these steps are completed.
again run **python run.py**

try out the api endpoints in postman. you can refer for the end points in Views/UserViews
