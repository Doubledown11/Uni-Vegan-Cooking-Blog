// JavaScript Code for the Dark Mode Effect 

 


document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ Dark Mode JavaScript file loaded!");

    // Still need to ID how to keep dark mode activated after refreshing the page
    let dark = 0;


    document.getElementById('checkbox').addEventListener('click', function () {
        // Used to toggle the elements which have been altered using .style.<css styling choice here>
        if (dark === 0) {
            dark++
        } else {
            dark--
        }

        console.log('Button click event captured')



        // Header 
        var header = document.getElementById('header_');
        header.classList.toggle('dark_mode_header');



        // Header Text
        var title_text = document.getElementById('Title_Text');
        title_text.classList.toggle('dark_mode_Title_Text');



        // Header Submit Button
        var header_submit_button = document.getElementById('header_submit_button');
        if (dark === 1) {
            header_submit_button.style.color = 'black';
            header_submit_button.style.background = 'silver';
        } else if (dark === 0) {
            header_submit_button.style.color = 'black';
            header_submit_button.style.background = 'rgb(248, 210, 95)';
        }
        
        // header_buttons.classList.toggle('dark_mode_header_button');



        // Header Buttons
        var header_buttons = document.getElementsByClassName('btn btn-secondary');
        for (let x = 0; x<header_buttons.length;x++) {
            if (dark === 1 ) {
                header_buttons[x].classList.toggle('dark_mode_header_button')
                header_buttons[x].style.color = 'black';
                header_buttons[x].style.background = 'silver';
            } else if (dark === 0) {
                header_buttons[x].classList.toggle('dark_mode_header_button')
                header_buttons[x].style.color = 'black';
                header_buttons[x].style.background = 'rgb(248, 210, 95)';
            }
        };
        // header_submit_button.classList.toggle('dark_mode_header_submit_button');



        // Lines -- TODO WONT CHANGE COLOR AFTER DARK TOGGLE. 
        var line1 = document.getElementById('line1');
        line1.classList.toggle('dark_mode_line1');

        var line2 = document.getElementById('line2');
        line2.classList.toggle('dark_mode_line2');


        // Body  
        var body = document.getElementById('body');
        body.classList.toggle('dark_mode_body');

        var body_CP = document.getElementById('body_CP');
        body_CP.classList.toggle('body_CP_dark_mode');
        


        // Posts Title
        var Posts_Title = document.getElementById('Posts');
        Posts_Title.classList.toggle('dark_mode_Posts_Title');


        

        // Post Urls -- Finish later.
        var post_urls = document.getElementsByClassName('Post_Url');
        //post_urls.classList.toggle('dark_mode_Post_Url');
        for (let x = 0; x<post_urls.length; x++) {
            post_urls[x].classList.toggle('dark_mode_Post_Url');
        };
        // post_urls[0].classList.toggle('dark_mode_Post_Url');
        
        // Post date/category 
        var date_category = document.getElementById('post_date_category');
        date_category.classList.toggle('dark_mode_post_date_category');

        // Post Category Name
        var category_name = document.getElementById('category_name');
        category_name.classList.toggle('dark_mode_category_name');
        
        // Post Body 
        var post_body = document.getElementById('post_body');
        post_body.classList.toggle('dark_mode_post_body');

        // Dark Mode Toggle Title 
        var toggle_title = document.getElementById('toggle_title');
        toggle_title.classList.toggle('dark_mode_toggle_title');

        // Dark Mode Slider 
        // var slider = document.getElementById('slider');
        // slider.classList.toggle('dark_mode_slider');

        // Dark Mode Slider Toggle
        if (dark === 1) {

        } else if (dark === 0) {

        }
        
    });
});