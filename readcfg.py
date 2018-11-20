
class Configuration:
    def __init__(self):
        self.line = []
        self.listline = []
        self.xstart = []
        self.xend = []
        self.ystart = []
        self.yend = []

    def reset(self):
        self.xstart = []
        self.xend = []
        self.ystart = []
        self.yend = []

    def _readcfg(self):
        f = open("config.txt",'r')
        while(True):
            self.line=f.readline()
            if (self.line == ""):
                break  
            self.listline.append(self.line)
        for i in range(0,(int)(len(self.listline)/2)) :
            self.xstart.append((float)(self.listline[2*i].split()[2]))
            self.xend.append((float)(self.listline[2*i].split()[4]))
            self.ystart.append((float)(self.listline[2*i+1].split()[2]))
            self.yend.append((float)(self.listline[2*i+1].split()[4]))  
        f.close()
