# Import necessary libraries
from pynput import keyboard
import pandas as pd
import time
from datetime import datetime, timezone, timedelta

# List to store all keyboard event records
events = []

# Dictionary to store press timestamps
press_times = {}

# Function triggered whenever a key is pressed
def on_press(key):
    try:
        k = key.char if hasattr(key, "char") else str(key)
        ts = time.time()
        events.append({"key": k, "state": "pressed", "timestamp": ts})
        press_times[k] = ts
    except Exception as e:
        print("Error on press:", e)

# Function triggered whenever a key is released
def on_release(key):
    try:
        k = key.char if hasattr(key, "char") else str(key)
        ts = time.time()
        events.append({"key": k, "state": "released", "timestamp": ts})
        
        if k in press_times:
            hold_time = ts - press_times[k]
            events.append({"key": k, "state": "held", "duration_s": hold_time})
            del press_times[k]
    except Exception as e:
        print("Error on release:", e)
    
    if key == keyboard.Key.esc:
        return False

print("Press keys – recording starts now (press ESC to stop)...")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

df = pd.DataFrame(events)
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s', utc=True)
IST = timezone(timedelta(hours=5, minutes=30))
df['timestamp'] = df['timestamp'].dt.tz_convert(IST)
df.to_csv("key_events.csv", index=False)

print("\nSaved to key_events.csv (timestamps converted to IST)")
print(df)