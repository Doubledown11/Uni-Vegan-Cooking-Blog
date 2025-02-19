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

* use js to dynamically adjust the padding at bottom of the my_account_container on account based on the number of enquiries made 

* move contact_enquiry_container to blog_admin

* finish displaying 

* fix account button on contact

* finish blog_admin on account

* Finish Photo Upload tool on account/ --> Also remove JS file on this template if not using JS for the functionality.

* can change account information, but have error when trying to route user back to a prior URL --> Account.html is no found.

* throw some stuff on sides of pages (Fake ads, gifs, etc..)

* Fix signout modal close button on base and other pages

* Change login page template to be like registration page template --> Check how posts on base.html were passed from view to template

* Fix styling bug (Cant move styles on login/registration to the style.css page?)
	* Unable to get styles to change from inside style.css

*login and registration page need errors from views displayed to the templates

* Fix broken dark mode switch on login and fix the auto turn off dark mode on when moving into register.html from login.html

* Links from posts categories need to link to a page with all the posts related to a given category

* Need to be able to add multiple categories to a post

* Admin Page for web based add/remove blog posts

* Need to confirm account email changes with a confirmation email to both new and old emails
* also need to send confirmation emails when user changes password
* Account lockouts, password reset timers (# times reset in 24 hours), 

* User profile page with avatar pictures, bio, maybe individual blog sections with fake posts
* Password Reset emails to be sent to users 
* Delete accounts


* At /users/ there is a page with a single button displayed on it saying register.

* After failed and successful chaging passwords, we are directed to users/account/change_password_page/change_password_page from users/account/change_password_page ---> Common bug keeps appearing with my forms.

* contact page needs to have a form like login page which users can submit inquiries by first name, last name, email, inquiry topic, message
	* Need to have inquiry topic as a drop down selection button with a list of possible inquiry topics, if a user's topic is not found have an other option which when clicked will open another input field for the user to add in their topic manually.

* Need contact page to have a padding at the bottom of the page so the divs for each contact method do not go straight to the bottom of the page --> currently adding padding-bottom to contact_header need to change later?


* Need the contact submissions to be sent to my email NO (Keep this code,  but disable it prior to release AND remove my email variable)
	* Have submissions displayed to a admin page like the blog posts are displayed to the main page.


Cache Stuff 
* Randomized URLs per session? --> Doesnt seem like this is something Django is supposed to do. Maybe able to do it with extensive work, will skip for now.



* If I create account pages, use randomized account ID strings in the URL for their locs. 



* Use cryptographic signing to create randomized recover my account URLs
	https://docs.djangoproject.com/en/5.1/topics/signing/
	Send an email docs: https://docs.djangoproject.com/en/5.1/topics/email/


https://docs.djangoproject.com/en/5.1/topics/cache/
Link above shows diff cache types (Not sure what will be needed --> Maybe view cache to catch generated URLs? Maybe template?)
Also shows commands to access the cache data such as we can access model data through shell


