from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


    def create_dir(self, path):
        directory = self.dest + self.source / Path.relative_to()
        Path.mkdir(directory, parents=True, exist_ok=True)


    def build(self):
        Path.mkdir(self.dest, parents=True, exist_ok=True)

        for path in self.source.rglob("*"):
            if path is Path.is_dir():
                self.create_dir(path)




