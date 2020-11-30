<h1>The Dice Depot 🎲</h1>

<p>The Dice Depot is an e-commerce website, designed to be the best destination for fans of Tabletop Gaming, 
giving them both a wide variety of the most popular and up to date titles, 
and the ability to sell their unwanted games to us.</p>

<br>

<h2>User Experience</h2>

<h3>Project Goals</h3>

<p>The primary goals of The Dice Depot are to give Tabletop Gaming fans an easy one stop shop. It aims to have an easy to navigate selection of the most popular current board
games, and also aims to allow user to communicate with the site admins in order to sell their unwanted games in an efficient manner.</p>

<h3>User Goals</h3>
<ul>
    <li>An up to date selection of the most popular current titles for easy purchase, such as Scythe, Spirit Island and Gloomhaven</li>
    <li>The ability to create an account to check on order statuses and past orders</li>
    <li>Easy to navigate interface, along with the ability to easily organise games by the user's choice of category</li>
    <li>A responsive site that works on tablet, mobile and desktop</li>
    <li>The ability to sell unwanted games to the store</li>
</ul>

<h3>Admin Goals</h3>
<ul>
    <li>Sleek and responsive site design</li>
    <li>An easy to manage payment system</li>
    <li>The ability to update and delete products from the store library</li>
    <li>A form that requires evidence of the quality of games, thereby allowing the right to refuse games that are in unacceptable condition.</li>
</ul>

<h3>User Stories</h3>

<ul>
    <li>As a user, I expect to be able to easily log in to my profile to be able to check on the status of past and present orders.</li>
    <li>As a user, I would like to be able to sell my unwanted games.</li> 
    <li>As a user, I would like to know the price that I would be offered for selling games, without being pressured into commiting to selling for that price.</li>
    <li>As a user, I would like the ability to be able to keep a profile to save my details for faster checkouts.</li>
</ul>

<h2>Wireframes</h2>

<ul>
    <li><a href="https://i.imgur.com/Wnoc6ZP.png" target="_blank">Front Page - Desktop</a></li>
    <li><a href="https://i.imgur.com/ijVf2QB.png" target="_blank">Shop - Desktop</a></li>
    <li><a href="https://i.imgur.com/2xb0GQS.png" target="_blank">Sell - Desktop</a></li>
    <li><a href="https://i.imgur.com/TwQcKiC.png" target="_blank">Profile - Desktop</a></li>
    <li><a href="https://i.imgur.com/Jgrhrfw.png" target="_blank">Basket - Desktop</a></li>
    <li><a href="https://i.imgur.com/qel7SIv.png" target="_blank">Front Page - Tablet</a></li>
    <li><a href="https://i.imgur.com/CEspLjE.png" target="_blank">Shop - Tablet</a></li>
    <li><a href="https://i.imgur.com/wxQWVlY.png" target="_blank">Sell - Tablet</a></li>
    <li><a href="https://i.imgur.com/ijCzcUy.png" target="_blank">Profile - Tablet</a></li>
    <li><a href="https://i.imgur.com/MoBgsvf.png" target="_blank">Basket - Tablet</a></li>
    <li><a href="https://i.imgur.com/tqNqMNy.png" target="_blank">Front Page - Mobile</a></li>
    <li><a href="https://i.imgur.com/RrPEZCw.png" target="_blank">Shop - Mobile</a></li>
    <li><a href="https://i.imgur.com/LGDrhNo.png" target="_blank">Sell - Mobile</a></li>
    <li><a href="https://i.imgur.com/CAYBXmN.png" target="_blank">Profile - Mobile</a></li>
    <li><a href="https://i.imgur.com/wsAggTv.png" target="_blank">Basket - Mobile</li>
</ul>

<h2>Design Choices</h2>

<h3>Fonts</h3>

<p>The primary font of The Dice Depot is Spectral SC, imported from Google Fonts. I wanted a font that was clearly stylised, but still looked professional
and remained easy to read. Spectral SC fit this criteria, as well as retaining a regal, fantasy-esque look, akin to the rulebooks of many fantasy based games.
As such, I felt that this was a perfect fit.</p>

<h3>Icons</h3>

<p>All icons are imported from FontAwesome. I decided to keep it simple in terms of icons so as to keep the page readable and easy to navigate. I opted to use a shopping
cart icon for the user's cart, and the profile icon for their profile page, and retained a clear, readable navbar.</p>

<h3>Background Image</h3>

<p>I wanted a background that would convey the purpose of the site, but that wasn't too busy or difficult to look at. I opted for a nice, clean blue background with a set of dice on
the right hand side, in order to keep the front page minimalist, but to still imply the purpose of the site to the user. The image was taken from Unsplash, which is a royalty free image library.</p>

<h3>Colour Scheme</h3>

<p>Similarly to the background image, I wanted the colour scheme to be fun, but not too busy.</p>

<ul>
    <li>Primary Colour : #6F732F; "Spanish Bistro" - A variant in the Phthalo Green palette that ebbs slightly towards yellow. Again, a bright colour but one that is easy on the eyes.</li>
    <li>Secondary Colour : #f5cb42;  - A royal Gold that contrasts well with the main site image and evokes a color scheme found in many available games</li>
    <li>White Colour : #ffffff; "White" - Shows up well against the Phthalo Green</li>
    <li>Black Colour : #000; "Black" - Standard CSS black</li>
    <li>Danger Colour : #ff0000; "Red" - Used to denote required elements and errors</li>
</ul>

<h2>Data Models</h2>

<h3>The Product Model</h3>

| Name   | Key In API   | Validation    | Data Type   |
|-  |-  |-  |-  |
| Game  | name  | max_length=254, default="" |  CharField  |
| Year  | year_published  | max_digits=4 |  IntegerField  |
| Players  | (foreign_key)  | max_digits=3 |  ForeignKey  |
| Age  | (foreign_key)  | max_digits=2 |  ForeignKey  |
| Description  | description  | default="some string" |  TextField  |
| Image  | image_url  | upload_to"static/images" |  ImageField  |
| RRP  | msrp  | max_digits=6, decimal_places=2, default=0.0 |  DecimalField  |
| Price  | price  | max_digits=6, decimal_places=2 |  DecimalField  |

<h3>The Age Model</h3>

| Name   | Key In API   | Validation    | Data Type   |
|-  |-  |-  |-  |
| Age  | min_age  | default="0.0" |  IntegerField  |

<h3>The Players Model</h3>

| Name   | Key In API   | Validation    | Data Type   |
|-  |-  |-  |-  |
| Players  | min_players  | default="0.0" |  IntegerField  |
| Players  | max_players  | default="0.0" |  IntegerField  |

<h3>The Sell Model</h3>

| Name   | Key In db   | Validation    | Data Type   |
|-  |-  |-  |-  |
| Game Name  | game_name  | max_length=254, blank=False |  CharField  |
| Email  | email  | max_length=254, null=False, blank=False |  EmailField  |
| Sealed  | sealed  | help_text="Only tick this box if your game is still contained in it's original wrapping", null=True |  BooleanField  |
| Condition  | condition  | max_length=25, choices=GAME_CONDITION, default='good' |  CharField  |
| Game Description  | game_description  | max_length=512, default="Please provide a quick description of your game's quality", null=True, blank=True |  TextField  |


<h3>The Order Model</h3>

| Name   | Key In db   | Validation    | Data Type   |
|-  |-  |-  |-  |
| User  | user  | User, on_delete=models.PROTECT |  ForeignKey  |
| Full Name  | full_name  | max_length=50, blank=False |  CharField  |
| Phone Number  | phone_number  | max_length=20, blank=False |  CharField  |
| Country  | country  | blank_label='Country *', max_length=40, blank=False |  CharField  |
| Postcode  | postcode  | max_length=40, blank=False |  CharField  |
| City  | city  | max_length=40, blank=False |  CharField  |
| Address Line 1  | address_line_1  | max_length=50, blank=False |  CharField  |
| Address Line 2  | address_line_2  | max_length=50, blank=False |  CharField  |
| Date  | date  |  |  DateField  |

<h3>The OrderItem Model</h3>

| Name   | Key In db   | Validation    | Data Type   |
|-  |-  |-  |-  |
| Order  | order  | Order, null=False |  ForeignKey  |
| Product  | product  | Product, null=False |  ForeignKey  |
| Quantity  | quantity  | blank=False |  IntegerField  |


<h2>Features</h2>

<h3>Current Features</h3>

<ul>
    <li>Account creation through Django, allowing users to login and check past orders</li>
    <li>The ability for user to update their profile information</li>
    <li>Dropdown bar that organises products by specific criteria such as Publisher and minimum recommended age</li>
    <li>Checkout function created using the Stripe API</li>
    <li>Full game catalogue created using the Board Game Atlas API</li>
    <li>A shopping cart that allows users to amend the items currently in their basket</li>
    <li>A from on the Sell page that allows users to post information regarding a game for the site owner to review</li>
</ul>

<h3>Features to implement in the future</h3>

<ul>
    <li>A rewards system, giving cutomers points based on their past purchases</li>
    <li>The ability for users to reset forgotten or lost passwords</li>
    <li>The ability for customers to check the status of the game they want to sell using their profile</li>
    <li>The ability to attach an image to the sell form</li>
    <li>The ability to view the progress of games being sold in a profile</li>
</ul>

<h2>Technologies Used</h2>

<strong>Languages:</strong>

<ul>
    <li><a href="https://html.spec.whatwg.org/" target="_blank">HTML</a></li>
    <li><a href="https://www.w3.org/Style/CSS/Overview.en.html" target="_blank">CSS</a></li>
    <li><a href="https://www.javascript.com/" target="_blank">JavaScript</a></li>
    <li><a href="https://www.json.org/json-en.html" target="_blank">JSON</a></li>
    <li><a href="https://www.python.org/" target="_blank">Python</a></li>
</ul>

<strong>Tools & Libraries:</strong>

<ul>
    <li><a href="https://jquery.com/" target="_blank">jQuery</a></li>
    <li><a href="https://git-scm.com/" target="_blank">Git</a></li>
    <li><a href="https://getbootstrap.com/" target="_blank">Bootstrap</a></li>
    <li><a href="https://fontawesome.com/" target="_blank">Font Awesome</a></li>
    <li><a href="https://fonts.google.com/" target="_blank">Google Fonts</a></li>
    <li><a href="https://en.wikipedia.org/wiki/Pip_(package_manager)" target="_blank">PIP</a></li>
    <li><a href="https://www.djangoproject.com/" target="_blank">Django</a></li>
    <li><a href="https://stripe.com/docs/api" target="_blank">Stripe</a></li>
    <li><a href="https://gunicorn.org/" target="_blank">Gunicorn</a></li>
    <li><a href="https://www.gitpod.io/" target="_blank">Gitpod</a></li>
</ul>

<strong>Databases:</strong>

<ul>
    <li><a href="https://www.postgresql.org/" target="_blank"></a>PostgreSQL - Production</li>
    <li><a href="https://www.sqlite.org/index.html" target="_blank"></a>SQlite3 - Development</li>
</ul>

<h2>Testing</h2>

<p>The Dice Depot has been coded and tested on Mozilla Firefox and Google Chrome internet browsers, on both a Macbook Pro and a desktop PC -it runs identically on both.
The code for The Dice Depot was written in Gitpod</p>

<p>All of the model forms have been tested to ensure that they correctly post to the database. The JSON files have all been validated numerous times</p>

<h3>Specific App Testing</h3>

<h2>Home</h2>

<h3>Planning Stage</h3>

<p>The home page needed to have links to all the other relevant functions, and very little else.</p>

<h3>Implementation</h3>

<p>After deciding on a background image, the basic structure was created, along with a navbar and mobile nav. Hyperlinks were originally left empty until other
apps were created, as this can cause Django to throw error messages as it looks for things that don't exist.</p>

<h3>Testing</h3>

<p>Different app links were tested as they were created, and I'm happy that all of these links work.</p>

<h2>Product Rendering</h2>

<h3>Planning Stage</h3>

<p>Setting up the products app was a vital first step, as the majority of the other functionality revloves around them.</p>

<h3>Implementation</h3>

<p>The first step was to obtain the necessary product information, which I found in the Board Game Atlas API. Though very dense in information, this was a rather cluttered API, 
 and much time was spent refactoring and validating the json to get it to it's current stage. Following this, the products were uploaded to the Django database by attaching them
 to their requisite models. Once this was done, it was a matter of presenting the products well on the main products page, and including all of the relevant information
 on the product description page.</p>

<h3>Testing</h3>

<p>All of the products look the same in the view on the all products page, and contain the information required on their individual product description pages.</p>

<h2>Profile Functions</h2>

<h3>Planning Stage</h3>

<p>The profile functions are a vital part of any online store. Users need to be able to log in, log out and save all of their information for future orders.</p>

<h3>Implementation</h3>

<p>As Django already contains a user database, this was kept relatively simple. Once allauth was installed in the project (providing a ready to use set of login and register pages),
it was simply a matter of creating the necessary forms and models in order to ensure these were being pushed to the database correctly.</p>

<h3>Testing</h3>

<p>All login, register and log out functions are working and redirecting as they should, and user information is stored in their profiles for future use.</p>

<h2>The Sell App</h2>

<h3>Planning Stage</h3>

<p>The Sell app is designed for users to quickly and easily send an email to the admin, with details of a game that they want to sell. The key goals here
was to make the form clean and easy to use so as not to dissuade the user.</p>

<h3>Implementation</h3>

<p>The Sell app simply needed a form and a model to be efficient, due to there being no data to load from the admin side. Once the model and form were created,
it became a matter of creating a view that would render the form, and let the user know that their details have been received.</p>

<h3>Testing</h3>

<p>Currently, the Sell form acts more as a contact form of sorts. Originally there was an image field to allow user images to be uploaded for the use of the admin in revieweing the product.
Unfortunately, this had to be removed due to time constraints. The app currently does not require the user to have a profile in order to use the form, as I felt that some users may not
want to sign up to a service that they may end up not using - dependent on the offer from the admin. The user is given a toast notification to advise them that their details have been received,
and they will be contacted upon product review.</p>

<h2>Stripe Payments</h2>

<h3>Planning Stage</h3>

<p>The most important aspect of the online store, is to make sure that user's can actually buy things from the store. Due to it's relatively simple information, as well
as it's additional wealth of reccommended CSS and JS, Stripe was the most efficient choice.</p>

<h3>Implementation</h3>

<p>Once signed up to Stripe, the implementation of it is fairly well explained by the Stripe documentation. Once the Stripe JS link has been added,
functions were then created to pass all relevant user and order information to Stripe in order for payment to succeed. As I leanred during bug fixing, it was vital to ensure that
all the data matches the data that Stripe is expecting - otherwise the payment intent will hit Stripe, but your console will receive an error, as Stripe has been unable
to save it's reuqired forms.</p>


<h2>Bugs</h2>

<h3>The Sell Form</h3>

<ul>
    <li><strong>Issue : </strong>I ran into continual issues when trying to get the Sell form to post to the database.</li>
    <li><strong>Solution : </strong>Initially, I was trying to render the context before I had rendered any sort of form, which meant that the form simply didn't appear
    in the site. Rendering the context after checking the forms validity fixed this. Additionally, the Sell model originally contained an image field, which can be seen in the commits. 
    Unfortunately, due to time constraints, this had to be removed. An error was being thrown up by the form itself, claiming that no image was attached, even when there was. Setting the field to not require a picture didn't help,
    and it was stopping the form from hitting the database, so this will have to be added at a later date.</li>
</ul>

<h3>Navbar Link</h3>

<ul>
    <li><strong>Issue : </strong>The actual link to the sell form worked on the index link,
    but not on the navbar link.</li>
    <li><strong>Solution : </strong>This was a simple one that took far too long to spot - I had rendered the section of the nav as a dropdown. Upon
    removing this value, the link worked perfectly.</li>
</ul>

<h3>Models - The JSON files</h3>

<ul>
    <li><strong>Issue : </strong>I was initially unable to get the value of the age and players models to appear within the products model as foreign keys.</li>
    <li><strong>Solution : </strong>This took some time to wrap my head around, but soon made perfect sense. After creating the products model, I assumed if I made seperate json files with
    matching pk's, that all of these products would then 'sync up'. In essence,iIn my age and players models,I was trying to match the number of ages and players to the pk of the products in my products.json. 
    After several chats with Miklos, I understood that I needed to create a set number of fields, each with a unique value, then place those pk's in the products model - with the pk in this
    case referencing a value found in both the players and age json files. For example, if a product has an age of 1, this actually references the value 8, as has been set in the age.json file.</li>
</ul>

<h3>Secure Checkout</h3>

<ul>
    <li><strong>Issue : </strong>Upon clicking 'secure checkout', my site did nothing, and just stayed on the same screen with all of the customer info still on screen.</li>
    <li><strong>Solution : </strong>This was the toughest spot - Stripe was giving me a 400 error in the console, which meant the data being sent to Stripe didn't match what it was
    expecting. After checking that the Stripe Javascript included all the correct fields, I eventually found that the Country field was causing the issue. It was set in a manner
    that didn't abbreviate countries to their 2 letter acronym for Stripe, which was causing the form not to save. Adding in blank_label='Country *' fixed this problem.</li>
</ul>

<h3>Product Admin</h3>

<ul>
    <li><strong>Issue :</strong>The admin functions were working, but still behaving strangely. When the admin added a product to the
    database, or edited an existing product, Django would give an error code to do with the product description view. Strangely, the add or edit 
    function would still complete despite this error.</li>
    <li><strong>Solution :</strong>Due to time constraints, I made the decision to change the redirect so that if a superuser clicks on a product,
    they are redirected to the edit product view. This bug was a particular struggle, as the product description view was only throwing
    an error for superusers - there are no issues with standard users. Print statements were added to the view, and the html was commented
    out so that I could see any errors in the terminal, but the problem consistently pointed to some sort of issue in the relationship
    between the superuser and the product description view that I was sadly unable to figure out. By sending the superuser to the edit
    product view, it at least means that the superuser can view product details on the store front.</li>
</ul>

<h2>Deployment</h2>

<h3>Local Deployment</h3>

<p>The following installs are required in order to deplot The Dice Depot locally:</p>
<ul>
   <li>A development environment. I reccommend VS Code - though Dice Depot was completed in Gitpod.</li> 
   <li>PIP</li>
   <li>Python</li>
   <li>Git</li>
</ul>
<p>Additionally, a developer account with Stripe is required.</p>

<p>1 - From the terminal in your IDE, run :</p>

```
git clone https://github.com/Scrambles86/dice_depot
```

<p>2 - Open the dice_depot folder, and in the terminal enter : </p>

```
python3 -m .venv venv
```

<p>Followed by : </p>

```
.venv\bin\activate
```

<p>This will activate your virtual environment.</p>

<p>3 - In order to ensure that the project has all of it's required settings, use the terminal to enter : </p>

```
pip3 -r requirements.txt
```

<p>4 - You will then need a file to keep your secret information. If using Gitpod, you can set these in your settings in the
main workspace area, and then reference them in your projects settings file. You can use an env.py file, but this will make your secret information
visible to anyone who accesses your project.</p>

<p>5 - In your terminal, enter the following commands : </p>

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

```
python3 manage.py loaddata age
```

```
python3 manage.py loaddata players
```

```
python3 manage.py loaddata products
```

<p>This will install the models and then load the product data from the json files. It's important to do this in this order, as the json data wont load without
their requisite models.</p>

<p>6 - Create a superuser for your admin page using :</p>

```
python3 manage.py createsuperuser
```
<p>You can now run your project locally from the terminal by typing :</p>

```
python3 manage.py runserver
```

<h3>Heroku Deployment</h3>

<p>1 - Create your requirments.txt file using : </p>

```
pip3 freeze > requirements.txt
```

<p>2 - Create a Procfile (Make sure it's a capital P!) and push the files.</p>

```
echo web: python3 app.py > Procfile
```

<p>3 - In Heroku, click 'create app'</p>

<p>4 - On the 'Deploy' tab, click 'Github' under 'Deployment method'</p>

<p>5 - On the Settings tab, click 'reveal config vars'</p>

<p>6 - Set your DATABASE_URL, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY and save them.</p>

<p>7 - On the main dashboard, click 'Deploy' and wait for the build to finish before opening the app.</p>

<h2>Media & Game Content</h2>
<ul>
    <li>The main background image was found in Unsplash</li>
    <li>All other images, and the game information are taken from the Board Game Atlas API</li>
</ul>

<h2>Acknowledgements</h2>

<p>This project would not have been possible without <a href="https://github.com/ckz8780" target="_blank">ckz8780</a> and his Boutique Ado project. This was an exemplary walkthrough, and was vital
in my implementation of Stripe, as well as understanding of the nature of how individual apps work within Django. 
Much of the code in this project is an adaptation of his fantastic example.</p>

<p>As always, I have to thank my mentor <a href="https://github.com/Eventyret">Simen</a>, who throughout the course has provided encouragment, the occasional kick up the backside,
and endless knowledge and troubleshooting. He is an asset to the Code Institute.</p>

<p>And a huge thanks to all of the Code Institue tutors, particulary Miklos, Scott and Michael for this project. I have no doubt that they'll be glad to see the back of me, 
but they were still happy to help as much as they could at all hours.</p>

<h2>Disclaimer</h2>

<p>The contents of this website are for educational purposes only. Some game details may differ.</p>

