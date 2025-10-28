# Auto login to TAU's Moodle

#### Setup Credentials

for security reasons (obvisuly) your login details must remain hidden and never published. therefore, inorder for the script to work follow these instriuctions:

1. go to root dir and create a `.env` file: `cd path/to/dir && touch .env`
2. Enter your credentials:

```.env
USERNAME={yourUsername}
PASSWORD={yourPasswod}
ID={yourIDNumber}
```

## Use the script:

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

### Recommended - add alias

for example with `zsh` , assuming the path is `~/scripts/moodle`:

```bash
echo "alias moodle ='~/scripts/moodle/.venv/bin/python3 ~/scripts/moodle/main.py'" >> ~/.zshrc

```

now you can simply write `moodle` in terminal and your moodle would open up logged in.

## Q&A

**can it work with other universities?**

> probably yes, as long as thyre using moodle and the same login system for both.
> to config for youre own uni, checkout the html id for the username, password, id and confirm button and update config.

## Roadmap:

- [ ] get credentials and save them to system using a TUI

- [ ] make it cross platform and cross university
