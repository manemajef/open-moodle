from main.login import login
import time
import sys
from main.config import config


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "tau":
        config["login_url"] = (
            "https://nidp.tau.ac.il/nidp/idff/sso?id=10&sid=0&option=credential&sid=0&target=https%3A%2F%2Fmytau.tau.ac.il%2F"
        )
        config["url"] = "https://my.tau.ac.il/TAU_Student/"
    driver = login(config)
    driver.get(config["url"])
    # Keep browser open
    print("Browser is open. Press Ctrl+C or close the browser window to exit...")
    try:
        while True:
            # Check if browser is still open
            try:
                driver.current_url
                time.sleep(1)
            except:
                print("\nBrowser was closed.")
                break
    except KeyboardInterrupt:
        print("\nClosing browser...")
        driver.quit()


if __name__ == "__main__":
    main()
