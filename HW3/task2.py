from nltk import word_tokenize


class FileReader:
    def __init__(self, path):
        self.path = path
        self.line_count = None
        self.word_count = None

    def __add__(self, other):
        newFile = f'Unified_{self.path}&{other.path}.txt'
        with open(newFile, 'rw') as f:
            for line in open(self.path):
                f.write(line)
            for line in other:
                f.write(line)
        return FileReader(newFile)

    def __str__(self):
        return f'{self.path}'

    def read(self):
        try:
            with open(self.path) as read_file:
                return read_file.read()
        except FileNotFoundError:
            return ''

    def write(self, inp):
        with open(self.path, 'w') as write_file:
            write_file.write(inp)

    def count(self):
        self.line_count = 0
        self.word_count = 0
        for line in open(self.path):
            self.lines_count += 1
            self.word_count += len(word_tokenize(line))
        return self.line_count, self.word_count
