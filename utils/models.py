from os import listdir
from os.path import isfile, join

class Models:
    def __init__(self, path):
        self.path = path

    def get_names(self):
        onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]

        onlyfiles.sort()

        files_sorted = []
        for file in onlyfiles:
            name = file.split('.')
            files_sorted.append(name[0])
        return files_sorted
