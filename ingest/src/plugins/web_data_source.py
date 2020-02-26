from plugins.data_source import DataSource


class WebDataSource(DataSource):
    def __init__(self):
        super().__init__()
        print("Web data source created")
