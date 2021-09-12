import PyQt5.QtCore
from krita import *
from . import dsdk


class DocData:
    id: int
    opened: int

    def __init__(self, id):
        self.time = id


application_id = 886631121192882226
docs: dict = dict()
nextId = 0
previousDocId = None


def inst():
    return Krita.instance()


def get_active_doc():
    return inst().activeDocument()


def get_activity() -> dsdk.activity:
    act = dsdk.Activity()
    ad = get_active_doc()
    act.application_id = application_id
    act.assets.large_image = "krita_logo"
    act.assets.large_text = "Version {}".format(inst().version())
    act.party.id = "krita"
    if ad is not None:
        act.details = "Editing {}".format(ad.name() or "something")
        sizeX = ad.width()
        sizeY = ad.height()
        animLength: int = ad.animationLength()
        type: str = "image"
        #if animLength > 1:
        #    type = "{}FPS animation".format(ad.framesPerSecond())
        # TODO: Make it able to detect if a document is an animation or a static image
        act.state = "{}x{} {}".format(sizeX, sizeY, type)
    else:
        act.details = "Idle"

    return act
