# postcardsaction

A Django based kind of a postcard-picture-blog

## Installation

Quick'n'dirty installation

    $ virtualenv --python=python3 ./
    $ source bin/activate
    $ pip install -r requirements.txt
    $ cd postcardsaction
    $ ./manage.py migrate
    $ ./manage.py collectstatic
    $ ./manage.py createsuperuser
    $ ./manage.py runserver

