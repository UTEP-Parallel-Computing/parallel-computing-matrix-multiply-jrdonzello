#!/usr/bin/env python3
import matrixUtils, time

class MatrixMain():
    def __init__(self):
        value = input("Input custom size and value? Or use standard size=1024, value=1? \nExample Input: 10 5\n")
        if value is not "":
            value = value.split(" ")
            self.matrix = matrixUtils.genMatrix(int(value[0]), int(value[1]))
        else:
            self.matrix = matrixUtils.genMatrix()

    def main(self):
        start = time.process_time()
        self.multiplyMatrix()
        end = time.process_time() - start
        print('{} {}'.format("Computation Time:", end))

    def multiplyMatrix(self):
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] *= self.matrix[x][y]

    def printSubMatrix(self):
        matrixUtils.printSubarray(self.matrix, 10)

    # Print entire matrix
    def printMatrix(self):
        print(self.matrix)

    def writeToFile(self):
        matrixUtils.writeToFile(self.matrix,"output.txt")

    def readFromFile(self):
        # input file not available
        self.matrix = matrixUtils.readFromFile("input.txt")

if __name__ == '__main__':
    matrix = MatrixMain()
    matrix.main()
    matrix.printSubMatrix()
