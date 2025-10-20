from PyQt6.QtWidgets import QMainWindow, QToolBar, QPushButton, QTabWidget
from PyQt6.QtWebEngineCore import QWebEngineProfile
from PyQt6.QtCore import QUrl, QTimer
from app.config import Config
from app.gui.browser_tab import BrowserTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.setGeometry(100,100,1200,800)

        self.setWindowTitle("Moodle Desktop")
        self.create_toolbar()
        self.create_browser()
        if self.config.has_credentials():
            self.auto_login()
        else:
            self.open_settings()
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        new_tab_btn = QPushButton("+ New Tab")
        new_tab_btn.clicked.connect(lambda: self.add_new_tab())
        toolbar.addWidget(new_tab_btn)

        settings_btn = QPushButton("Settings")
        settings_btn.clicked.connect(self.open_settings)
        toolbar.addWidget(settings_btn)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.auto_login)
        toolbar.addWidget(login_btn)
    def create_browser(self):
        profile = QWebEngineProfile.defaultProfile()
        if not profile:
            return
        profile.setPersistentStoragePath("./browser_data")

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tab_widget)

        self.add_new_tab(QUrl(self.config.settings.urls.url))
    def open_settings(self):
        pass
    def add_new_tab(self, url=None):
        browser = BrowserTab()
        browser.new_tab_requested.connect(self.add_new_tab)

        if url:
            browser.setUrl(url)
        else:
            browser.setUrl(QUrl(self.config.settings.urls.url))

        browser.titleChanged.connect(lambda title: self.update_tab_title(browser, title))

        index = self.tab_widget.addTab(browser, "New Tab")
        self.tab_widget.setCurrentIndex(index)

        return browser

    def update_tab_title(self, browser, title):
        index = self.tab_widget.indexOf(browser)
        if index != -1:
            self.tab_widget.setTabText(index, title[:30])

    def close_tab(self, index):
        if self.tab_widget.count() > 1:
            self.tab_widget.removeTab(index)

    def current_browser(self):
        return self.tab_widget.currentWidget()

    def auto_login(self):
        if not self.config.has_credentials():
            self.open_settings()
            return

        creds = self.config.settings.credentials
        selectors = self.config.settings.selectors
        urls = self.config.settings.urls

        browser = self.current_browser()
        browser.setUrl(QUrl(urls.login_url))

        try:
            browser.loadFinished.disconnect()
        except:
            pass

        def on_load_finished(ok):
            if ok:
                QTimer.singleShot(500, lambda: self.fill_login_form(browser, creds, selectors))

        browser.loadFinished.connect(on_load_finished)

    def fill_login_form(self, browser, creds, selectors):
        js_code = f"""
        (function() {{
            try {{
                var username = document.getElementById('{selectors.username}');
                var password = document.getElementById('{selectors.password}');
                var id = document.getElementById('{selectors.id}');
                var button = document.getElementById('loginButton');

                if (username && password && id && button) {{
                    username.value = '{creds.username}';
                    password.value = '{creds.password}';
                    id.value = '{creds.id}';
                    button.click();
                    return 'success';
                }} else {{
                    return 'missing elements: ' +
                        (!username ? 'username ' : '') +
                        (!password ? 'password ' : '') +
                        (!id ? 'id ' : '') +
                        (!button ? 'button' : '');
                }}
            }} catch(e) {{
                return 'error: ' + e.message;
            }}
        }})();
        """

        def on_script_finished(result):
            if result and result != 'success':
                print(f"Login form fill result: {result}")

        browser.page().runJavaScript(js_code, on_script_finished)
if __name__ == "__main__":
    gui = MainWindow()
