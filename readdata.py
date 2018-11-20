
class Data:
    def __init__(self):           
        self.line = ''
        self.n = 0       
        self.time = []
        self.dlist = []        

    def reset(self):        
        self.line
        self.n
        self.time = []
        self.dlist = []

    def _readdata(self):
        f = open("data.txt", 'r')
        while(True):
            self.line = f.readline()
            if (self.line == ""):
                break    
            self.time.append(self.line.split()[0])
            self.dlist.append(self.line.split()[1])
        f.close()
        self.n = len(self.time)
        self.time = [float (i)/1000 for i in self.time]
        self.dlist = [float (i) for i in self.dlist]        
