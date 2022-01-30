import os
import math
import itertools
from collections import defaultdict
from tqdm import tqdm
#
# condition: cue.
#            0 -> not in the word in any spot.
#            1 -> in the word but in the wrong spot.
#            2 -> in the word and in the correct spot.
#
#

class WordleSolver(object):
    def __init__(self, dict_path):
        self.dict_path = dict_path
        self.raw_vocab = self._load_dict(self.dict_path)
        self.vocab = self.raw_vocab
    
    def reset(self):
        self.vocab = self.raw_vocab
    
    def next_word(self, query, condition):
        self.vocab = self._conditioning(query, condition)
        word_ent_table = {}
        for word in self.vocab:
            entropy = self.calc_entropy(word)
            word_ent_table[word] = entropy
        sorted_word_ent_table = sorted(word_ent_table.items(), key=lambda x:x[1], reverse=True)
        return sorted_word_ent_table[0][0]
    
    def _conditioning(self, query, condition):
        new_vocab = []
        for word in self.vocab:
            if self._is_meet_condition(word, query, condition) and not query == word:
                new_vocab.append(word)
        return new_vocab
    
    def _is_meet_condition(self, word, query, condition):
        already_mentioned = set()
        for i, cond in enumerate(condition):
            if cond == "0":
                if query[i] in word and not query[i] in already_mentioned:
                    return False
            if cond == "1":
                if query[i] == word[i] or not (query[i] in word):
                    return False
                else: already_mentioned.add(query[i])
            if cond == "2":
                if not query[i] == word[i]:
                    return False
                else: already_mentioned.add(query[i])
        return True

    def to_pattern(self, query, answer):
        condition = ["0"] * 5
        already_mentioned = set()
        for i, char in enumerate(query):
            if char == answer[i]:
                condition[i] = "2"
                already_mentioned.add(char)
            if char in answer and not (char in already_mentioned):
                condition[i] = "1"
                already_mentioned.add(char)
        return tuple(condition)

    def calc_entropy(self, query):
        sum_entropy = 0.0
        words_meet_condition = []
        vocab_size = len(self.vocab)
        pattern_count = defaultdict(int)
        # answerが答えであった時の色のパターンを考える
        for answer in self.vocab:
            pattern = self.to_pattern(query, answer)
            pattern_count[pattern] += 1
        entropy = sum([-(count / vocab_size) * math.log2(count / vocab_size) for count in pattern_count.values()])

        return entropy

    def best_initial_query(self, out_path=""):
        out_path = out_path if out_path else f"result_{os.path.basename(self.dict_path)}.txt"
        word_ent_table = {}
        for word in tqdm(self.vocab):
            entropy = self.calc_entropy(word)
            word_ent_table[word] = entropy
        
        sorted_word_ent_table = sorted(word_ent_table.items(), key=lambda x:x[1], reverse=True)

        with open(out_path, "w") as f:
            for word, entropy in sorted_word_ent_table:
                line = f"{word}\t{entropy}\n"
                f.write(line)

    def _load_dict(self, path):
        vocab = []
        with open(path) as f:
            for line in f:
                line = line.strip()
                vocab.append(line)
        return vocab


if __name__ == "__main__":
    dict_path = "dictionary.dict"
    out_path = "best_initial_query.txt"
    solver = WordleSolver(dict_path)
    solver.best_initial_query(out_path=out_path)