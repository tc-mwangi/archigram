# archigram

**archigram**, is an instagram clone specifically for posting Architectural images with online followers.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Installation
OS X

### Pre-requisites
* [Python 3](https://www.python.org/)
* [Django version 1.11.17](https://www.djangoproject.com/download/)
* IDE of your choice.


### Steps

* Clone the app to a directory.
```
git clone https://github.com/tc-mwangi/archigram.git
```

* Build Locally

```
$ python -m venv virtual
$ source virtual/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

* Serve

```
Then visit http://localhost:8000 to view the app. 
```


### User Stories

* **As a User**:

* I would like to be signed into the application
* Upload pictures to the application
* View my profile with all my pictures
* Follow Other Users and see their pictures on my timeline
* Like a picture and leave a comment on it


### BDD
|     | Behaviour    |          Input                | Output    | 
|--- | ---         |     ---      |          --- |
|  1. | login registered User |  display login form   | redirect user to their timeline  |
|  2. | sign up new User | display sign up form   | save user details, redirect to signup  |
|  3. | enable image uploads |  display image uploads form  |  save, display image on user's timeline  |
|  4. | view profile, display image uploads  | |  redirect to selected location page  |
|  5. | follow or unfolow other users |  display buttons next to user's profile  | add or subtract to number of followers  |
|  6. | like a post |  display like button  | add or subtract to likes counter |
|  7. | comment on a post |  display comment form  | display comment feed  |


## Authors

* **Lose Mwangi** - *Initial work* - [archigram](https://github.com/tc-mwangi/archigram.git)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


