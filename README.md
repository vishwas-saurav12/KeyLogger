# KeyLogger
Python, Spyware


# KeyLogger-Spyware-Kali

## 🐧 Kali Linux Version

> **Note**: This is the **Kali Linux** version of the keylogger project.
> 
> - **KeyLogger-Spyware.py** → For Windows OS
> - **KeyLogger-Spyware-Kali.py** → For Kali Linux OS (this version)
>
> This version is specifically optimized for Kali Linux and other Debian-based distributions.

A Python-based keyboard event logger designed for Kali Linux environments, capturing keystroke data with precise timing information and timezone conversion to IST (Indian Standard Time).

## ⚠️ Legal Disclaimer

**IMPORTANT: READ BEFORE USE**

This tool is provided for **EDUCATIONAL AND RESEARCH PURPOSES ONLY**. 

- ✅ **Authorized Use Only**: Use only on systems you own or have explicit written permission to monitor
- ❌ **Unauthorized Access is Illegal**: Deploying keyloggers without consent violates computer fraud and privacy laws in most jurisdictions
- ⚖️ **Your Responsibility**: You are solely responsible for ensuring compliance with all applicable laws and regulations
- 🎓 **Intended for**: Security researchers, penetration testers, and students in controlled lab environments

**Violation of these terms may result in criminal prosecution and civil liability.**

---

## 📋 Table of Contents

- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Output Format](#output-format)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- **Real-time Keystroke Monitoring**: Captures all keyboard events (press, release, hold)
- **Precise Timing**: Records timestamps with microsecond precision
- **Hold Duration Tracking**: Calculates how long each key was held down
- **Timezone Conversion**: Automatic conversion from UTC to IST (GMT+5:30)
- **CSV Export**: Structured data output for easy analysis
- **Special Key Support**: Captures both regular characters and special keys (Enter, Shift, Ctrl, etc.)
- **Graceful Exit**: Stop recording cleanly by pressing ESC key
- **Lightweight**: Minimal resource usage and dependencies

---

## 🖥️ System Requirements

### Operating System
- Kali Linux (2020.1 or later)
- Other Debian-based distributions (Ubuntu, Debian, etc.)

### Software Requirements
- Python 3.6 or higher
- X11 display server (for GUI environments)

### Hardware Requirements
- Minimum 512 MB RAM
- 100 MB free disk space
- Active keyboard input device

---

## 📦 Installation

### Step 1: Update System Packages

```bash
sudo apt update
sudo apt upgrade -y
```

### Step 2: Install Python and Dependencies

```bash
# Install Python 3 and pip (if not already installed)
sudo apt install python3 python3-pip -y

# Install X11 libraries (required for pynput)
sudo apt install python3-xlib -y
```

### Step 3: Install Python Libraries

```bash
# Install pynput for keyboard monitoring
pip3 install pynput

# Install pandas for data processing
pip3 install pandas
```

### Step 4: Verify Installation

```bash
# Check Python version
python3 --version

# Verify installed packages
pip3 list | grep -E "pynput|pandas"
```

**Expected Output:**
```
pynput     1.7.6
pandas     2.x.x
```

### Step 5: Download or Create the Script

```bash
# Create project directory
mkdir ~/keylogger-project
cd ~/keylogger-project

# Create the script file (Kali Linux version)
nano KeyLogger-Spyware-Kali.py
```

Paste the keylogger code and save (`Ctrl+X`, then `Y`, then `Enter`).

**Important**: Make sure you're using the **Kali Linux version** of the code, not the Windows version (KeyLogger-Spyware.py).

---

## 🚀 Usage

### Basic Usage

```bash
# Navigate to project directory
cd ~/keylogger-project

# Run the keylogger (Kali Linux version)
python3 KeyLogger-Spyware-Kali.py
```

**Output:**
```
Press keys – recording starts now (press ESC to stop)...
```

Type normally and press **ESC** to stop recording.

### Advanced Usage

#### Run with Elevated Privileges (System-Wide Monitoring)

```bash
sudo python3 KeyLogger-Spyware-Kali.py
```

This captures keystrokes from all applications, not just the terminal.

#### Run in Background

```bash
# Start in background
nohup python3 KeyLogger-Spyware-Kali.py > output.log 2>&1 &

# Check if running
ps aux | grep KeyLogger-Spyware-Kali

# Stop background process
pkill -f KeyLogger-Spyware-Kali.py
```

#### Run with Custom Output File

Modify the script to change the output filename:

```python
# Change this line in the script:
df.to_csv("custom_log_name.csv", index=False)
```

### Stopping the Keylogger

- **Method 1**: Press the `ESC` key (graceful shutdown)
- **Method 2**: Press `Ctrl+C` in the terminal (force stop)
- **Method 3**: Kill the process: `pkill -f KeyLogger-Spyware-Kali`

---

## 📊 Output Format

### CSV File Structure

The keylogger generates a `key_events.csv` file with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `key` | string | The key character or special key name |
| `state` | string | Event type: "pressed", "released", or "held" |
| `timestamp` | datetime | Event timestamp in IST timezone |
| `duration_s` | float | Key hold duration in seconds (only for "held" events) |

### Sample Output

```csv
key,state,timestamp,duration_s
h,pressed,2025-12-24 15:30:45.123456+05:30,
h,released,2025-12-24 15:30:45.234567+05:30,
h,held,2025-12-24 15:30:45.234567+05:30,0.111111
e,pressed,2025-12-24 15:30:45.345678+05:30,
e,released,2025-12-24 15:30:45.456789+05:30,
e,held,2025-12-24 15:30:45.456789+05:30,0.111111
Key.enter,pressed,2025-12-24 15:30:46.123456+05:30,
Key.enter,released,2025-12-24 15:30:46.234567+05:30,
Key.enter,held,2025-12-24 15:30:46.234567+05:30,0.111111
```

### Viewing the Output

```bash
# View raw CSV
cat key_events.csv

# View in formatted columns
column -s, -t < key_events.csv | less

# Open in LibreOffice Calc
libreoffice --calc key_events.csv

# View with pandas (Python)
python3 -c "import pandas as pd; print(pd.read_csv('key_events.csv'))"
```

---

## ⚙️ Configuration

### Changing Timezone

To use a different timezone, modify this section in the code:

```python
# Current: Indian Standard Time (IST)
IST = timezone(timedelta(hours=5, minutes=30))

# For EST (Eastern Standard Time)
EST = timezone(timedelta(hours=-5))

# For UTC (no conversion)
# Simply remove or comment out the timezone conversion line
```

### Filtering Specific Keys

Add filtering logic in the `on_press` or `on_release` functions:

```python
def on_press(key):
    try:
        k = key.char if hasattr(key, "char") else str(key)
        
        # Example: Only log alphabetic characters
        if k.isalpha():
            ts = time.time()
            events.append({"key": k, "state": "pressed", "timestamp": ts})
            press_times[k] = ts
    except Exception as e:
        print("Error on press:", e)
```

### Changing Output Format

Modify the save section to use different formats:

```python
# JSON output
import json
with open("key_events.json", "w") as f:
    json.dump(events, f, indent=2, default=str)

# Excel output
df.to_excel("key_events.xlsx", index=False)

# SQLite database
import sqlite3
conn = sqlite3.connect("key_events.db")
df.to_sql("events", conn, if_exists="replace", index=False)
```

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pynput'"

**Solution:**
```bash
pip3 install --user pynput
# Or with sudo
sudo pip3 install pynput
```

### Issue: "ModuleNotFoundError: No module named 'pandas'"

**Solution:**
```bash
sudo apt install python3-pandas
# Or
pip3 install pandas
```

### Issue: Keys Not Being Captured

**Causes & Solutions:**

1. **Missing X11 libraries:**
```bash
sudo apt install python3-xlib -y
```

2. **Insufficient permissions:**
```bash
sudo python3 KeyLogger-Spyware.py
```

3. **Running over SSH without display:**
```bash
export DISPLAY=:0
sudo python3 KeyLogger-Spyware.py
```

### Issue: "Permission Denied" Error

**Solution:**
```bash
# Give execute permissions
chmod +x KeyLogger-Spyware-Kali.py

# Run with sudo
sudo python3 KeyLogger-Spyware-Kali.py
```

### Issue: ESC Key Not Stopping the Program

**Solutions:**
- Press `Ctrl+C` to force stop
- Check if ESC key is being captured by another application
- Ensure you're pressing ESC in the correct terminal window

### Issue: High CPU Usage

**Causes:**
- Too many rapid keystrokes
- Large log file accumulation

**Solutions:**
```bash
# Limit recording time
timeout 60 python3 KeyLogger-Spyware-Kali.py

# Clear old log files
rm key_events.csv
```

### Issue: Timestamps Not in IST

**Solution:**
Verify timezone conversion code is present:
```python
IST = timezone(timedelta(hours=5, minutes=30))
df['timestamp'] = df['timestamp'].dt.tz_convert(IST)
```

---

## 🔒 Security Considerations

### Protecting Captured Data

#### 1. Encrypt Output Files

```bash
# Encrypt with GPG
gpg -c key_events.csv
# Enter passphrase when prompted

# Delete original
shred -u key_events.csv

# Decrypt when needed
gpg key_events.csv.gpg
```

#### 2. Secure File Permissions

```bash
# Restrict access to owner only
chmod 600 key_events.csv

# Restrict script access
chmod 700 KeyLogger-Spyware.py
```

#### 3. Automated Cleanup

Add to the end of your script:

```python
import os
import time

# Auto-delete logs older than 24 hours
log_age = time.time() - os.path.getmtime("key_events.csv")
if log_age > 86400:  # 24 hours in seconds
    os.remove("key_events.csv")
```

### Best Practices

1. **Immediate Deletion**: Delete logs after analysis
2. **No Cloud Storage**: Keep logs local and encrypted
3. **Minimal Retention**: Don't store logs longer than necessary
4. **Access Control**: Restrict script and log file permissions
5. **Audit Trail**: Document when and why the tool was used
6. **Informed Consent**: Always obtain written permission

### Detection & Prevention

This tool can be detected by:
- Antivirus software
- Process monitors (ps, top, htop)
- Network traffic analysis (if modified to send data)
- File integrity monitoring

To avoid false positives in your own testing environment:
```bash
# Add to antivirus whitelist (example for ClamAV)
sudo clamscan --exclude-dir=/path/to/keylogger-project
```

---

## 📈 Data Analysis Examples

### Using Python/Pandas

```python
import pandas as pd

# Load data
df = pd.read_csv("key_events.csv")

# Count key presses
key_counts = df[df['state'] == 'pressed']['key'].value_counts()
print("Most pressed keys:")
print(key_counts.head(10))

# Average hold time per key
avg_hold = df[df['state'] == 'held'].groupby('key')['duration_s'].mean()
print("\nAverage hold duration:")
print(avg_hold.sort_values(ascending=False).head(10))

# Typing speed (characters per minute)
time_range = (df['timestamp'].max() - df['timestamp'].min()).total_seconds() / 60
total_chars = len(df[df['state'] == 'pressed'])
cpm = total_chars / time_range if time_range > 0 else 0
print(f"\nTyping speed: {cpm:.2f} characters per minute")
```

### Using Command Line

```bash
# Count total keystrokes
wc -l key_events.csv

# Find most common keys
cut -d',' -f1 key_events.csv | sort | uniq -c | sort -rn | head -10

# Extract only pressed events
grep "pressed" key_events.csv > pressed_only.csv

# Get events in a specific time range
awk -F',' '$3 ~ /2025-12-24 15:30/ {print}' key_events.csv
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** with clear commit messages
4. **Test thoroughly** in a Kali VM environment
5. **Submit a pull request** with a detailed description

### Areas for Improvement

- [ ] GUI interface using Tkinter or PyQt
- [ ] Real-time keystroke analysis dashboard
- [ ] Machine learning for typing pattern recognition
- [ ] Multi-language support
- [ ] Cross-platform compatibility (Windows, macOS)
- [ ] Encrypted log transmission
- [ ] Configurable hotkeys for start/stop

---

## 📄 License

This project is provided as-is for educational purposes. Use at your own risk and responsibility.

**MIT License** (or specify your chosen license)

```
Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Support & Contact

### Getting Help

- Check the [Troubleshooting](#troubleshooting) section
- Review Kali Linux documentation: https://www.kali.org/docs/
- Python pynput documentation: https://pynput.readthedocs.io/

### Reporting Issues

When reporting issues, please include:
- Kali Linux version (`uname -a`)
- Python version (`python3 --version`)
- Complete error message
- Steps to reproduce the issue

---

## 🔄 Changelog

### Version 1.0.0 (Current)
- Initial release
- Basic keystroke logging functionality
- IST timezone conversion
- CSV output format
- ESC key termination

### Planned Features (Future Versions)
- v1.1.0: GUI interface
- v1.2.0: Real-time analysis
- v1.3.0: Encrypted storage
- v2.0.0: Multi-platform support

---

## 📚 Additional Resources

### Related Tools
- **KeyTweaker**: Keyboard remapping tool
- **xev**: X11 event viewer for debugging
- **evtest**: Input device event monitor

### Learning Resources
- [Python pynput Documentation](https://pynput.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Kali Linux Official Docs](https://www.kali.org/docs/)
- [OWASP Security Guidelines](https://owasp.org/)

### Ethical Hacking Courses
- Certified Ethical Hacker (CEH)
- Offensive Security Certified Professional (OSCP)
- SANS SEC560: Network Penetration Testing

---

## ⚖️ Final Warning

**Remember: With great power comes great responsibility.**

This tool demonstrates security vulnerabilities in systems. Use this knowledge to:
- ✅ Improve security practices
- ✅ Educate others about risks
- ✅ Conduct authorized security testing
- ❌ NEVER compromise others' privacy or security

**Stay ethical. Stay legal. Stay secure.**

---

*Last Updated: December 2025*
