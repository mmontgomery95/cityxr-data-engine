from plugins.data_source import DataSource


class HttpDataSource(DataSource):
    def __init__(self):
        super().__init__()
        print("Http data source created")
