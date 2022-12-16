# ecabanas dev - ci portfolio

## Introduction
Welcome to my fourth project. This project is a simple portfolio, allow users to vote and comment projects. This will use languages such as Django, Python, HTML, CSS and JavaScript.

This project will show the use of CRUD functionality (Create, Read, Update, Delete). The admin will be able create, read, update and delete their projects.

A live website can be found [here](https://pp4-portfolio.herokuapp.com/).

# Table of Contents
 [1. UX Design](#ux)
- [User Goals:](#user-goals)
- [User Expectations:](#user-expectations)
- [User Stories:](#user-stories)
-	[Colour scheme and font](#color-scheme)
- [Website skeleton](#wireframes)

[2. Features](#features)

[3.Technologies](#technologies)

[4.Testing](#testing-phase)

[5.Bugs](#bugs)

[6. Deployment](#deployment)

[7. Acknowledgement](#acknowledgement)


<a name="ux"></a>
# 1. UX design
[Go to the top](#table-of-contents)

<a name="user-goals"></a>
## 1.1 User Goals
[Go to the top](#table-of-contents)

First-Time Visitor Goals
- As a first-time visitor, I want to see portfolio projects.
- As a first-time visitor, I want to see the project details.
- As a first-time visitor, I want to see the project user comments.
- As a first-time visitor, I want to see the project user likes.
- As a first-time visitor, I want to view the contact menu.
- As a first-time visitor, I want to be able to register on the website as a user.

Returning Visitor Goals

- As a Returning Visitor, I can login with my registered user.
- As a Returning Visitor, I can comment on published projects.
- As a Returning Visitor, I can like/dislike projects.

Frequent User Goals

- As a Frequent User, I want to check if there are any new projects.
- As a Frequent User, I want to check if there are any new comments on projects.

Admin User Goals

- As an admin, I want to manage projects (create, publish/unpublish, update and delete)
- As an admin, I want to manage projects comments (publish and delete)

<a name="user-expectations"></a>
## 1.2 User Expectations
[Go to the top](#table-of-contents)

- The design should be clear and clean.
- Easy navigation through the different pages.
- Compatible with all browsers.
- Responsive design and adaptable to all devices.
- Have the possibility of contacting the developer for any questions.

<a name="user-stories"></a>
## 1.3 User Stories
[Go to the top](#table-of-contents)

The project has been managed using the GitHub project boards tool. It is a very useful tool to classify the different tasks to be carried out in the project.

![github-boards](docs/images/github-boards.png)

Link to user stories [here](https://github.com/users/ecabanasv/projects/10/views/1)

<a name="color-scheme"></a>
## 1.4 Color Scheme
[Go to the top](#table-of-contents)

The colour scheme of the project is quite simple and clean. The following colours used are presented below:

- Background: #212529
- Text: white
- Links: orange
- Hover link: yellow

The colour palette can be seen through the following [link](https://coolors.co/212529-ffffff-ff7f00-ffff00).

<a name="wireframes"></a>
## 1.5 Website Skeleton
[Go to the top](#table-of-contents)

### Desktop

<details> <summary>Desktop (click here to view)</summary>

Index:

![index](docs/wireframes/desktop/01.%20Index.png)

About:

![about](docs/wireframes/desktop/02.%20About.png)

Portfolio - 1st page:

![portfolio - 1st page](docs/wireframes/desktop/03.%20Portfolio%20-%201st%20page.png)

Portfolio - 2nd page:

![portfolio - 2nd page](docs/wireframes/desktop/04.%20Portfolio%20-%202nd%20page.png)

Portfolio - Admin:

![portfolio - admin](docs/wireframes/desktop/05.%20Portfolio%20-%20Admin.png)

Portfolio - Unpublished:

![portfolio - unpublished](docs/wireframes/desktop/06.%20Portfolio%20-%20Unpublished.png)

Project details:

![project details](docs/wireframes/desktop/07.%20Project%20details.png)

Project details - user:

![project details - user](docs/wireframes/desktop/08.%20Project%20details%20-%20User.png)

Project details - admin:

![project details - admin](docs/wireframes/desktop/09.%20Project%20details%20-%20Admin.png)

Add new project:

![add new project](docs/wireframes/desktop/10.%20Add%20new%20project.png)

Update project:

![update project](docs/wireframes/desktop/11.%20Update%20project.png)

Delete project:

![delete project](docs/wireframes/desktop/12.%20Delete%20project.png)

Contact:

![contact](docs/wireframes/desktop/13.%20Contact.png)

Signup:

![signup](docs/wireframes/desktop/14.%20Signup.png)

Login:

![login](docs/wireframes/desktop/15.%20Login.png)

Logout:

![logout](docs/wireframes/desktop/16.%20Logout.png)

</details>

### Mobile

<details> <summary>Mobile (click here to view)</summary>

Index:

![index](docs/wireframes/mobile/01.%20Index.png)

About:

![about](docs/wireframes/mobile/02.%20About.png)

Portfolio:

![portfolio](docs/wireframes/mobile/03.%20Portfolio%20-%20User.png)

Portfolio - admin:

![portfolio - admin](docs/wireframes/mobile/04.%20Portfolio%20-%20Admin.png)

Portfolio - unpublished:

![portfolio - unpublished](docs/wireframes/mobile/05.%20Portfolio%20-%20Unpublished.png)

Project details:

![project details](docs/wireframes/mobile/09.%20Project%20details%20-%20non%20user.png)

Project details - user:

![project details - user](docs/wireframes/mobile/10.%20Project%20details%20-%20user.png)

Project details - admin:

![project details - admin](docs/wireframes/mobile/11.%20Project%20details%20-%20admin.png)

Add new project:

![add new project](docs/wireframes/mobile/06.%20Add%20new%20project.png)

Update project:

![update project](docs/wireframes/mobile/07.%20Update%20project.png)

Delete project:

![delete project](docs/wireframes/mobile/08.%20Delete%20project.png)

Contact:

![contact](docs/wireframes/mobile/12.%20Contact.png)

Signup:

![signup](docs/wireframes/mobile/13.%20Signup.png)

Login:

![login](docs/wireframes/mobile/14.%20Login.png)

Logout:

![logout](docs/wireframes/mobile/15.%20Logout.png)

</details>

<a name="features"></a>
# 2. Features
[Go to the top](#table-of-contents)

### All Pages

Header:

![navbar](docs/images/desktop/navbar.png)

Messages:

![messages](docs/images/desktop/messages.png)

Footer:

![footer](docs/images/desktop/footer.png)

### Index

Index:

![index](docs/images/desktop/01-index.png)

### About

About:

![about](docs/images/desktop/02-about.png)

### Portfolio

User:

![portfolio-user](docs/images/desktop/03-portfolio-user.png)

Admin:

![portfolio-admin](docs/images/desktop/04-portfolio-admin.png)

Admin comments:

![admin-comments](docs/images/desktop/admin-comments.png)

Pagination:

![pagination](docs/images/desktop/pagination.png)

### Portfolio - Unpublished

Portfolio unpublished:

![portfolio-unpublished](docs/images/desktop/05-portfolio-unpublished.png)

### Project details

Project details (non user):

![project-details-nonuser](docs/images/desktop/06-project-details-nonuser.png)

Project details (user):

![project-details-user](docs/images/desktop/07-project-details-user.png)

Project details (admin):

![project-details-admin](docs/images/desktop/08-project-details-admin.png)

### Add new project

Add new project:

![add-new-project](docs/images/desktop/09-add_new_project.png)

### Update project

Update project:

![update-project](docs/images/desktop/10-update_project.png)

### Delete project

Delete project:

![update-project](docs/images/desktop/11-delete_project.png)

### Contact

Contact:

![contact](docs/images/desktop/12-contact.png)

### Sign Up

Signup:

![contact](docs/images/desktop/13-signup.png)

### Login

Login:

![contact](docs/images/desktop/14-login.png)

### Logout

Logout:

![contact](docs/images/desktop/15-logout.png)

 <a name="technologies"></a>
# 3. Technologies Used
[Go to the top](#table-of-contents)

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    -   The project uses HyperText Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   The project uses Cascading Style Sheets.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   The project uses JavaScript.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    -   The project uses Python.
-   [Django](https://www.djangoproject.com/)
    -   The project uses Django framework for web development.
-   [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    -   The project uses Bootstrap 5.
-   [Elephant SQL](https://www.elephantsql.com/)
    -   The project uses ElephantSQL as a database hosting.
-   [PostgreSQL](https://www.postgresql.org/)
    -   The project uses PostgreSQL as a database.
-   [Visual Studio code](https://code.visualstudio.com/)
    -   The project uses Visual Studio code for developing.
-   [Firefox developer](https://www.mozilla.org/en-US/firefox/developer/)
    -   The project uses Firefox developer to debug and test the source code.
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    -   The project uses Chrome Developer tools to test performance.
-   [Balsamiq](https://balsamiq.com/)
    -   Balsamiq was used to create the wireframes during the design process.
-   [Google Fonts](https://fonts.google.com/)
    -   Google fonts were used to import the "Be Vietnam Pro" font into the style.css file which is used on all pages throughout the project.
-   [GitHub](https://github.com/)
    -   GitHub was used to store the project's code after being pushed from Git.

<a name="testing-phase"></a>
# 4. Testing
[Go to the top](#table-of-contents)

## 4.1 Testing using tools

### 4.1.1 Browser Developer tools

#### Google Developer tools

Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. It was used in the project to test the performance of the different pages of the project. Also Lighthouse was used to check the accesibility of the web project.

### 4.1.2 Responsive Tools

[Am I Responsive](http://ami.responsivedesign.is) was used to make sure that all my pages are responsive to all devices.

### 4.1.3 W3C Validator Tools (HTML and CSS)

#### HTML

Index fails:

![index-bad](docs/test/html/01-index-bad.png)

Index passed:

![index-good](docs/test/html/01-index-good.png)

About:

![about](docs/test/html/02-about-good.png)


Portfolio:

![portfolio](docs/test/html/03-portfolio.png)


Project details:

![project-details](docs/test/html/04-project_details.png)


Add project:

![add-project](docs/test/html/05-add_project.png)


Delete project:

![delete-project](docs/test/html/07-delete_project.png)


Contact:

![contact](docs/test/html/08-contact.png)


Signup:

![signup](docs/test/html/09-signup.png)


Login:

![login](docs/test/html/10-login.png)


#### CSS

CSS Validator:

![css-validator](docs/test/css/validator.png)

#### JavaScript

JavaScript validator:

![js-validator](docs/test/javascript/validator.png)


#### Python

Admin:

![admin](docs/test/python/01-admin.png)

Models:

![models](docs/test/python/02-models.png)

URLs:

![urls](docs/test/python/03-urls.png)

Views:

![views](docs/test/python/04-views.png)

Forms:

![forms](docs/test/python/05-forms.png)

## 4.2 Manual Testing

### All Pages

### Index

Lighthouse:

![index](docs/test/lighthouse/01-index.png)

### About

Lighthouse:

![about](docs/test/lighthouse/02-about.png)

### Portfolio

Lighthouse:

![portfolio](docs/test/lighthouse/03-portfolio.png)

### Project details

Lighthouse:

![project-details](docs/test/lighthouse/04-project_details.png)

### Contact

Lighthouse:

![contact](docs/test/lighthouse/05-contact-form.png)

### Add new project

Lighthouse:

![add-new-project](docs/test/lighthouse/06-add_new_project.png)

### Update project

Lighthouse:

![update-project](docs/test/lighthouse/07-update_project.png)

### Delete project

Lighthouse:

![delete-project](docs/test/lighthouse/08-delete_project.png)

### Sign Up

Lighthouse:

![sign-up](docs/test/lighthouse/09-signup.png)

### Login

Lighthouse:

![login](docs/test/lighthouse/10-login.png)

### Logout

Lighthouse:

![logout](docs/test/lighthouse/11-logout.png)

<a name="bugs"></a>
# 5. Bugs
[Go to the top](#table-of-contents)

### Solved bugs

<a name="deployment"></a>
# 6. Deployment
[Go to the top](#table-of-contents)

## Deployment to Heroku

### 1. Creating the Django Project
* If development if being done locally: Activate your virtual environment
* To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
* Install Django and gunicorn: `pip install django gunicorn`
* Install supporting database libraries dj_database_url and psycopg2 library: `pip install dj_database_url psycopg2`
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`
* Create file for requirements: `pip freeze --local > requirements.txt`
* Create project:`django-admin startproject project_name .`
* Create app: `python manage.py startapp app_name`
* Add app to list of `installed apps` in settings.py file: `'app_name'`
* Migrate changes: `python manage.py migrate`
* Test server works locally: `python manage.py runserver`

### 2. Create your Heroku app
* Navigate to the Heroku website
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app
* In the Heroku dashboard click on the Resources tab
* Scroll down to Add-Ons, search for and select 'Heroku Postgres'
* In the Settings tab, scroll down to 'Reveal Config Vars' and copy the text in the box beside DATABASE_URL.

### 3. Set up Environment Variables
* In you IDE create a new env.py file in the top level directory
* Add env.py to the .gitignore file
* In env.py import the os library
* In env.py add `os.environ["DATABASE_URL"]` = "Paste in the text link copied above from Heroku DATABASE_URL"
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`
* In Heroku Settings tab Config Vars enter the same secret key created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

### 4. Setting up settings.py

* In your Django 'settings.py' file type:

 ```
 from pathlib import Path
 import os
 import dj_database_url

 if os.path.isfile("env.py"):
  import env
 ```
* Remove the default insecure secret key in settings.py and replace with the link to the secret key variable in Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`
* Comment out the `DATABASES` section in settings.py and replace with:
```
DATABASES = {
  'default': 
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }`
```
* Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`
* In Heroku  add cloudinary url to 'config vars'
* In Heroku config vars add DISABLE_COLLECTSTATIC with value of '1' (note: this must be removed for final deployment)
* Add Cloudinary libraries to the installed apps section of settings.py file:
 ```
 'cloudinary_storage'
 'django.contrib.staticfiles''
 'cloudinary'
 ```
* Connect Cloudinary to the Django app in `settings.py`:
```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku 
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
* Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
* Add Heroku Hostname to ALLOWED_HOSTS: ```ALLOWED_HOSTS =
['rhi-book-nook.herokuapp.com', 'localhost']```
*Create Procfile at the top level of the file structure and insert the following:
    ``` web: gunicorn PROJECT_NAME.wsgi ```

* Make an initial commit and push the code to the GitHub Repository.
    ```git add .```
    ```git commit -m "Initial deployment"```
    ```git push```

### 5. Heroku Deployment: 
* Click Deploy tab in Heroku
* In the 'Deployment method' section select 'Github' and click the 'connect to Github' button to confirm.
* In the 'search' box enter the Github repository name for the project
* Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.

### 6. Final Deployment
In the IDE: 
* When development is complete change the debug setting to: `DEBUG = False` in `settings.py` 
* In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

## To fork the repository on GitHub

A copy of the GitHub Repository can be made by forking the GitHub account. Changes can be made on this copy without affecting the original repository.

1. Log in to GitHub and locate the repository in question.
2. Locate the Fork button which can be found in the top corner, right-hand side of the page, inline with the repository name.
3. Click this button to create a copy of the original repository in your GitHub Account.

## To clone the repository on GitHub

1. Click on the code button which is underneath the main tab and repository name to the right.
2. In the 'Clone with HTTPS' section, click on the clipboard icon to copy the URL.
3. Open Git Bash in your IDE of choice.
4. Change the current working directory to where you want the cloned directory to be made.
5. Type git clone, and then paste the URL copied from GitHub.
6. Press enter and the clone of your repository will be created.

<a name="acknowledgement"></a>
# 7. Acknowledgement
[Go to the top](#table-of-contents)

### Code

### Content 




