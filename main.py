from utils import Trie

words = ["à", "arbre", "artiste", "chape", "chapeau", "créatif", "création", "œuf", "zèbre"]


trie = Trie()
trie.add("arbre")

for w in words:
    trie.add(w)

print(trie.contains("créa"))
print(trie.contains("création"))

