<h1 align="center">StarTrade </h1>

[View the live project here.](https://star-trade.herokuapp.com/)

When coming up with the idea of StarTrade I knew using databases from MongoDB could make this happen. This website allows users to create their profile and unique encrypted password with Werkzeug. People that come to the site most likely have a digital/non-digital item want to sell or trade. At StarTrade we set out and expanding to have the best trading platform on the market. We plan on setting our goals straight to the stars ourselves. The platform also has a function for Admins to manage what sort of trades are allowed, that meaning consoles, cards, NFT's, etc... Anyways enjoy looking over the site!
<h2 align="center"><img src = "https://github.com/nickl98/StarTradeMS3/blob/master/static/images/Responsive/responsive_picture.png?raw=true"></h2>

## UX


### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.JavaScript.com/)
-   [Python](https://www.python.org/)
### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Roboto Slab' font into the style.css file which is used on all pages throughout the project.
3. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
4. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
5. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
6. [MongoDB:](https://www.mongodb.com/cloud/atlas1)
    - MongoDB was used as the main storage for all the database data.
7. [Adobe XD:](https://adobe.xd.com/)
    - Adobe XD was used during the design process.
8. [JavaScript:](https://www.JavaScript.com/)
    - JavaScript JavaScript was used a little bit for some of the tooltip functions.
9. [WebFormatter:](https://webformatter.com/html)
    -  WebFormatter was used at the end of the project for correct spacing and formatting in the code
10. [Heroku:](https://www.heroku.com/)
    - Heroku was used to host the application.
11. [Flask:]()
    - Flask was used in the python file for talking to the database

12. [PyMongo]()
    - This also played a big part in communicating to the daatbase in the python folder.


## Testing

The W3C Markup Validator, W3C CSS Validator, Lighthouse Audits, and CodeBeautify Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C HTML Validator](https://validator.w3.org/#validate_by_input) - [Results](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/Responsive/lighthouse_valadation.png)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/Valadation%20pictures/CSS%20Valadation/css_valadation.png)
-   [JS Validator](https://codebeautify.org/jsvalidate) - [Results](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/Valadation%20pictures/Javascript%20Valadation/javascript_val.png)
-   [Lighthouse Report](https://developers.google.com/web/tools/lighthouse#devtools) - [Results](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/Responsive/lighthouse_valadation.png)
-   [AmIResponsive](http://ami.responsivedesign.is/?url=https%3A%2F%2Fstar-trade.herokuapp.com%2F) - was used to check how the application looks on other devices - [Results](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/Responsive/responsive_picture.png)


### Testing Section


#### Frequent User Goals

- As a User, I would want each user to have a easy way of listing thier items with ease. 
- Also having those frequent users reccomend thier friends as well, thus having more items too look through.


  
### Further Testing

-   The Website was tested with Google Chrome Dev Tools.
-   The website was viewed on a variety of devices such as 
    Desktop (1600x992px), Laptop (1280x802px ), Ipad (768x1024px), iPhone 5 (320x480px). 
-   Friends and family members were asked to create usernames and passwords and list their own trades. 

### Manual Testing
-   When working on the accordian function where the trades reside I ran into a problem where the accordian acted as one big one. I got in contact with student support, and they reccomend that I create a loop index. When doing that I was able to have each item act independent from one eachother.
So after some digging around I came across a Zoom property where the div is zoomed out and then the game board is able to be viewd on any decive.
-  At the start of the project I ran across a issue of misnaming a variable in the database. Was able to find the mistake and get things going again.
-  When adding the tooltip from bootstrap I was having problems seeing it. I found out it needs to be intialized in the scipt.js file. 
- Another problem that happend at the start was with the pip commands. It wasnt allowing any commands, then I found it needed a upgrade. After the upgrade everything worked.
### Known Bugs

-   Sometimes when loading in the application there is a scollbar on the right side.





## Life Cycle

-   ### Design
    -   #### Color Scheme
        -   The main colors used are gray, off-white, and black
    -   #### Typography
        -   Roboto Slab font is the main font used throughout the site. 

*   ### Wireframes

    -   StarTrade desgin wireframe - here is where I mapped out what the application will look like [View](https://github.com/nickl98/StarTradeMS3/tree/master/static/images/Wireframes)

    - Database wireframe - here is where all the database varibles are listed and how they connect to eachother [View](https://github.com/nickl98/StarTradeMS3/blob/master/static/images/Database%20Diagrams/database.png.jpg)


    

## Features
### Existing Features
-   Up-to-date with current trades from all users on the homepage.
-   The Admin has the function for deleting trade types/consoles.
-   Users are able to sign up and logout anytime. Thanks to the Navagation bar above.
### Features left to Implement
- I would like to create a automnated chat assistant for any users that may have any issues. 
- Sometime down the road I would like for this application do be on the app store for Andriod and IOS.
- Another great feature to have on the application would be more admin functions, from edititng anybodys trades, to deleting potentialy scam listings.

## Deployment

### Heroku

The project was deployed to Heroku.

- You can view the project on any device you may use, just use the link at the top of the page!



## Credits

### Code



-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly using their Grid system, as well as card decks.
 -  [JavaScript:](https://www.JavaScript.com/) JavaScript was used for the Bootstrap tooltip. 

 - [Python 3](https://www.python.org/) pyhton was used for connecting to the database
### Content

-   All content was written by the developer.
-   The CRUD functionality of the python file were used from the Mini-Project from CodeInsitute
-   Grammerly.com was used to check spelling mistakes I overlooked.

