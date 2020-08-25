## To start the API
    Open your terminal
    $ sudo easy_install pip # installs Pip package manager
    $ git clone https://github.com/bartoszbad/googleapis-books
    $ cd googleapis-books # Browse into the repo root directory
    $ pip install virtualenv # Virtualenv is a tool to create isolated Python environments.
    $ virtualenv venv #Create virtual enviroment
    $ source venv/bin/activate # Launch the environment
    $ pip3 install -r requirements #Install dependiences
    $ create .env file -> see .env section
    $ python3 manage.py makemigrations #Make migrations
    $ python3 manage.py migrate #Migrate models
    $ python3 manage.py runserver

## .env
    SECRET_KEY=<type your django secret key>
    DATABASE_HOST=<type your Database host>
    DATABASE_USER=<type your Database username>
    DATABASE_PASSWORD=<type your Database password>
    DATABASE_NAME=<type your Database name>


## URLs and its functions:
1. /db - Allow to add data set to db
2. /books - Allow to view all books from local database Additional params: author, published_date, sort 
3. /books/pk - Shows detail of selected book 

## License
* Please see LICENSE file
