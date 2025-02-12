// JavaScript Code for the Typewriter Title Effect 

// Below function as a sleep function --> Allows JavaScript to pause before further code execution.
const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));



async function typewriter(text, i) {
    /* 
    Uses recursion to print text title character by character.  
    */

    for (let i = 0; i < text.length; i++) {
        document.getElementById('Title_Text').innerHTML += text.charAt(i);
        await sleep(50);
    };
};

 


document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ Typewriter JavaScript file loaded!");
        
    let text = 'The Vegan Meals Which Got Me Through University';
    let i = 0;    

    typewriter(text, i);
});

document.addEventListener('')





