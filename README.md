## Open And login to Moodle

**PROBLEM**: As a student, You need to open [Moodle](https://moodle.tau.ac.il/) multiple times a day, somtimes even dozens! and since it requires three credentials (ID, username, password) Youre password mannager cant insert it autmaticly - and you have to manualy type youre id. this is liveable, but annyoing.

**Solution**
Create a script which does that autmaticly for you.

**inputs it needs**:

- youre specific UNI moodle url `https://moodle.yourUni.com`.
- youre credentials:

  - password
  - username
  - id

  ### Working

  - do the logic in a chromium window, on close kills the script. **NEEDS CHROME**.

  ##### TODOS

  - [] wrap in a desktop app
  - [] prompt user to add credentials
  - [] have ui settings
  - [] work in default browser without chromium

  ## Installing

  - Clone the repo
  - make sure u have python installed
  - if uv is installed run `uv sync`
  - if no iv installed:

  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install .
  ```

  - run `python3 main.py`
