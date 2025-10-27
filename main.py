from main.login import login
import time

def main():
    driver = login()
    driver.get("https://moodle.tau.ac.il/local/mycourses/")
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
