# src/trie.py
"""
Trie data structure for autocomplete.

Public surface expected by tests:
- class Trie
  - insert(word: str, freq: float) -> None
  - remove(word: str) -> bool
  - contains(word: str) -> bool
  - complete(prefix: str, k: int) -> list[str]
  - stats() -> tuple[int, int, int]  # (words, height, nodes)

Complexity target (justify in docstrings):
- insert/remove/contains: O(len(word))
- complete(prefix, k): roughly O(m + k log k')
"""

class TrieNode:
    __slots__ = ("children", "is_word", "freq")

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.freq = 0.0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self._words = 0
        self._nodes = 1

    def insert(self, word, freq):
        # TODO: implement
        raise NotImplementedError

    def remove(self, word):
        # TODO: implement
        raise NotImplementedError

    def contains(self, word):
        # TODO: implement
        raise NotImplementedError

    def complete(self, prefix, k):
        # TODO: implement
        raise NotImplementedError

    def stats(self):
        # TODO: implement: return (words, height, nodes)
        raise NotImplementedError
