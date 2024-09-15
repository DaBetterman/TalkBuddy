from flask import Flask, render_template, request, jsonify, redirect, url_for
import google_calendar
import speech

app = Flask(__name__)


@app.route('/')
def index():
    google_calendar.get_credentials()
    return render_template('index.html')

@app.route('/api/speak', methods=['POST'])
def speaks():
    data = request.json
    text = data.get('text')
    if text:
        speech.speak(text)
        return jsonify({"message": "Speaking: " + text}), 200
    return jsonify({"error": "No text provided"}), 400

@app.route('/calendar/events')
def calendar_events():
    try:
        events = google_calendar.list_upcoming_events()
        speech.speak(events)
        return jsonify({"events": events}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/calendar/public_holidays')
def public_holidays():
    try:
        events = google_calendar.list_public_holidays()
        speech.speak(events)
        return jsonify({"events": events}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/calendar/delete_event')
def delete_event():
    try:
        events = google_calendar.list_events_by_name()
        print(f"this is the event found: {events}")
        # if not events:
        #     speech.speak("No event found to delete.")
        #     return jsonify({"message": "No matching events found."}), 404

        # Assuming 'events' is a list, prompt the user to choose which event to delete
        # event_to_delete = events[0]
        # speech.speak(f"Would you like to delete the event {event_to_delete}?")
        # print(f"Would you like to delete the event {event_to_delete}?")

        # query = speech.hearing().lower()
        # if query == 'yes':
        list = []
        google_calendar.delete_event(events)
        new_list = list.append(events)
        return jsonify({"events": new_list}), 200
        # else:
        #     speech.speak("Event has not been deleted")
        #     print(f"Event has not been deleted {event_to_delete}")

            # return jsonify({"message": "Event deletion canceled."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

