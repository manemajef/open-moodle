# automate the boring login proccess for TAU's website and the Moodle

- save credentials under `.env` as:
  - USERNAME = "your username"
  - ID = your-id-number
  - PASSWORD = "your password"

**Activate `.venv`**:

```bash
cd path/to/dir
source .venv/bin/activate
```

**open moodle**:

```bash
python3 main.py
```

**open TAU**:

```bash
python3 main.py tau
```

## Q&A

**can it work with other universities?**

> probably yes, as long as thyre using moodle and the same login system for both.
> to config for youre own uni, checkout the html id for the username, password, id and confirm button and update config.

## Roadmap:

- [ ] get credentials and save them to system using a TUI
- [ ] make it cross platform and cross university
