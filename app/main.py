from playwright.sync_api import sync_playwright 
from app.config import Config 
import time 
from dotenv import dotenv_values 
is_dev = True 
def main():
    config = Config() 
    # if (config):
    #     for field in ["username", "password", "id"]:
    #         value = getattr(config, field, None) 
    #         selector = config.selectors.get(field, None)  
    #         print(f"Field: {field}, Selector: {selector}, Value: {value}")
    #     return 
    if not config.has_credentials():
        if is_dev:
            env_vars = dotenv_values(".env") 
            config.save_credentials(env_vars['USERNAME'], env_vars['PASSWORD'], env_vars['ID'])

                
                
        print("no credentials found") 
        return 
    creds = config.settings.credentials 
    selectors = config.settings.selectors 
    urls = config.settings.urls  
    print(f"Loaded config from: {config.settings_path}") 
    print(f"Login URL: {urls.login_url}")
    p = sync_playwright().start()
    # browser = p.chromium.launch(headless=False) 
    context = p.chromium.launch_persistent_context(
        user_data_dir = "./browser_data", 
        headless=False, 
        # channel = "chrome" 
    )
    # context = browser 
    page = context.pages[0]  if context.pages else context.new_page() 

    # page.goto(urls.url)  
    # if urls.logged_url in page.url: 
    #     print("Already logged in -- exiting") 
    #     return 
    page.goto(urls.login_url)
    print(f"Navigated to login page: {page.url}")
    for field in ["username", "password", "id"]:
        value = getattr(creds, field, None) 
        selector = getattr(selectors,field, None)  
        print(f"Field: {field}, Selector: {selector}, Value: {'***' if value else None}")

        if value and selector: 
            page.fill(f'#{selector}', value) 
    page.click ('#loginButton') 
    page.wait_for_load_state("networkidle") 
    
    if urls.logged_url in page.url:
        print("Succesfull") 
    else: 
        print("failed") 
        return 
    try:
        while True:
            try:
                page.title()
                time.sleep(1)
            except:
                print("\nBrowser Closed")
                break 
    except KeyboardInterrupt:
        print("\nExisitng...")
   



if __name__ == "__main__":
    main() 
    