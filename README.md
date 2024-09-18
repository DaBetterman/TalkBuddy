# BuddyTalk

**BuddyTalk** is a virtual assistant designed to help you manage your Google Calendar with ease. Inspired by other popular virtual assistants like Siri and Google Assistant, BuddyTalk specializes in **creating**, **reading**, **updating**, and **deleting** events from your Google Calendar through intuitive voice commands.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Challenges and Future Improvements](#challenges-and-future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Event Management**: Create, read, update, and delete events directly from your Google Calendar.
- **Voice Commands**: Use natural language to interact with your calendar.
- **Text-to-Speech & Speech-to-Text**: Built-in speech recognition and text-to-speech capabilities.
- **Seamless Integration**: Automatically syncs with Google Calendar.

---

## Technologies Used

- **Flask**: Backend web framework for managing HTTP requests.
- **Google Calendar API**: Integration for interacting with the Google Calendar.
- **Pyttsx3**: Text-to-speech engine.
- **SpeechRecognition**: Recognizes voice commands from the user.
- **Gunicorn**: WSGI server for running the Flask application.
- **Render**: Cloud platform for hosting the application.

---

## Architecture

BuddyTalk is a modular application with three main components:

1. **Backend**: Built using Flask, which handles the server-side logic and interacts with Google Calendar API.
2. **Google Calendar API**: Used to manage calendar events (CRUD operations).
3. **Voice Processing**: Utilizes `SpeechRecognition` for interpreting user commands and `pyttsx3` for generating audio responses.

---

## Installation

### Prerequisites

- Python 3.11+
- A Google Developer account and a project with the Google Calendar API enabled.
- A virtual environment (recommended).

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/dabetterman/buddytalk.git
