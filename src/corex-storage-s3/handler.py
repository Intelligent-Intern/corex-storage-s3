# Handler for s3 implementing storage interface
from corex.core.interfaces.storage import StorageInterface

class S3Handler(StorageInterface):
    def __init__(self):
        pass

    def example_method(self):
        print("Handling storage with s3")
