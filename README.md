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


Big Problems: (Hacked.)
Cannot find a working solution to style my Django forms. Unable to add styling to input fields created with Django tags.
	Cant style input fields on login or register. 

Also cant change login or register functionality to any other solution. Am being forced into a solution.

CSS grid view refused to work and now I cant use that to aid with responsive design. I will now have to use execessive media queries.


Found a working solution which uses auth_views
	has weird bug though where it appends a login_submit on each successful login, so when trying to login again it looks for a wrong URL. 



Current TODO:


* do the Spotify background square wiggling thing for the site. Maybe as a background for the blog page base.html. https://business.adobe.com/blog/basics/best-website-design-examples#superlist 

* from the chocolate site on the list at https://business.adobe.com/blog/basics/best-website-design-examples#superlist use the styling on the buttons. on hover the color changes by filling up from one direction and when it fills it empties by draining in the same direction.

* give post URLS with underlines an effect on hover which shrinks the underline to the left until you remove the cursor from chocolate site on above link list


* start with designing responsiveness with CSS media queries once stuck.


* Fix bug with account info change modal on account.html


* Fix titles on Account.html, contact.html
	Underline and size increase to x-large


* Add signout button and modal to change_password (also need to create another JS file for change_password


* Errors need to be returned to the various site forms 
	contact form --> Django debug page when empty form submitted
	change_password form --> Django debug when empty AND test for password change related errors (left change password error styling on page for this)
	forgotten_password --> Django debug when empty and test cases


* Add an images selection with a horizontal carousel --> Take pics of meals.


* Fix signout modal on account.html 
	Can not click outside of the modal to close it?


* Add dark mode to accounts, contact, change password 
	* maybe CSS variable to save dark mode state data (1 or 0) in style.css
		(FINISH THE DARK MODE CODE B4 THO -- I want to be able to save dark mode status so dark mode option is kept through page refresh and new page load)



* Add search icon to top page search input 
	  background-image: url('searchicon.png');




* fix big white space at bottom of every page

* Weird bug on /users/account --> When I try to open the sign-out modal, it opens the account change modal.
	* try bringing the forms into the account page with context dict like with the contact messages container 
	* then rather then creating the forms with HTML code, use Django tags {{form.old_username}} for example

* Password Reset emails to be sent to users 
	* Video from dennis ivy --> got a NoReverseMatch error when trying to send a password reset email from /users/reset_password --> Reverse for password_reset_confirm not found --> Says it is not a valid view function or pattern name.

* Fix login function form has errors and wont redirect to home page but still logs user in, when the password has been discovered in a data breach. 

* Cant display uploaded profile pic for admin user 
	* I got stuck and am now trying to use JS to fetch the URL of the view needed to retrieve the picture from media.

* Ensure enquiry display on admin account allows message values to wrap and fit with the amount of text within -- Test with long message values.



* use js to dynamically adjust the padding at bottom of the my_account_container on account based on the number of enquiries made 


* fix signout modal on account page --> Check all pages with modals. When trying to open signout modal, the other modal is being opened. Prob just have to clean up styles.css

* Change login page template to be like registration page template --> Check how posts on base.html were passed from view to template

* Fix styling bug (Cant move styles on login/registration to the style.css page?) maybe try removing all js ties to templates?
	* Unable to get styles to change from inside style.css

*login and registration page need errors from views displayed to the templates

* Fix broken dark mode switch on login and fix the auto turn off dark mode on when moving into register.html from login.html
	* Maybe store current dark mode status as an entry in a cache!

* Links from posts categories need to link to a page with all the posts related to a given category

* Need to be able to add multiple categories to a post

* Admin Page for web based add/remove blog posts

* Need to confirm account email changes with a confirmation email to both new and old emails
* also need to send confirmation emails when user changes password
* Account lockouts, password reset timers (# times reset in 24 hours), 

* give users options to Delete their accounts 


* After failed and successful chaging passwords, we are directed to users/account/change_password_page/change_password_page from users/account/change_password_page ---> Common bug keeps appearing with my forms.



