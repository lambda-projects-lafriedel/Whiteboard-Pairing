class SuffixTrie:
    def __init__(self, string):
        self.string = string
        self.root = {}
        self.end_symbol = "*"

        for i in range(len(string)):
            new_str = string[i:]
            self.create(new_str)


    def contains(self, string):
        node = self.root
        for char in string:
            if char in node:
                node = node[char]  
            else:
                return False
        return self.end_symbol in node
    # Iterate over all the substrings babc, abc, bc, c
    # Start at the beginning "babc" and for each character, check if self.root contains that key. If it doesn't, add it as a key. It if does 
    def create(self, string):
        trie = self.root
        for char in string:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
       
        trie[self.end_symbol] = True


string = SuffixTrie('babc')
print(string.root)
print(string.contains('ab'))