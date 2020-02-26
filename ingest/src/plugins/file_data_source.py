from plugins.data_source import DataSource


class FileDataSource(DataSource):
    def __init__(self):
        super().__init__()
        print("File data source created")
