def counter(name):
    dic = {};
    list = [];
    file = open(name, 'r');
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
            list.append(buffer_word);
    for word in list:
        if word in dic:
            dic[word] += 1;
        else:
            dic[word] = 1;
    return dic;

def write_Dic_to_file(name, dic):
    file = open(name, 'w');
    for i in sorted(dic):
        file.write(i);
        file.write(" || ");
        file.write(str(dic[i]));
        file.write("\n");

write_Dic_to_file("outputfile.txt", counter("lyrics.txt"));