# BuddyTalk

**BuddyTalk** is an AI-powered virtual assistant tailored to help you efficiently manage your Google Calendar. It automates calendar tasks such as event creation, modification, and deletion, allowing you to focus on more important things. Whether you prefer using voice commands or traditional input, BuddyTalk provides a seamless experience, similar to popular assistants like Siri and Google Assistant.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Challenges and Future Improvements](#challenges-and-future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Core Features
- **Create Events**: Add new events to your Google Calendar effortlessly through voice or text input.
- **Read Events**: Ask BuddyTalk to read out your daily, weekly, or specific calendar events.
- **Update Events**: Modify existing events, change dates, times, or descriptions.
- **Delete Events**: Easily remove an event from your Google Calendar.
- **Text-to-Speech & Speech-to-Text**: Supports voice interactions for hands-free operations.
- **Event Overviews**: Summarizes upcoming events in a simple and organized format.

### Unique Features
- **Voice-Controlled Operations**: Interact with BuddyTalk entirely through speech commands.
- **Seamless Google Calendar Integration**: Sync your Google account and let BuddyTalk handle the rest.
- **Cross-Platform**: Available via web browser or API integration, making it accessible from various devices.

---

## Technologies Used

- **Python**: Main programming language for backend and logic.
- **Flask**: Lightweight web framework to handle routing, requests, and responses.
- **Google Calendar API**: Manages user calendar events via API integration.
- **Gunicorn**: WSGI HTTP server to serve the Flask application.
- **SpeechRecognition**: Converts speech commands into text.
- **Pyttsx3**: Text-to-speech engine that enables BuddyTalk to speak.
- **Dotenv**: Handles environment variables securely.
- **ALX Servers**: Cloud platform used to deploy the application.
- **Nginx**: Used as a reverse proxy to manage traffic (if required in advanced deployment).
  
---

## Architecture

BuddyTalk follows a simple, yet effective architecture:

### Frontend
- **Voice Input Interface**: Allows users to interact using voice commands.
- **Forms & Buttons**: Provides an alternative way to interact via text or buttons when voice isn’t feasible.

### Backend
- **Flask Application**: Handles HTTP requests and manages routes such as creating, reading, updating, and deleting events. It also serves the frontend static files.
- **Google Calendar API**: Directly communicates with the Google Calendar to fetch or manipulate event data.
- **Speech-to-Text Processing**: Converts voice commands into actionable text using SpeechRecognition.
- **Text-to-Speech**: Communicates responses back to the user using Pyttsx3 for voice output.

### External Integrations
- **Google Calendar API**: Centralized to manage and manipulate events.
- **OAuth2 Authentication**: Secures user access to their Google Calendar data.

---

## Installation

### Prerequisites
- Python 3.11+
- Google API credentials (Google Developer Console with Calendar API enabled).
- Virtual environment for package management.
- (Optional) Nginx for deployment in production environments.

### Steps

1. **Clone the repository**:
   ```
   git clone https://github.com/dabetterman/buddytalk.git


2. **Navigate to the project folder**:
    ```
    cd buddytalk

3. **Set up virtual environment**:
    ```
    python3 -m venv venv
    source venv/bin/activate

4. **Install dependencies**:
    ```
    pip install -r requirements.txt

5. **Configure environment variables**:

Create a .env file in the project root.
Add the following variables:
    ```
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
    GOOGLE_REFRESH_TOKEN=your_refresh_token
    FLASK_APP=app.py
    FLASK_ENV=development

6. **Run the application**:
    ```
    flask run

Challenges and Future Improvements

**Challenges**

Ensuring reliable voice recognition, especially in noisy environments.

Handling Google API rate limits efficiently.

Managing user authentication tokens securely.

**Future Improvements**

Multi-Language Support: Expanding to support multiple languages for global users.

Additional Services: Integration with other Google services like Gmail or Google Tasks.

Improved UI: Enhancing the frontend for a more user-friendly experience.

Mobile App: Create a companion mobile app for more accessibility.

***Contributing***

Contributions are always welcome! If you have suggestions or improvements, feel free to create an issue or submit a pull request.

**How to Contribute**

1.Fork the repository.

2.Create a new feature branch (git checkout -b feature/new-feature).

3.Commit your changes (git commit -am 'Add new feature').

4.Push to the branch (git push origin feature/new-feature).

5.Create a new Pull Request.

**License**

This project is open source.

**Contact**

For any inquiries or feedback, please reach out:

Ebrahim Rhode
Email: 1ebrahimr@gmail.com
GitHub: https://github.com/dabetterman