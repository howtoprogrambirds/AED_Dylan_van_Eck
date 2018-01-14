class trie_node:
    def __init__(self, num=0, dic={}):
        self.num   = num;
        self.dic   = dic;

    def insert(self, word):
        buffer = self;
        for i in range(len(word)):
            char = word[i];
            if char in buffer.dic.keys():
                buffer = buffer.dic[char];
            else:
                buffer.dic[char] = trie_node(0, {});
                buffer = buffer.dic[char];
            if i is len(word)-1:
                buffer.num += 1;

    def find(self, word):
        buffer = self;
        for char in word:
            if char in buffer.dic.keys():
                buffer = buffer.dic[char];
            else:
                return None;
        return buffer;

def write_Dic_to_file(name, dic):
    file = open(name, 'w');
    for i in sorted(dic):
        file.write(i);
        file.write(" || ");
        file.write(str(dic[i]));
        file.write("\n");

def main_trie(iname, oname):
    dic = {};
    list = [];
    trie = trie_node(1);
    file = open(iname, 'r');
    buffer = file.read();
    buffer = buffer.split();
    for word in buffer:
        buffer_word = '';
        for char in word:
            if char.isalpha():
                buffer_word += char;
            else:
                continue;
        if buffer_word:
            trie.insert(buffer_word);
            list.append(buffer_word);
    for i in list:
        node = trie.find(i);
        dic[i] = node.num;
    write_Dic_to_file(oname, dic);

main_trie("lyrics.txt", "outputfile.txt");