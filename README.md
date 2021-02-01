# Vintage Cars
![Devices picture](static/img/vintage_cars_responsive.png)
This application was created for people who like vintage cars and would like to expand their knowledge about other models they have not known yet and share their knowledge and models that are unique by adding to the page.

******************************************************************************************************
## Table of Contents
1. [**UX**](#ux)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)

3. [**Wireframes**](#wireframes)
    - [**Database Schema**](#database)

4. [**Technologies used**](#technologies-used)
    - [**Language**](#language)
    - [**Tools Used**](#tools-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)
    - [**Media**](#media)
    - [**Acknowledgments**](#acknowledgments)

******************************************************************************************************

### Project Rational

This app was created for the Data Centric Development project of [**_Code Institute's_**](https://codeinstitute.net/) Full Stack Software Development course. The project scope was to create a web app using Python and a MongoDB, which uses **CRUD** operations to allow users to easily create, read, update and delete data from a database viewed through a web application.

This was developed as both a front-end and backend project. The technologies used for each are:
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask, MongoDB
- Hosting: Heroku
- Database: MongoDB


## UX

The following user stories have been identified:

1. As a user, I want the home screen to be visually appealing and easy to navigate.
2. As a user, I want to be able to start register easily.
2. As a user, I want to be able to start login and logout easily.
3. As a user, I want to be able to add my car.
7. As a user, I want to be able to edit my car.
4. As a user, I want to be able to delete my car.
5. As a user, I want to be able to search car.
6. As a user, I want to be able to access this website from different devices easily.

##### Back to [Top](#table-of-contents)

## Features

### Functionality

This app makes use of Python logic to enable users to login and, or register for an account. 
The CRUD features that are available through using Python and Mongodb allow users to create, read, update and delete records in a variety of manners:

- Create car list
- Create a user account
- Read car list
- Read/view car list by all users
- Update their car list
- Update their profile
- Delete a car list

### Existing Features

**Navbar Links** 

The navbar contains the following links to all users:

- Logo
- Home
- Login
- Register

When the user is registered and logged in, the navbar will show 'Profile' and 'Add cars' buttons.

**Navbar after logged in as user**

The following are the nav bar links when a user is logged in:

- Logo
- Home
- Profile
- Add Car
- LogOut

**Navbar after logged in as Admin**

- Logo
- Home
- Profile
- Categories
- Add Car
- LogOut

As a Admin you can create, read, edit and delete Categories.

**Home Page** 

The Home page displays the cars added to the category. The "search" option is added to facilitate the search.

**Profile Page**

The Profile page displays the cars added by the user.

**Register Page**

The Register page displays the form to register by the user or if user already have an account link to Login page.

**Login Page**

The Login page displays the form to login by the user or if user is new to link to Register page.

**Add Car Page**

The Add Car page displays the form to add car by the user.

**Categories Page**

The Categories page displays all categories that have been added by Admin. This page can be create, read, edit and delete only by Admin.


##### Back to [Top](#table-of-contents)

## Wireframes

- [Wireframs Home Page](/static/img/wireframe_home_page.png)
- [Wireframs Category Page](/static/img/wireframe_category_page.png)
- [Wireframs Register Page](/static/img/wireframe_register_page.png)
- [Wireframs Login Page](/static/img/wireframe_login_page.png)
- [Wireframs Profile Page](/static/img/wireframe_profile_page.png)
- [Wireframs Add Car Page](/static/img/wireframe__add_car_page.png)
- [Wireframs Edit Car Page](/static/img/wireframe__edit_car_page.png)
- [Wireframs Add Category Page](/static/img/wireframe__add_category_page.png)
- [Wireframs Edit Category Page](/static/img/wireframe__edit_category_page.png)

## Database

- [Database Schema](/static/img/database.pdf)


##### Back to [Top](#table-of-contents)

## Technologies Used

### Language

- HTML - standard language used to create this page.
- CSS - standard language that describes the style of HTML.
- Javascript - standard language for game functions.
- Materialize - The project uses the Materialize framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Materialize styles to my app, before adding my custom styles.
- Python - used as the back-end programming language for app. 
- Flask - used Flask, which is a Python microframework.
- Jinja - used for templating with Flask in the HTML code. It allow simpler linking of the back-end to the front-end.
- JQuery - used to simplify DOM manipulation.
- PyMongo - used as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.
- MongoDB - used to store the database in the cloud. The information displayed in the front-end app is pulled from the database store.
- Github - used to host the repository.
- Heroku - used to host the app.
- Font Awesome - to style the website icons.

## Testing

The project was tested on development tools in Google Chrome and the responsiveness of mobile devices and Ipads was also tested.

- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2XL 
- Iphone 5/SE 
- Iphone 6/7/8
- Iphone 6/7/8Plus
- IphoneX
- Ipad
- Ipad Pro 
- Surface Duo 
- Galaxy Fold 

The first of the testing steps was on W3C Markup Validation and W3C CSS validation with no errors found.

The second testing step was http://ami.responsivedesign.is/, which has been used to see how the site performs on different devices and their viewports. All pages, links, icons performed as expected on all devices. I also used it to create the all-devices.jpg at the top of this Readme file.

The third step was testing by the Slack community, my mentor from the Code Institute and my friends and family.

Testing consists of finding any errors that could reveal incorrect operation of the website during its use. The website was also tested on private mobile devices like Iphone 7, Samsung A20 and Ipad 7.

All problems related to the functioning of the site have been resolved.

##### Back to [Top](#table-of-contents)

### Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [JSHint Validator tool](https://jshint.com/) to validate my JavaScript syntax.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.


## Deployment

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Run the `snap install --classic heroku` command in the terminal window to instal heroku in my local workspace.
3. Ran the `heroku login` command in the terminal window and entered my credentials to login to Heroku.
4. Added and committed the files to Git using the `git add .` and `git commit -m ""` commands in the terminal window.
5. Linked the Heroku app as the remote master branch using the following command in the terminal window:

    ```heroku git:remote -a <app-name>```

6. Created a requirements.txt file using the following command in the terminal window:

    ```pip3 freeze --local > requirements.txt```

7. Created a Procfile using the following command in the terminal window:

    ```echo web: python <fileName.py> > Procfile```

8. Ran the `git push heroku master` command in the terminal window to push the app to Heroku.
9. Ran the `heroku: ps:scale web=1` command in the terminal window to run the app in Heroku.
10. Entered the following Config Var in Heroku:

    ```MONGO_URI : <link to MongoDB>```


The app was successfully deployed to Heroku at this stage.

### Live App Link

Click the link below to run my project in the live environment:

[Vintage Cars](https://cars-vintage-project.herokuapp.com/)

### Repository Link

Click the link below to visit my project's GitHub repository:

[Vintage Cars](https://github.com/Maras00/MS3)

### Running Code Locally

To run my code locally, users can download a local copy of my code to their desktop by completing the following steps:

1. Go to [my GitHub repository]
2. Click on 'Clone or download' under the repository name.
3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4. Open 'Git Bash' in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, then paste the URL you copied in Step 3:

    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and create your local clone.
8. Create a new Database in MongoDB  
9. Create collections 
9. Navigate to the `.bashrc` terminal and add your MongoDB URI in the following format:

    ```MONGO_URI="insert your mongo uri details here"```

10. In the terminal, run the `pip3 install -r requirements.txt` command to install the requirements.txt file.
11. You should now be able to run the app locally using the `python3 run.py` command.

##### Back to [Top](#table-of-contents)

## Credits

## Content


### Media
- The images for cars were copied from [Google Gallery](https://www) 

### Acknowledgements

- I received inspiration and help for this project from my mentor and Slack community.
- I received inspiration for this project from [](https://www) and [ tutorial]()

##### Back to [Top](#table-of-contents)