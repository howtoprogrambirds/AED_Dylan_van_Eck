import random

class hash_entry:
    def __init__(self,element,isActive):
        self.elementSet = set({})
        self.elementSet.add(element)
        self.isActive = isActive


class seperate_chain_hash_table:
    def __init__(self):
        self.len = 3;
        self.size = 0;
        self.used = 0;
        self.table = [None]*self.len
        print("len: " + str(self.len))

    def __repr__(self):
        s = "==============\n"
        for i in range(self.len):
            if self.table[i]!= None:
                s = s + '(' + str(i) + ',' + str(self.table[i].elementSet) + ',' + str(self.table[i].isActive) + ")\n"
        s = s + 'lenght: ' + str(self.len) + '\n'
        s = s + 'size: ' + str(self.size) + '\n'
        s = s + 'used: ' + str(self.used) + '\n'
        s = s + '-----------------\n'
        return s

    def get_pos(self, e):
        buffer = hash(e) % self.len;
        return buffer;

    def search(self, e):
        buffer = self.get_pos(e)
        if self.table[buffer] != None and self.table[buffer].isActive:
            for element in self.table[buffer].elementSet:
                if element == e:
                    return element
        return -1

    def rehash(self, newLen):
        print(self)
        if newLen >= self.size:
            oldLen = self.len
            oldTable = self.table

            self.size = 0
            self.used = 0
            self.len = newLen
            self.table = [None]*self.len

            for i in range(oldLen):
                if oldTable[i] != None and oldTable[i].isActive:
                    for element in oldTable[i].elementSet:
                        self.insert(element)
            print("rehash: len: " + str(self.len))
            print(self)

    def insert(self, e):
        buffer = self.get_pos(e)
        if self.table[buffer] == None:
            self.table[buffer] = hash_entry(e, True)
            self.size += 1
            self.used += 1
        elif not self.table[buffer].isActive:
            self.table[buffer].isActive = True
            self.table[buffer].elementSet += e
            self.used += 1
        else:  # if exists and is active
            if e not in self.table[buffer].elementSet:
                self.table[buffer].elementSet.add(e)
                self.used += 1
                return buffer
            return -1
        if self.used > 0.75 * self.len:
            self.rehash(2 * self.len)
        return buffer

    def delete(self, e):
        self.search(e)
        del e
        self.used -= 1

if __name__ == '__main__':
    hash_table = seperate_chain_hash_table()
    random_broken_list = [random.uniform(1, 100) for i in range(200)]

    for i in range(200):
        hash_table.insert(random_broken_list[i])
    print("erase")
    for i in range(0, 200, 2):
        hash_table.delete(random_broken_list[i])
    print(hash_table)
