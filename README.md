# Jungle Devs - Backend Challenge #001

## Considerations

First of all I would like to thank the oportunity to participate this challenge, it was very enriching. I had almost no experience with python beforehand (the code that I made seems to be really ugly). The django tutorial was quite satifying and straightfoward to implement. It started to get ugly when Django REST Framework appeared. It was hard for me to understand the tutorials and how it fits in the project, as well as understand why things were being structured that way. 

I started the challenge with the intention to implement it using Django REST Framework, the User entity was built this way, but thigs started to get messy, so I decided to use plain Django to implement the rest of the entities. That being said, CRUD functionallities and authentication probably will not work. The URLs and entities models are following the specified instructions.

Here's what you should expect:
https://user-images.githubusercontent.com/22632486/109894762-d3ffc900-7c6c-11eb-9387-919285505cb4.mp4



## Prerequisites

- [Python 3.7](https://www.python.org)
- [Docker](https://www.docker.com)
- [Docker Compose](https://docs.docker.com/compose/)
- [Virtualenv](https://github.com/pypa/virtualenv/)
- [Git](https://git-scm.com/)

## Instructions to Run

- Create the virtual environment and activate it

        virtualenv -p python3 venv
        source venv/bin/activate
- Install the requirements `pip install -r requirements.txt`
- Start the dockers `docker-compose up` with the database and the localstack
- Run the server with `python manage.py runserver 8000`

You need a `.env`file with your environment variables, here's an example file:
```
LOAD_ENVS_FROM_FILE='True'
ENVIRONMENT='development'
SECRET_KEY='#*=backend-challenge=*#'
DEFAULT_FROM_EMAIL='Challenge <challenge@jungledevs.com>'
DATABASE_URL='postgres://postgres:postgres@localhost:5432/boilerplate'
SENTRY_DSN='sentry_key'
AWS_STORAGE_BUCKET_NAME='django-be'
```

## Additional Information
Here are some useful stuff to keep in mind while completing this challenge:

* Try to keep your code [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), so the creation of 
[abstract helper](https://realpython.com/modeling-polymorphism-django-python/#abstract-base-model) [models](https://docs.djangoproject.com/en/3.0/topics/db/models/#abstract-base-classes) is more than welcome 
to avoid repetition of fields in your models
* Remember that only the author of a topic, post or comment should be able to modify or delete it!
If you have any doubts, check the 
[Authentication and Permissions part](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/) 
on the Django REST tutorial
* For better structuring and visualization, you may use 
[Nested Serializers](https://www.django-rest-framework.org/api-guide/relations/#nested-relationships) to customize your 
responses beyond the primary keys

### Entities

As mentioned in the description, this challenge will have four entities (each one should be a separate app). 
Here are brief descriptions of what they are and what are the expected properties of each (keep in mind that you can 
improve them as you wish!):

* *User*: can be used plain from what is offered by Django;
* *Topic*: the equivalent of a sub-reddit. The suggest fields are:
    * Name
    * Title
    * Author
    * Description
    * URLName - the name we want to use to reach it through the browser (check [SlugField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#slugfield))
    * Created_at
    * Updated_at
* *Post*: the equivalent of a *Reddit thread*, a *post* belongs to a *specific topic* and is *created by an user*. The 
suggested fields are:
    * Title
    * Content
    * Created_at
    * Updated_at
    * Topic
* *Comment*: the equivalent of a comment, a comment belongs to a *specific post* (which belongs to a *specific topic*) 
and is *created by an user*. The suggested fields are:
    * Title
    * Content
    * Created_at
    * Updated_at
    * Post
    
### URLs    

We want to have a behavior similar to *Reddit (not necessarily equal)*, so ideally we'd like a structure like this:

* */topics/* - lists all available topics
* */topics/{urlname}/* - details (as well as some posts) from a specific topic (identified by *urlname*)
* */topics/{urlname}/posts/* - lists all posts from a specific topic
* */topics/{urlname}/posts/{post_id}/* - lists details and some comments from a post
* */topics/{urlname}/posts/{post_id}/comments/* - lists all comments from a post
* */topics/{urlname}/posts/{post_id}/comments/{comment_id}/* - lists details from a comment


If you have any doubts on how to implement these structures, check the
[Nested Routers documentation](https://github.com/alanjds/drf-nested-routers) and the 
[lookup field section on the Routers documentation](https://www.django-rest-framework.org/api-guide/routers/#simplerouter).
