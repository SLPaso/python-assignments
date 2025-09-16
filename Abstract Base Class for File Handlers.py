python
from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def write(self):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        print("Reading from a text file.")
    
    def write(self):
        print("Writing to a text file.")

class BinaryFileHandler(FileHandler):
    def read(self):
        print("Reading from a binary file.")
    
    def write(self):
        print("Writing to a binary file.")

# Example usage
text_handler = TextFileHandler()
text_handler.read()
text_handler.write()

binary_handler = BinaryFileHandler()
binary_handler.read()
binary_handler.write()
