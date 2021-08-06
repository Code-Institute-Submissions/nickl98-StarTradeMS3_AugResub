

# StarTrade

When coming up with the idea of StarTrade I knew using databases from MongoDB could make this happen. This website allows users to create their profile and unique encrypted password with Werkzeug. People that come to the site most likely have a digital/non-digital item want to sell or trade. At StarTrade we set out and expanding to have the best trading platform on the market. We plan on setting our goals straight to the stars ourselves. The platform also has a function for Admins to manage what sort of trades are allowed, that meaning consoles, cards, NFT's, etc... Anyways enjoy looking over the site!

The overall purpose of the site is ultimately for users to come and list their items. That being said a chat platform on the app (in the future) would make things a lot more smooth when contacting the seller.

<h2 align="center"><img src = "https://github.com/nickl98/StarTradeMS3/blob/master/static/images/Responsive/devices2.png?raw=true"></h2>


The link for the app is: 

*https://star-trade.herokuapp.com/*

The link for the Github repository is:

*https://github.com/nickl98/StarTradeMS3*

## UX

To make the user experience as enjoyable as possible I opted for a simple looking site that is easy to navigate using the navigation bar links `Sign Up`, `Log In`, and `Active trades` for the not logged in user and `Active trades`, `Log Out`,  `Profile` for the signed-in user. For the superuser/admin a `Manage Categories` tab shows up when the admin signs in, allowing them to change the types of categories.
I used flash messages that provide a notification bar below the Navbar that alerts the user to when an action such as logging in or out is successful. Also will appear for admins when they delete or add a category
There is a search bar where the user can type in any word to search the trades currently available. The StarTrade logos in the header act as links to the homepage and allows you to restart the color gradient. There are links in the footer that will redirect you to either the homepage,
Twitter, Google, or a Gmail link. 

The user must be signed up and logged in to post a trade on the site. To sign up the user needs to complete the registration form on the sign-up page which requests a Username and Password. Once the user confirms their account they will be able to start posting trades.
Once a User lists an item it can be found on your `Profile` or `Active Trades` tabs. Both use Jquery to collapse an accordion view revealing details.


The original concepts for the web-app pages can be seen in the *wireframes folder*  
These were created in Adobe XD. There are numerous changes since these wireframes, mainly due to learning more about the capabilities of Python and Flask. 
There is also a database schema showing the original idea for the project.

The site is aimed at users who have an item they want to trade or sell. There are no limits on what you can list, just needs to be a category created by the admin.
We set on having as many different categories as possible so we can adhere to everyone's needs. You can list a car to trade, to even trading apples for oranges.

## Features

### Existing Features

The choice of features, links and buttons available to the user are:

* **Nav Bar –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/navbar/navbar-pic.png?raw=true)
Contains the StarTrade logo that is also a homepage link. The logo also acts as a refresh to the gradient keyframes. The Navbar is designed to keep the Logo shown still on mobile view, thanks to Bootstrap 4.
When the user scrolls down the navbar disappear, this allows for more content to be shown when scrolling.

* **Mobile Nav Bar –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/navbar/collapse-navbar.png?raw=true)
 Here is what the navbar looks like in the mobile view, with the navbar logo still showing. Shows the dropdown elements as well!

* **Admin Nav Bar –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/navbar/admin-navbar.png?raw=true) 
Contains the StarTrade logo that is also a homepage link. This is only shown to the admin, this is where the categories for trades can be changed.
The link to `Manage Categories` will only be visible to the admin user, so no one else can make that change.

* **Flash Messages –** [View](https://github.com/nickl98/StarTradeMS3/tree/master/static/images/features/flash%20messages)
I used Flash's to pop up whenever a user signs in, logs out, and when an admin deletes an item. They show up on the top of the page in bold font.

* **Mission Statement –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/content/mission_statement.png?raw=true) 
This paragraph is located below the Welcome message. Here is a brief statement about StarTrade and also directions when making a trade.

* **Search Bar –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/search%20bar/seach-bar.png?raw=true) 
The search bar is available on the main page. When you search the accordion will only show what results are queried.

* **Active Trade Accordian –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/accordian/active-trades-accordian.png?raw=true) 
Every trade that is listed will show up here. When you click on the item the user will be presented with contact information for the seller. Also if you are the seller
there will be an option to list items as sold. When that is clicked the item will be deleted.

* **Profile Trade Accordian –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/accordian/profile-accordian.png?raw=true) 
Every trade that is listed will show up here, filtered with the username. When you click on the item the user will be presented with contact information for the seller. Also if you are the seller
there will be an option to list items as sold. When that is clicked the item will be deleted.

* **Footer –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/footer/footer.png?raw=true) 
The Footer is defensively designed to show only the active social links. One of the links will bring you back to the homepage. Other links will open 
certain websites, that relate to the icons.

* **Sign up Page –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/pages/signup-page.png?raw=true) 
The Signup page is required for users to make a trade. When presented you have to enter a username and password over 5 characters. Then after a successful sign up you will be redirected to the profile page.

* **Login Page –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/pages/login-page.png?raw=true) 
The Login page provides the user with a form where they can log in using their username and password. The login page is required for users to make a trade, however, visiters can view trades but can't list a trade.

* **Profile Page –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/accordian/profile-accordian.png?raw=true) 
The Profile page will welcome you back by printing a welcome message at the top. Also, you will be able to see the current trades linked to their username.

* **Category Page  (admin only) –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/admin%20page/manage-categories-fix.png?raw=true) 
The Category page allows the admin to have control over what type of trade categories can be listed. They can choose to add a category or create a new one

* **Custom 404.html –** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/404%20page/custom-404-page.png?raw=true) 
Instead of having a default 404 page, I made a custom 404 page where the CSS and styling line up with the rest of the site. 




### Features left to implement
* Added security features, preventing URL changing. Due to time constraints, this was not done. 

* Search function not returning anything when no items match. Need to Update to show a message (e.g. No trades match your search).

* If no seller reviews have been left, need to add a statement saying 'Please be the first to review this seller'.

* Having an online chat service so that sellers and buyers can communicate with each other.

* Add a view for images to be uploaded to the trade section.

## Technologies Used
The languages, frameworks, libraries and other tools utilised for building this web-app are:

* **Gitpod -** Gitpod is a cloud-based integrated development environment (IDE) that has been used to write, run, and debug the code used for 
the web-app. https://www.gitpod.io/

* **GitHub -** GitHub has been used for version control of the code by using Git functions in the control panel. Github was utilised frequently 
during the development of the web-app.  https://github.com/

* **Heroku -** This is a cloud based application platform that allows deployment of an application to the web and connection to the database. 
https://heroku.com/



* **MongoDB -** PostgreSQL is a powerful, open source object-relational database system. https://www.postgresql.org/


* **Adobe XD -** fUsed for design of ireframes. https://www.AdobeXD.com/

### Front-End Technologies

* **HTML 5 -** The web-app uses HTML5 as a fundamental basis for building the web-app. Where possible semantic HTML is used to give the user a 
better understanding.

* **CSS3 -** The web-app uses CSS3 for styling of elements within the website. It is linked from the page to the *style.css* file.

* **Bootstrap 3.7.7 -** The open-source Bootstrap framework has been used to implement the layout of the site. Bootstrap is also utilised 
to accommodate the responsive and mobile first design of the dashboard. https://getbootstrap.com/

* **jQuery -** The web-app uses jQuery, as it simplifies a lot of complicated tasks from JavaScript, such as AJAX calls and DOM manipulation. 
https://www.jquery.com/jquery-3.4.1

* **Google Fonts-** The dashboard uses Google fonts to accentuate certain text. https://fonts.google.com/

### Back-End Technologies

* **Python 3.1 -** Python emphasises readability, uses English keywords and is highly extensible. The core language itself is quite small, 
and it is easy to learn for brginners. https://www.python.org/  



* **Jinja -** This is a modern and designer-friendly templating language for Python. It is fast, widely used and secure with the optional 
sandboxed template execution environment. https://jinja.palletsprojects.com/en/2.11.x/



## Testing

The main basic functions of the site that required rigorous testing in different scenarios are listed below.

*	**Navbar** 
    * All Navbar links are coded in a separate file called `main-nav.html`. The file is then called into the base.html and then inherited by every other webpage.
    
*	**Footer** 
    * All Footer links are encoded within the base.html that extends to each HTML page.
    The Footer Social Links of `Trade Now`, `Contact Us`, `Follow Us` and `Locate Us` have all been extensively tested to redirect the user to the relevant 
    page.

*	**Search Bar** 
    *  The Search bar is used to search all available trades. It can only be seen on the homepage, not on the profile page. In the future, I would add a hidden search bar on the profile page.
*	**404.html** 
    *  The custom 404 page is presented to the user whenever a link that doesn't work is typed in. In `app.py` an error handler is activated it will show the 404.html file.


*	**Sign Up Page** 
    * In the Sign Up Page, the user can set up an account by inserting a Username, Password. The form automatically cross-checks the validity of the username and password. There is an optional link for the user to Sign In if they already have an account. However, the username and password has to be
    over 5 characters.


*	**Login Page** 
    * A user who has already registered can log in to the site via the `Log in` Navbar menu item. This page authenticates the user against those stored in the database. 
    A user will be logged in otherwise the relevant errors will be presented. Also when logging in you will be presented with a view of the items you have listed.


*	**Profile Page - Form**
    * When succesfully logged in the profile page will be shown to the user. They will be able to see the trades they previosuly listed, no need to revist the active trades page. Unless you want to look for other trades.


*	**Responsive / Mobile First design** 
    * Each page of the web-site has a **Header**; **Body** and **Footer**. These needed to display correctly accross 
      all devices and screen resolutions. primarily checks are required to ensure that the site collapses in to columns in mobile view 
      and that the information is presented in a clear and legible fashion.    
    * Various methods of testing have been carried out to test the code of the web-site. Continuous testing throughout the development has been 
      implemented to check the quality of the code. The aim is to check the functionality of the code on different devices (mobile, tablet, desktop) 
      with an overall perspective of responsive and mobile first design. The site has been viewed and tested in **Firefox**, **Safari**, **Chrome** 
      **Microsoft Edge** and **Explorer**. The devices used to test the site are **iPad**, **iPad Pro** 
      **iPhone X**.

*	**W3 Nu Html Checker** 
    * All .html files require validation through the online checker. This ensures that the code is more legible and does 
      not contain formatting errors. https://validator.w3.org/ 

*	**W3C CSS Validator** 
    * The style.css file requires validation through the online checker. This ensures that the code is more legible and does 
      not contain formatting errors. https://jigsaw.w3.org/css-validator/validator

*	**PEP8 Online** 
    * The Python (.py) pages require validation through the online checker. This ensures that the code is more legible and does not contain formatting 
      errors. http://pep8online.com/            
       
*	**LightHouse Reports** 
    * Lighthouse is a devloper tool on google chrome that tests out if best practices where used when building the site.      
       
The final database schema and desktop wireframes for the web-app can be seen here.

**Database schema** [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/Database%20Diagrams/database.png.jpg?raw=true)


These wireframes and database schema were used initially to plan the site and build around.

**Wireframes** [View](https://github.com/nickl98/StarTradeMS3/tree/master/static/images/Wireframes)

## Issue List


  | Issue  |                 Description                     |       Solution                      |  
  | ------ |:-----------------------------------------------:|:-----------------------------------:|
  |   1    |CSS errors are presented because of the color gradient I picked.|Due to time restraints I could not figure it out [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/bugs/css-validator-bug.png?raw=true) |
  |   2    |I was presented with an error in the google developer tool when it comes to my jquery code|Due to time restraints, I left the error because jquery was still working. [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/bugs/jqueryBug.png?raw=true) |
  |   3   |Had overflow issues with navbar width [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/bugs/bg-card-with-border.png?raw=true)|I was able to fix this by adding full width to navabr [Result](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/features/navbar/navbar-pic.png?raw=true)  |
  |   4    |The desgin I choose left behind background borders [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/bugs/no-more-border.png?raw=true)|I fixed this by adding border-style = none !important [Results](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/Responsive/devices2.png?raw=true) |
  |   5   |Ran into a issue with getting html errors when adding a loop index [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/bugs/html-bug-with%20accordian.png?raw=true)|Due to time constraints I left this in because tutor support recommend this so that the accordion could be populated correctly |
  |   6    |The old homepage I had was containing overflow issues, and lacked color [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/bugs/Old_background.png?raw=true)|I fixed this by adding in a color gradient that changes every few seconds giving the site an interactive background. [Results](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/Responsive/devices2.png?raw=true) |
  |   7    |When building my project I had a lot of duplicate ID's, didn't realize they were supposed to be used once| I fixed this by making them into class names instead of id's 
 
  
(credit to the table layout above found on slack)

## Deployment

The web-site is designed in the Gitpod environment and regularly committed to GitHub after each crucial piece of coding. 
Using this method as a sanity check for the development enabled me to restore the site back to previous stages when it 
functioned correctly or easily find lost pieces of code. 

### To deploy the project to Github the following steps were taken:

  1. created a `main` branch in Github repository 
  2. Used Local Cloud9 and Gitpod environment used to build the site
  3. Committed files to the staging area using bash terminal commands: `git status`; `git add (specify directory)`; `git commit -m"add message"`
  4. Pushed files to the working environment using `git push`, which then updates the repository.
  5. Published site from `main` branch using `settings` tab in the main page of the repository, select `source` as `main branch`, then `save`
  6. The repository can be cloned by clicking `Clone or Download` on the main page of the repository 
  7. In the Clone with HTTPs section, click the clipboard icon to copy the clone URL for the repository
  8. Open Git Bash Terminal
  9. Type `git clone`, and then paste the URL
  10. Press `Enter`. A local clone will be created.


### To deploy the project to Heroku the following steps were taken:

  1. created a Heroku account @ https://signup.heroku.com/
  2. Create `requirements.txt` file in Gitpod workspace for Heroku to understand installation files to run app. From CLI type type 
     `pip3 freeze --local > requirements.txt`.
  3. To install the Heroku command line on Gitpod, use the following command `npm install -g heroku`
  4. Using the `New` buton, Create a new app with apropriate title and server in Heroku. This creates a connection between the Gitpod application and Heroku that would allow us 
     to push our changes using Git to update the application at any given time. 
  5. To login to Heroku from the CLI, use the command `heroku login`
  6. To get the application up and running a `Procfile` is required that istructs Heroku which file is the entry point. Use the following command to create this: 
     `echo web: python app.py`
  7. Code that is prepared to be pushed from Github to Heroku can be executed following the CLI commands:
     `git add .`
     `git commit -m "fist Heroku commit"`
     `git push`
  8. Now that the relevant code is pushed to Github, it can also be pushed to Heroku from the chosen branch (e.g. Master)
  9. To connect an existing repository from Github to Heroku use the following CLI syntax: `heroku git:remote -a [followed by name of Heroku app]`
  10. To push to Heroku Master Branch, then simply use `git push heroku master`
  11. To scale dynos and run the app in Heroku, use the CLI command: `heroku ps:scale web=1`
  



### Content

This README.md file is based on the Code Institute template.

