# Hasslefree.ie
 
## Overview
Website created for a people who want to advertise their products e.g. cars,servieces, clothing etc .
Interactive Frontend Development; design focused on simplicity and user friendlyness. 

### Users
As a user I should be able to :
-see the homepage with all the products.
-see the main navigation bar with filters where I am able to search by selecting different categories/locations and search for the product using search bar
-select the order of the product by the date and price
-to register, login, log out see my cart(with orders) 
-add product to my cart
-to pay for my orders, and remove my orders
-I can see my profile with picture, details and transactions
-when I am loged in I am able to add/delete/update my own adds etc
-be able to access a new password when I forgot the previous one




As a user who whats to add new product I should:
see a responsive form
be able to add the: titile, description, category, location, price, quantity, picture
see the submit button

As a user who has product:
I should be able to add it, delete it, update it

As a user who wants to buy a product:
I should be able to look for it by price, the date, category, location, word.I should by able to add it to the cart, adjust the quantity and after pay for it 
 
### What is this website for?
Website is aiming:
-at all age audience
-people who want to sell their products
-people who are looking for a specific item or serviece 
The purpose of this website is for the vistor to be able to look for the product and safely sell and/or buy products. 

### How does it work
Based on Bootstrap 4.0, Django 2.0 framework.
The site uses:Bootstrap style with some customizations, Javascript,JQuery, HTML and CSS.
Additional: Stripe to proccess payment, AWS to store the static files and Heroku to deploy 


## Features
 
### Existing Features
- Navbar - enables visitor to: 
    -login,
    -logout,
    -register,
    -go back to homepage, 
    -see all adds, 
    -see the shopping cart
    -choose the location and categories from the dropdown menu
    -order by: price and the date 
    -when user is loged in he can add new product
    -when user click on the logo it takes him to the homepage
- Home page: 
    - contains project pictures, 
    - title, price amount of the product,
    - user is able to add the product to the cart and select the quantity.
    - Customer can search for the product in the search bar
-Product page: 
    -contains product picture, title, description, location, category
    -enables user to add it to the cart and select the quantity.
    -when user is loged in he/she can update or delete their own ad
- Footer with links - enables visitor to check socila media
- Register page
    - with form were user is able to create new account with an emial and password
- Login page
    - user is able to ogin with an email and password
    - user is able to reset his passord (in case he/she forgot the password)
    - user is able to request passowrd resert or sign in with the new account

- Cart
    -user is able to see all of the items he selected
    -user is able to change the quantity
    -user is able to checkout once he/she is finished with shopping
    -user is able to go back to the product page and conitniue shopping
- Checkout
    - user has to imput his/her if he wants to purchase the product
    - Using Stripe the payment methd is safe

### Features Left to Implement
- shop mamagment 
- comments section
- posibility to leave the review 

## Tech Used

### Some the tech used includes:
-**Django**
    -Base library used to create the website
- **HTML**, **CSS** and **Javascript** 
  - Base languages used to create website
- [Bootstrap](http://getbootstrap.com/)
    - I used **Bootstrap** to give our project a simple, responsive layout
- [JQuery](https://jquery.com)
    - **JQuery** 

## Testing
- All code used on the site has been tested to ensure everything is working as expected
- Site viewed and tested in the following browsers:
  - Google Chrome
  - Microsoft Edge
  - Mozilla Firefox
- Site was validated with online tools: https://jigsaw.w3.org/css-validator/ and https://validator.w3.org/


## Contributing
All contributions to improving our code and accept pull requests are welcome.
 
### Deployment
1.Clone this repository by opening your Terminal, change the current working directory to the location where you want the cloned directory to be made.
    2.Type $ git clone " https://github.com/JustynaGrze/HassleFree.ie.git" and hit Enter. Your repository will be ready.
3.Please check the requirmets.txt to see learn what should be installed in order for the project to run
4. Live version here: https://hasslefree.herokuapp.com/

## Credits

## Developer
Justyna Grzeszczyk (email:justyna.grzeszczyk91@gmail.com)


### Information
- The information used to create this site was from a number of sources:
    - stack overflow
    - youtube
    - code institute 

### Thank you: 
Marek 
   
