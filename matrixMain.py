#!/usr/bin/env python3
import matrixUtils, time, pymp

class MatrixMain():
    def __init__(self):
        value = input("Input custom size and value? Or use standard size=1024, value=1? \nExample Input: 10 5\n")
        if value is not "":
            value = value.split(" ")
            self.matrix = pymp.shared.array((int(value[0]),int(value[0])), dtype='intc')
            self.assignVals(value[1])
            #self.matrix = matrixUtils.genMatrix(int(value[0]), int(value[1]))
        else:
            self.matrix = pymp.shared.array((1024,1024),dtype='intc')
            self.assignVals(1)
            #self.matrix = matrixUtils.genMatrix()

    def assignVals(self, value):
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] = value

    def main(self):
        start = time.process_time()
        self.multiplyMatrix()
        end = time.process_time() - start
        print('{} {}'.format("Computation Time:", end))

    def multiplyMatrix(self):
        with pymp.Parallel(8) as p:
            print('Thread {} of {}'.format(p.thread_num,p.num_threads))
            for x in p.range(0,len(self.matrix)):
                for y in range(0,len(self.matrix[x])):
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
    #matrix.printSubMatrix()
    matrix.printMatrix()
