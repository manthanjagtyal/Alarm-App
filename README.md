# Alarm-App
This is a basic Alarm App made By me as a Second Project.
# Alarm App (Python + Tkinter)

A simple and beginner-friendly **Alarm Application** built using **Python** and **Tkinter**. This app allows users to set an alarm in `HH:MM:SS` format, shows live current time, and plays a beep sound when the alarm time is reached.

## Features

* Clean and user-friendly GUI
* Set alarm using `HH:MM:SS` format
* Real-time current time display
* Automatic alarm triggering with beep sound
* Popup notification when alarm rings
* Background thread for smooth UI (no freezing)

## How It Works

* The user enters a time in the format `HH:MM:SS`.
* The current time updates every second using Tkinter's `after()` method.
* A background thread continuously checks the system time.
* When the given alarm time matches, a **beep sound** is played and an **alert box** appears.

## How to Run

1. Install Python 3.x
2. Save the app file as `alarm_app.py`
3. Run the script:

   ```bash
   python alarm_app.py
   ```
4. The GUI window will open.

## Requirements

* Python 3.x
* Tkinter (comes pre-installed)
* `winsound` module (Windows only for beep sound)

## File Structure

* `alarm_app.py` — Main application file
* `README.md` — Project documentation

## Possible Enhancements

* Add snooze button
* Add custom ringtone (MP3/WAV)
* Multiple alarms feature
* Modern UI design / Dark mode

## License

Free to use and modify for learning or personal projects.
