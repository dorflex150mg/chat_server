class ConvBook:
    pairs_convs = {}
    pairs_convs_last = {}

    def add(self, pair):
        self.pairs_convs[pair] = []
        self.pairs_convs_last[pair] = 0
    
    def getConv(self, pair):
        conv = self.pairs_convs[pair]
        self.pairs_convs[pair] = []
        return [conv, self.pairs_convs_last[pair]]
    
    def checked(self, pair, last):
        if self.pairs_convs_last[pair] > last:
            return False 
        return True

    def append(self, pair, msg):
        self.pairs_convs[pair].append(msg)
        self.paris_convs_last[pair] += 1
