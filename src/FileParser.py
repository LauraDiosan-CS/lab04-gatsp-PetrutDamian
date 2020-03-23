import os
class FileParser:

    @staticmethod
    def parseMatrix(filename):
        currentDir = os.getcwd()
        filePath = os.path.join(currentDir, 'Data', filename)
        f = open(filePath)
        n = int(f.readline())
        matrix = []
        for line in f:
            args = line.split(',')
            l = []
            for arg in args:
                l.append(float(arg))
            matrix.append(l)
        return matrix,n

