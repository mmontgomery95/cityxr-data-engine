from plugins.data_source import DataSource


class FileDataSource(DataSource):
    def __init__(self, runtime_id, name):
        super().__init__(runtime_id, name)
        print("File data source created")

    def migrate():
        pass

    def collect():
        pass

    def clean():
        pass

    def persist():
        pass
