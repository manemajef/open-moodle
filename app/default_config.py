"""
Default configuration for TAU Moodle
These settings are bundled with the app and work for Tel Aviv University's Moodle
Users can override these in their personal settings if needed
"""

DEFAULT_CONFIG = {
    "url": "https://moodle.tau.ac.il",
    "login_url": "https://moodle.tau.ac.il/auth/saml2/login.php",
    "logged_url": "https://moodle.tau.ac.il/local/mycourses/",
    "course_url": "https://moodle.tau.ac.il/local/mycourses/",
    "selectors": {
        "username": "Ecom_User_ID",
        "password": "Ecom_Password",
        "id": "Ecom_User_Pid"
    }
}
