import sys

from PyQt5.QtWidgets import QMessageBox
from krita import *
from . import dsdk
import time
import PyQt5.QtCore
import io
from .data import get_activity, application_id

class Diskrita(Extension):
    app: dsdk.discord
    am: dsdk.discord.ActivityManager
    timer: PyQt5.QtCore.QTimer

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.app = None
        self.am = None
        self.timer = PyQt5.QtCore.QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_rpc)
        self.log("Diskrita extension has been initialised")

    def log(self, msg: str) -> None:
        p = "[Diskrita]: {}\n".format(msg)
        # *(tecc) Might wanna do something here later?
        print(p)
        pass

    def setup(self) -> None:
        self.app = dsdk.Discord(application_id, dsdk.CreateFlags.default)
        self.am = self.app.get_activity_manager()
        self.log("Setting self up")
        self.timer.start()

    def update_result(self, result: dsdk.Result) -> None:
        if result == dsdk.Result.ok:
            # self.log("Update OK")
            pass
        else:
            self.log("Update NOT OK: {}".format(result.name))

    def update_rpc(self) -> None:
        if self.app is None or self.am is None:
            self.log("App or AM is none")
            pass
        self.am.update_activity(get_activity(), self.update_result)
        self.app.run_callbacks()

    def createActions(self, window):
        # testAction = window.createAction()
        pass

    def windowClosed(self):
        self.timer.stop()
        self.am.clear_activity(self.update_result)
        self.log("Shutting down")


Krita.instance().addExtension(Diskrita(Krita.instance()))
