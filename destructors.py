class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r') # Open file in read mode
    def read_data(self):
        return self.file.read()
    def __del__(self):
        self.file.close() # Closes the file once the object has been released.

# Instantiating the class
file_obj = FileHandler("sample.txt")
print(file_obj.read_data())
