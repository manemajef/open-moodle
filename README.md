# Moodle Desktop

**Problem**: As a student, you need to open [Moodle](https://moodle.tau.ac.il/) multiple times a day, sometimes dozens of times. Since it requires three separate credentials (ID, username, password), password managers can't auto-fill everything and you end up manually typing your ID every single time. It's liveable, but annoying.

**Solution**: A desktop app that automatically logs you in and opens Moodle in a clean browser interface with tab support.

## Features

- Auto-login with saved credentials
- Multi-tab browsing (right-click links for "Open in new tab")
- Persistent sessions (stays logged in between launches)
- Clean desktop app interface

## Installing

Clone the repo and install dependencies:

```bash
git clone <repo-url>
cd open-moodle

# If you have uv installed:
uv sync

# Otherwise:
python -m venv .venv
source .venv/bin/activate
pip install .
```

## Running

**GUI version (default):**
```bash
python -m app.main_gui
```

**CLI version (opens in Chromium):**
```bash
python -m app.main
```

## Configuration

Credentials are stored in `~/Library/Application Support/Moodle Desktop/settings.json`

You can manually edit this file or the settings dialog will be added soon.

## Building for macOS

To create a `.dmg` installer:

```bash
# Build the app
uv run pyinstaller Moodle.spec --clean --noconfirm

# Create DMG
./build_dmg.sh
```

## TODOs

- [ ] Settings dialog UI for managing credentials
- [ ] UI polish and better styling
- [ ] Proper DMG distribution with installer
- [ ] Per-user credential management
- [ ] Cross-platform support (Windows, Linux)
- [ ] Custom URL configuration for other universities

## Tech Stack

- Python 3.13
- PyQt6 + QtWebEngine for the browser
- Pydantic for config management
