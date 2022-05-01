## Did You?

Did You is a To-do list web application in which you can create several different boards with individually assigned tasks.

Visit Did You [here](https://did-you.herokuapp.com)
or visit the GitHub repository [here](https://github.com/PaulBueckhard/did-you).

## Usage
When trying to access the homepage without being logged in you will automatically be sent to the [loginpage](https://did-you.herokuapp.com/login).
On the login page you have the option to access the [registrationpage](https://did-you.herokuapp.com/register) at the bottom of the box, if you do not have an account yet.
Here you can choose your username, email and password to be added to the database. After successfully registering you are redirected to the login page again and can login with your new account. You can also check the "Remember me" box to stay logged in after closing the page.

On the homepage you will start out with an empty board list. On the left of the page type in the name of your board in the "Add board" field and hit enter or press the "+" button. You can then click on the board name to reveal your newly created board. In the text field "Add task" type in a task and press enter or the "+" button to add that task to your current board. After you have completed that task you can check it off by clicking on it or the checkbox next to it. If you want to uncheck it just click on it again. If you want all your completed tasks to be completely removed from your board, click on the "Clear completed tasks" on the bottom of your board to remove every checked off tasks from your board. If you no longer need the entire board, press the "Delete current board" next to it. The app will keep track of how many tasks you have left on the board. You can create as many boards as you want with as many tasks as you want. You can log out of your account anytime by pressing "Log out" on the top right corner.

## Architecture

### Diagram
To see a simplified diagram of the website architecture see [websitearchitecture.png](websitearchitecture.png).

### Frontend
The frontend consists of HTML, CSS and JavaScript files. In the app/templates directory you can find the three HTML pages login, main and register. In the app/static/css directory are the three CSS files affiliated to the HTML pages that share the same name. The app/static/js directory consists of one JavaScript file name script. It is only linked to the main.html page and responsible for the entire board and task functions. The JavaScript file uses forms and unique ID's for the boards and tasks to differentiate them from each other and pull them from your local browser storage. This way your boards and tasks remain after you close the page or even your browser. 

### Backend
The backend was written using Python 3 and the related python package Flask. For this project Blueprints were used to simplify the size of the application by creating instances and organizing the app into modules. The three used modules are app, main and user. App contains and handles the database as well as affiliated configurations in addition to the login manager. It also contains the for the frontend responsible folders static and templates and the two other modules. Main handles the routing to the main page of the application. Users handles everything user related. It holds the forms for the login and the registration of users as well as the routing to these corresponding pages. It also handles users logging out of the application.

## Deployment
Git and Heroku are responsible for the web deployment. Git is the communicator that pushes the code and information onto Heroku, the server host. With the help of the Procfile Heroku knows to run the run.py file, with gunicorn as its dyno, in order to start the application. 

## Requirements
To see the essential packages and requirements see [requirements.txt](requirements.txt).
