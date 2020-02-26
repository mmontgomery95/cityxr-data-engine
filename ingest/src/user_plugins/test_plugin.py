from plugins.file_data_source import FileDataSource


class Plugin(FileDataSource):
    def __init__(self):
        super().__init__()
        pass

    def print(self):
        print("test 2")
