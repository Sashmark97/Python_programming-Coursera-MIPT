import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
class FileReader:
    def __init__(self, path):
        self.path = path
    
    def read(self):
        str = ""
        try:
            str = open(os.path.join(__location__, self.path)).read()
            #str = open(self.path, "r").read()
            return str
        except IOError:
            #print("Why are we still here?")
            return ""

#if __name__ == '__main__':
#    reader = FileReader("shit.txt")
#    print(reader.read())