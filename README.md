<h1>The Dice Depot 🎲</h1>

<p>The Dice Dept is an e-commerce website, designed to be the best destination for fans of Tabletop Gaming, 
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
    <li>A form that requires photographic evidence of the quality of games, thereby allowing the right to refuse games that are in unacceptable condition.</li>
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
| Players  | (foreign_key)  | max_digits=3 |  IntegerField  |
| Age  | (foreign_key)  | max_digits=2 |  IntegerField  |
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
| Game Picture  | model_pic  | upload_to='user_game_images/', default='' |  ImageField  |
| Sealed  | sealed  | help_text="Only tick this box if your game is still contained in it's original wrapping", null=True |  BooleanField  |
| Condition  | condition  | max_length=25, choices=GAME_CONDITION, default='good' |  CharField  |
| Game Description  | game_description  | max_length=512, default="Please provide a quick description of your game's quality", null=True, blank=True |  TextField  |

GAME_CONDITION = (
    ('perfect,', 'PERFECT'),
    ('good', 'GOOD'),
    ('well used', 'WELL USED'),
    ('damaged', 'DAMAGED'),
)

<h3>The Order Model</h3>

| Name   | Key In db   | Validation    | Data Type   |
|-  |-  |-  |-  |
| User  | user  | User, on_delete=models.PROTECT |  ForeignKey  |
| Full Name  | full_name  | max_length=50, blank=False |  CharField  |
| Phone Number  | phone_number  | max_length=20, blank=False |  CharField  |
| Country  | country  | max_length=40, blank=False |  CharField  |
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

<h2>Bugs</h2>

<h3>The Sell Form</h3>

<ul>
    <li><strong>Issue : </strong>I ran into continual issues when trying to get the Sell form to post to the database.</li>
    <li><strong>Solution : </strong>Initially, I was trying to render the context before I had rendered any sort of form, which meant that the form simply didn't appear
    in the site. Rendering the context after checking the forms validity fixed this.</li>
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
    <li><strong>Solution : </strong></li>
</ul>

<h3>Delete</h3>

<ul>
    <li><strong>Issue : </strong>The delete from bag function was initially unclickable, and didn't work.</li>
    <li><strong>Solution : </strong></li>
</ul>

<h2>Deployment</h2>
