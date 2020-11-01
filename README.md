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
    <li>A fast estimate on sell price that doesn't require any commitment from the user</li>
</ul>

<h3>Admin Goals</h3>
<ul>
    <li>Sleek and responsive site design</li>
    <li>An easy to manage payment system</li>
    <li>The ability to update and delete products from the store library</li>
    <li>A form that requires photographic evidence of the quality of games, thereby allowing the right to refuse games that are in unacceptable condition.</li>
    <li>A robust forumla to determine prices offered for second hand games</li>
</ul>

<h3>User Stories</h3>

<ul>
    <li>As a user, I expect to be able to easily log in to my profile to be able to check on the status of past and present orders.</li>
    <li>As a user, I would like to be able to sell my unwanted games.</li> 
    <li>As a user, I would like to know the price that I would be offered for selling games, without being pressured into commiting to selling for that price.</li>
    <li>As a user, I would like the ability to be able to sort games by length of play, publisher and recommended age range.</li>
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
    <li>Primary Colour : #f5cb42; "" - A royal Gold that contrasts well with the main site image and evokes a color scheme found in many available games</li>
    <li>Secondary Colour : #6F732F; "Spanish Bistro" - A variant in the Phthalo Green palette that ebbs slightly towards yellow. Again, a bright colour but one that is easy on the eyes.</li>
    <li>Tertiary Colour : #B38A58; "Camel" - A calm yellow used for highliting agaisnt the green background whilst still blending somewhat.</li>
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
| Min. Players  | min_players  | max_digits=3 |  IntegerField  |
| Max. Players  | max_players  | max_digits=3 |  IntegerField  |
| Min. Age  | min_age  | max_digits=2 |  IntegerField  |
| Description  | description  | default="some string" |  TextField  |
| Image  | image_url  | upload_to"static/images" |  ImageField  |
| RRP  | msrp  | max_digits=6, decimal_places=2, default=0.0 |  DecimalField  |
| Price  | price  | max_digits=6, decimal_places=2 |  DecimalField  |

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
    <li>A from on the Sell page that allows users to enter information regarding a game that send them back an estimate price</li>
</ul>

<h3>Features to implement in the future</h3>

<ul>
    <li>A rewards system, giving cutomers points based on their past purchases</li>
    <li>The ability for users to reset forgotten or lost passwords</li>
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

<h2>Deployment</h2>