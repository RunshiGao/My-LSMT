from SkipList import SkipList
class LSMTree:
    def __init__(self, max_lvl=None, P=None):
        if max_lvl != None and P != None:
            self.max_lvl = max_lvl
            self.P = P
        else:
            self.max_lvl = 3
            self.P = 0.5

        self.memtable = SkipList(self.max_lvl, self.P)

    def put(self, key) -> None:
        self.memtable.insert(key)

    def get(self, key) -> bool:
        return self.memtable.search(key)
    
    def print(self):
        self.memtable.displayList()

    # Function to read a text file and insert keys into the memtable
    def insert_keys_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                keys = line.strip().split(',')  # Assuming key-value pairs are separated by comma
                for key in keys:
                    self.put(key)

