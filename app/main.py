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
        print("Successfully logged in")
    else:
        print("Login failed")
        context.close()
        p.stop()
        return

    print("Browser is now open. Navigate freely. Press Ctrl+C to exit.")
    try:
        while True:
            try:
                # Check if context is still alive
                context.pages
                time.sleep(1)
            except Exception as e:
                # Only exit if the browser/context is actually closed
                if "Browser" in str(e) or "Target" in str(e) or "closed" in str(e).lower():
                    print("\nBrowser Closed")
                    break
                # Otherwise, just continue (temporary navigation issues)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        try:
            context.close()
            p.stop()
        except:
            pass




if __name__ == "__main__":
    main()
