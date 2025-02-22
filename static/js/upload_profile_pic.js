// JavaScript Code for the Profile Picture Upload  

document.addEventListener('DOMContentLoaded', function () {

    
    console.log('JavaScript for photo form has opened')

    // Detects submission of photo upload and display form
    document.getElementById("change_profile_pic_form").addEventListener("submit", function() {
        console.log("✅ Form submission detected!");
    });
    

    // Check if current user has a profile pic and print that to the page
    fetch('account/account/change_profile_pic/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'  // Add CSRF token if required
        },
        body: JSON.stringify({key:'value'}) // Send data if needed
    })


        .then(response => response.json())  // Convert response to JSON
        .then(ata => {
            console.log(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
        
        // .then(data => {
        //     console.log("✅ Profile Picture Data:", data);

        //     if (data.length > 0) {
        //         document.getElementById("profile_status").innerText = "Profile pictures found!";
        //     } else {
        //         document.getElementById("profile_status").innerText = "No profile pictures available.";
        //     };
        // })
        // .catch(error => console.error("❌ Error fetching data:", error));
    

    // else print the blank_profile_pic.jpg img
    

    

});
