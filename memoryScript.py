class memory:

    position = 0
    
    def __init__(self):

        memoryFile = open("memory.txt", "r")
        self.position = int(memoryFile.readline())
        memoryFile.close()


    def savePosition(self, posNum):
        memoryFile = open("memory.txt","w")
        memoryFile.write(posNum)
        memoryFile.close()

    def getPosition(self):
        memoryFile = open("memory.txt","r")
        pos = int(memoryFile.readline())
        memoryFile.close()
        return pos

    def switchUpdate(self):
        
        self.position = int(self.position + 1)

        if self.position == 4:
            self.position = 0
            self.savePosition(str(self.position))

        self.savePosition(str(self.position))
        return self.position


k = memory()

k.switchUpdate()

print(k.getPosition())
