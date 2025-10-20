import json 
from dotenv import load_dotenv , dotenv_values 
load_dotenv 
from dataclasses import dataclass
from pathlib import Path
from app.default_config import DEFAULT_CONFIG 
from app.models.settings import Settings, Credentials
from pathlib import Path
import json

class Config:
    def __init__(self):
        self.settings_path = Path.home() / "Library/Application Support/Moodle Desktop/settings.json"
        self.settings = self.load_settings()
    
    def load_settings(self):
        """Load settings from file or return defaults"""
        try:
            with open(self.settings_path, "r") as f:
                data = json.load(f)
                return Settings(**data)
        except:
            default_settings = Settings()
            self.settings_path.parent.mkdir(parents=True, exist_ok=True) 
            with open(self.settings_path, "w") as f:
                json.dump(default_settings.model_dump(), f) 
            return default_settings 

    def has_credentials(self):
        return self.settings.credentials is not None
    
    def save_credentials(self, username: str, password: str, id_number: str):
        """Save user credentials"""
        self.settings.credentials = Credentials(
            username=username,
            password=password,
            id=id_number
        )
        self.save_settings()
    
    def save_settings(self):
        """Save settings to file"""
        self.settings_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.settings_path, "w") as f:
            json.dump(self.settings.model_dump(), f, indent=2) 
    
        
# class Config:
#     def __init__(self):
#        self.settings_json = Path.home() / "Library/Application Support/Moodle Desktop/settings.json"  
#        load_dotenv() 
#        self.load_settings()
#        self.load_credentials()       
#     def load_settings(self):
#         if not self.settings_json.exists():
#             raise FileExistsError
#         with open(self.settings_json, "r", encoding="utf-8") as f:
#             data = json.load(f) 
#             for k, v in data.items():
#                 setattr(self, k ,v) 
    
#     def load_credentials(self):
#         config = dotenv_values(".env") 
#         if not config:
#             raise SystemError 
#         for k, v in config.items(): 
#             setattr(self, k.lower(), v) 

            
    