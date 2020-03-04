from plugins.data_source import DataSource


class HttpDataSource(DataSource):
    def __init__(self, id):
        super().__init__(id)
        print("Http data source created")

    def migrate():
        pass

    def collect():
        pass

    def clean():
        pass

    def persist():
        pass
