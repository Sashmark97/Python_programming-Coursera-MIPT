import os
import tempfile
import codecs
import io


class File:
    def __init__(self, path):
        self.path = path
        self.pos = 0
        if not os.path.isfile(path):
            f = io.open(path,"w+", encoding='utf8')
            f.close()

    def __str__(self):
        return self.path

    def __add__(self, other):
        res_path = os.path.join(tempfile.gettempdir(), 'sum.txt')
        print(res_path)
        f1 = io.open(self.path,"r", encoding='utf8')
        f2 = io.open(other.path,"r", encoding='utf8')
        res = f1.read() + f2.read()
        res_file = File(res_path)
        res_file.write(res)
        return res_file


    def write(self, str):
        f = io.open(self.path, 'a', encoding='utf8')
        f.seek(self.pos)
        f.write(str)
        self.pos = f.tell()
        f.close()

    def __iter__(self):
        return self

    def __next__(self):
        f = io.open(self.path, 'r', encoding='utf8')
        f.seek(self.pos)
        line = f.readline()
        if not line:
            self.pos = 0
            raise StopIteration('EOF')
        self.pos = f.tell()
        return line


'''
if __name__ == '__main__':
    f1 = File("/home/scarlet/Desktop/Python/Diving into Python(Coursera)/Week4/test1.txt")
    f2 = File("/home/scarlet/Desktop/Python/Diving into Python(Coursera)/Week4/test2.txt")
    f1.write('1111999\n')
    f2.write('22666')
    #f1 + f2
    #print(f)
'''