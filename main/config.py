import os
from dotenv import load_dotenv
load_dotenv()

config = {
    "login_url": "https://moodle.tau.ac.il/auth/saml2/login.php",
    "selectors": {
        "username": "Ecom_User_ID",
        "password": "Ecom_Password",
        "id": "Ecom_User_Pid"
    },
    "username": os.getenv("USERNAME"),
    "id": os.getenv("ID"),
    "password": os.getenv("PASSWORD")
}
