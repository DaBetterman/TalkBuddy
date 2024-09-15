/* ================================ */

        // SIDEBAR

/* ================================ */

let btn = document.querySelector('#btn');
let sidebar = document.querySelector('.sidebar');

btn.onclick = function() {
    sidebar.classList.toggle('active');
}


/* ================================ */

        // FUNCTIONS TO HANDLE EVENTS

/* ================================ */

// Function to fetch general Google Calendar events
function fetchEvents() {
    fetch('/calendar/events')
    .then(response => response.json())
    .then(data => {
        const eventsList = document.getElementById('eventsList');
        eventsList.innerHTML = ''; // Clear the list first
        if (data.events) {
            data.events.forEach(event => {
                const listItem = document.createElement('li');
                listItem.textContent = event;
                eventsList.appendChild(listItem);
            });
        } else if (data.error) {
            console.error('Error fetching events:', data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to fetch public holiday events
function getEvents() {
    fetch('/calendar/public_holidays')
    .then(response => response.json())
    .then(data => {
        const eventsList = document.getElementById('eventsList');
        eventsList.innerHTML = ''; // Clear the list first
        if (data.events) {
            data.events.forEach(event => {
                const listItem = document.createElement('li');
                listItem.textContent = event;
                eventsList.appendChild(listItem);
            });
        } else if (data.error) {
            console.error('Error fetching events:', data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to delete an event by name
function deleteEventbyName() {
    fetch('/calendar/delete_event')
    .then(response => response.json())
    .then(data => {
        const eventsList = document.getElementById('eventsList');
        eventsList.innerHTML = ''; // Clear the list first
        if (data.events) {
            data.events.forEach(event => {
                const listItem = document.createElement('li');
                listItem.textContent = event;
                eventsList.appendChild(listItem);
            });
        } else if (data.error) {
            console.error('Error fetching events:', data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to send text to the backend
function sendText() {
    const text = document.getElementById('textInput').value;

    fetch('/api/speak', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


/* ================================ */

        // SPEECH RECOGNITION SETUP

/* ================================ */

let recognition;
if ('webkitSpeechRecognition' in window) {
    recognition = new webkitSpeechRecognition();
} else if ('SpeechRecognition' in window) {
    recognition = new SpeechRecognition();
} else {
    alert('Speech recognition is not supported in your browser.');
}

// Speech recognition event handlers
if (recognition) {
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    recognition.onstart = () => {
        document.getElementById('startRecognition').disabled = true;
        document.getElementById('stopRecognition').disabled = false;
        console.log('Speech recognition started');
    };

    recognition.onresult = (event) => {
        const speechResult = event.results[0][0].transcript.toLowerCase();
        console.log('Result received: ' + speechResult);
        document.getElementById('textInput').value = speechResult;

        // Regular expressions to match the phrases
        const publicHolidaysRegex = /public holidays/i;
        const listPublicHolidaysRegex = /list.*public holidays/i;
        const holidaysRegex = /holidays/i;

        const calendarEventsRegex = /calendar events/i;
        const listCalendarEventRegex = /list.*calendar events/i;
        const calendarRegex = /calendar/i;
        
        const deleteEventRegex = /delete (an )?event/i;


        // Check for matches and call appropriate functions
        if (publicHolidaysRegex.test(speechResult) || listPublicHolidaysRegex.test(speechResult) || holidaysRegex.test(speechResult)) {
            getEvents();
        } else if (calendarEventsRegex.test(speechResult) || listCalendarEventRegex.test(speechResult) || calendarRegex.test(speechResult)) {
            fetchEvents();
        } else if (deleteEventRegex.test(speechResult)) {
            deleteEventbyName();
        } else {
            sendText();
        }
    };

    recognition.onerror = (event) => {
        console.error('Speech recognition error:', event.error);
    };

    recognition.onend = () => {
        document.getElementById('startRecognition').disabled = false;
        document.getElementById('stopRecognition').disabled = true;
        console.log('Speech recognition ended');
    };
}

// Start speech recognition
function startRecognition() {
    if (recognition) {
        recognition.start();
    }
}

// Stop speech recognition
function stopRecognition() {
    if (recognition) {
        recognition.stop();
    }
}

/* ================================ */

        // PRELOADER

/* ================================ */

const loader = document.querySelector(".loader")

window.addEventListener("load", vanish);

function vanish() {
  loader.classList.add("disappear");
}

/* ================================ */

        // SIGNUP

/* ================================ */


    // Render Google Sign-In button
    function renderGoogleSignInButton() {
        gapi.signin2.render('googleSignInBtn', {
            'scope': 'profile email',
            'width': 200,
            'height': 40,
            'longtitle': true,
            'theme': 'dark',
            'onsuccess': onSignIn,
            'onfailure': onSignInFailure
        });
    }

    // Called when sign in is successful
    function onSignIn(googleUser) {
        var profile = googleUser.getBasicProfile();
        console.log('Logged in as: ' + profile.getName());
        // You can perform additional actions here, like sending the user's ID token to your backend for verification.
    }

    // Called if sign in fails
    function onSignInFailure(error) {
        console.error('Sign in failed: ' + error);
    }


/* ================================ */

        // LOGIN

/* ================================ */


    // Sign out the user
    function signOut() {
        var auth2 = gapi.auth2.getAuthInstance();
        auth2.signOut().then(function () {
            console.log('User signed out.');
            // Redirect or perform other actions after sign out.
        });
    }


/* ================================ */

        // INTERCHANGABLE WALLPAPER

/* ================================ */


const deleteButton = document.getElementsByClassName('deleteButton');
deleteButton.addEventListener('click', () => {
    deleteEventbyName();  // Call your delete event function here
});



/* ================================ */

        // SAMPLE

/* ================================ */


/* ================================ */

        // SAMPLE

/* ================================ */


/* ================================ */

        // SAMPLE

/* ================================ */