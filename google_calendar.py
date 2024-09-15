import os
import json
from datetime import timedelta, datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dateutil.parser import parse
from dotenv import load_dotenv
import speech
import time

load_dotenv()


# SCOPES defines what permissions we are requesting from the user
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_credentials():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            credentials = os.getenv("CREDENTIALS")
            if not credentials:
                raise ValueError("No 'CREDENTIALS' environment found")
            cred_dict = json.loads(credentials)
            flow = InstalledAppFlow.from_client_config(cred_dict, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def list_upcoming_events():
    """
    Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    speech.speak("Getting the upcoming events")
    time.sleep(2)

    # Call the Calendar API
    now = datetime.now().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=3, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return 'No upcoming events found.'
    
    event_list = []
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        try:
            new_date = parse(start)
            formatted_date = new_date.strftime("%d-%B")
            event_list.append(f"{formatted_date} {event['summary']}")
        except ValueError as e:
            print(f"Error parsing date: {e}")
    # speech.speak(event_list)
    return event_list

def list_public_holidays():
    """
    List some of the upcoming public holidays
    """
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)

    # Specify the calendar ID for public holidays in South Africa
    calendar_id = 'en.sa#holiday@group.v.calendar.google.com'

    # Define the time range
    now = datetime.now().isoformat() + 'Z'  # 'Z' indicates UTC time
    time_max = (datetime.now() + timedelta(days=100)).isoformat() + 'Z'  # Next 100 days

    # Fetch events
    speech.speak("Getting the upcoming public holidays")
    time.sleep(2)
    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=now,
        timeMax=time_max,
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    if not events:
        speech.speak('No upcoming public holidays found.')
        return('No upcoming public holidays found.')

    event_list = []
    # Print the public holidays
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        try:
            new_date = datetime.strptime(start, "%Y-%m-%d")
            formatted_date = new_date.strftime("%d-%B")
            event_list.append(f"{formatted_date} {event['summary']}")
        except ValueError as e:
            print(f"Error: {e}")
    return event_list
        # print(f"{formatted_date} {event['summary']}")
        # speech.speak(f"{formatted_date} {event['summary']}")

def list_events_by_name():
    """
    Lists the events by name from the calendar
    """
    creds = get_credentials()
    speech.speak("Tell me the title of the event")
    event_title = speech.hearing().lower()

    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.now().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming events")
    speech.speak("Getting the upcoming events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        ).execute()
    )
    events = events_result.get("items", [])

    if not events:
        speech.speak("No upcoming events found.")
        return ("No upcoming events found.")

    # event_list = []
    # Find the event with the given title
    for event in events:
        if event["summary"].lower() == event_title.lower():
            
            # start = event['start'].get('dateTime')
            # try:
            #     new_date = parse(start)
            #     formatted_date = new_date.strftime("%d-%B")
            #     event_list.append(f"{formatted_date} {event['summary']}")
            # except ValueError as e:
            #     print(f"Error parsing date: {e}")
            # return (event_list)
            return event["summary"]
    return ("No upcoming event found.")




def delete_event(event_title):
    """
    Delete an event with the given title from the user's calendar.
    """
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)

    # Fetch upcoming events
    now = datetime.now().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming events")
    speech.speak("Getting the upcoming events")
    events_result = service.events().list(
        calendarId="primary",
        timeMin=now,
        maxResults=10,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])

    if not events:
        speech.speak("No upcoming events found.")
        return "No upcoming events found."

    # Search for the event by title
    event_to_delete = None
    for event in events:
        if event["summary"].lower() == event_title.lower():
            event_to_delete = event
            break

    if event_to_delete is None:
        speech.speak(f"No event found with the title '{event_title}'.")
        print(f"No event found with the title '{event_title}'.")
        return f"No event found with the title '{event_title}'."

    # Found the event, ask for confirmation
    speech.speak(f"Found event {event_to_delete['summary']} on {event_to_delete['start'].get('dateTime') or event_to_delete['start'].get('date')}.")
    speech.speak("Would you like to delete this event?")

    answer = speech.hearing().lower()
    print(answer)

    if answer == 'yes':
        try:
            service.events().delete(calendarId="primary", eventId=event_to_delete['id']).execute()
            print(f"Event '{event_to_delete['summary']}' deleted successfully.")
            speech.speak("Deleted successfully.")
            return event_title
        except Exception as e:
            print(f"Failed to delete event: {e}")
            speech.speak("Failed to delete the event.")
            return f"Failed to delete event: {e}"
    else:
        print(f"Delete canceled for event '{event_to_delete['summary']}'.")
        speech.speak("Delete canceled")
        return "Delete canceled."
