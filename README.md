# Uni-Vegan-Cooking-Blog
A short blog covering some recipes used during my time in university.

NOTE: This is unfinished.

Utilized Django (Python), JavaScript, HTML, CSS and bootstrap. 

Created a users app which allows for users registration, sign in, and sign out.

JavaScript was used to:
    give the site title a typewriter effect, 
    give the site a dark mode,
    and create a modal pop-up when trying to sign out, and to change account information


Also plan to use CSS media queries to ensure the site is responsive to various heights and widths.



Current TODO:

* Password Reset emails to be sent to users 


* Cant display uploaded profile pic for admin user 
	* I got stuck and am now trying to use JS to fetch the URL of the view needed to retrieve the picture from media.

* Fix frontend of enquiry display code on account page



* use js to dynamically adjust the padding at bottom of the my_account_container on account based on the number of enquiries made 


* Fix signout modal close button on base and other pages

* Change login page template to be like registration page template --> Check how posts on base.html were passed from view to template

* Fix styling bug (Cant move styles on login/registration to the style.css page?) maybe try removing all js ties to templates?
	* Unable to get styles to change from inside style.css

*login and registration page need errors from views displayed to the templates

* Fix broken dark mode switch on login and fix the auto turn off dark mode on when moving into register.html from login.html

* Links from posts categories need to link to a page with all the posts related to a given category

* Need to be able to add multiple categories to a post

* Admin Page for web based add/remove blog posts

* Need to confirm account email changes with a confirmation email to both new and old emails
* also need to send confirmation emails when user changes password
* Account lockouts, password reset timers (# times reset in 24 hours), 

* give users options to Delete their accounts 


* After failed and successful chaging passwords, we are directed to users/account/change_password_page/change_password_page from users/account/change_password_page ---> Common bug keeps appearing with my forms.


