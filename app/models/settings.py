from pydantic import BaseModel

class Credentials(BaseModel):
    id: str
    username: str
    password: str 

class Selectors(BaseModel):
    password: str = "Ecom_Password" 
    username: str = "Ecom_User_ID" 
    id: str = "Ecom_User_Pid" 
class Urls(BaseModel):
    url: str = "https://moodle.tau.ac.il/"
    login_url: str ="https://moodle.tau.ac.il/auth/saml2/login.php"
    logged_url: str = "https://moodle.tau.ac.il/local/mycourses/"
class Settings(BaseModel):
    urls: Urls = Urls()  
    credentials: Credentials | None = None 
    selectors: Selectors = Selectors()  

   