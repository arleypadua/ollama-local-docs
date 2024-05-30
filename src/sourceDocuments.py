import os

from settings import Settings

class SourceDocuments:
    def __init__(self, settings: Settings):
        self.settings = settings
        
    def save_file(self, file):
        filePath = os.path.join(self.settings.source_directory, file.filename)
        file.save(filePath)