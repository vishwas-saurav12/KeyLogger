# Import necessary libraries
from pynput import keyboard   # For listening to keyboard events
import pandas as pd           # For storing and saving data in tabular form
import time                   # For timestamping each event
from datetime import datetime, timezone, timedelta  # For timezone conversion

# List to store all keyboard event records
events = []

# Dictionary to store press timestamps (used to calculate how long a key was held)
press_times = {}

# Function triggered whenever a key is pressed
def on_press(key):
    try:
        # Try to get the key character; if it's a special key (like Enter or Shift), convert to string
        k = key.char if hasattr(key, "char") else str(key)
        ts = time.time()  # Record timestamp (in seconds since epoch)
        
        # Log the press event
        events.append({"key": k, "state": "pressed", "timestamp": ts})
        
        # Store the press time to calculate hold duration later
        press_times[k] = ts

    except Exception as e:
        print("Error on press:", e)

# Function triggered whenever a key is released
def on_release(key):
    try:
        # Get key name (works for both normal and special keys)
        k = key.char if hasattr(key, "char") else str(key)
        ts = time.time()  # Record release timestamp
        
        # Log the release event
        events.append({"key": k, "state": "released", "timestamp": ts})
        
        # If the key was previously pressed, calculate how long it was held
        if k in press_times:
            hold_time = ts - press_times[k]
            
            # Log the hold duration as a separate record
            events.append({"key": k, "state": "held", "duration_s": hold_time})
            
            # Remove key entry to avoid duplicates or memory leak
            del press_times[k]
    
    except Exception as e:
        print("Error on release:", e)
    
    # Stop listener when ESC key is pressed
    if key == keyboard.Key.esc:
        return False

# Notify user that logging has started
print("Press keys — recording starts now (press ESC to stop)...")

# Start the listener to capture keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Convert the list of events into a pandas DataFrame
df = pd.DataFrame(events)

# Convert timestamps (in seconds) to datetime objects
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s', utc=True)

# Convert UTC timestamps to Indian Standard Time (UTC+5:30)
IST = timezone(timedelta(hours=5, minutes=30))
df['timestamp'] = df['timestamp'].dt.tz_convert(IST)

# Save the log to a CSV file
df.to_csv("key_events.csv", index=False)

# Print confirmation and display the dataframe
print("\nSaved to key_events.csv (timestamps converted to IST)")
print(df)
