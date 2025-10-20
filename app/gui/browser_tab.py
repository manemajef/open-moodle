from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, pyqtSignal

class BrowserTab(QWebEngineView):
    new_tab_requested = pyqtSignal(QUrl)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.page().linkHovered.connect(self.on_link_hovered)
        self.hovered_link = None

    def on_link_hovered(self, url):
        self.hovered_link = url

    def contextMenuEvent(self, event):
        from PyQt6.QtWidgets import QMenu

        menu = QMenu(self)

        if self.hovered_link:
            open_in_new_tab_action = menu.addAction("Open in new tab")
            open_in_new_tab_action.triggered.connect(
                lambda: self.new_tab_requested.emit(QUrl(self.hovered_link))
            )

        back_action = menu.addAction("Back")
        back_action.triggered.connect(self.back)

        forward_action = menu.addAction("Forward")
        forward_action.triggered.connect(self.forward)

        reload_action = menu.addAction("Reload")
        reload_action.triggered.connect(self.reload)

        menu.exec(event.globalPos())

    def createWindow(self, window_type):
        new_browser = BrowserTab()
        self.new_tab_requested.emit(QUrl())
        return new_browser
