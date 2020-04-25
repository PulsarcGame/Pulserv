import zipfile


class beatMap:
    def __init__(self, raw):
        self.raw = raw


class beatAudio:
    def __init__(self, raw):
        self.raw = raw


class backgoundImage:
    def __init__(self, raw):
        self.raw = raw


class MapPackage:
    def __init__(self, raw):
        self.raw = raw
        unzipped_raws = None
        # self.beatmap = beatMap()
        # self.audio = beatAudio()
        # self.backgroundImage = backgoundImage()
