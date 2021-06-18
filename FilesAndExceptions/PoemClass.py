# class Poem:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def readfile(self):
#             opened_file = open(self.filename, 'r')
#             print(opened_file.read())
#
# poem = Poem("poem.txt")
# poem.readfile()

class Shakespeare():
    def __init__(self, file_path):
        self.file = open(file_path)
        print(self.file)

    def print_lines(self):
        for line in self.file:
            print(line.rstrip('\n'))

    def close_file(self):
        self.file.close()

x = Shakespeare("poem.txt")
x.print_lines()