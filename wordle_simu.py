import random
from solver import WordleSolver
from enum import Enum, auto
from tqdm import tqdm

class GameState(Enum):
    START = auto()
    END = auto()



class WordleSimulator(object):
    def __init__(self, answer_list):
        self.answer_list = answer_list
        self.reset_game_state()
    
    def reset_game_state(self):
        self.state = GameState.END
        self.step = 0
    
    def wordle(self, initial_query, solver, answer=""):
        self.answer = answer if answer else random.choice(self.answer_list)
        self.state = GameState.START
        query = initial_query
        while not self.state == GameState.END:
            self.step += 1
            cue = self.to_pattern(query, self.answer)
            if cue == ("2", "2", "2", "2", "2"):
                step = self.step
                self.reset_game_state()
                return step
            query = solver.next_word(query, cue)

    def simurate_solver_paformance(self, initial_query, solver):
        steps = []
        for answer in tqdm(self.answer_list):
            step = self.wordle(initial_query, solver, answer=answer)
            steps.append(step)
            solver.reset()
        print(f"average step: {sum(steps)/len(steps)}")

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

def load_answers(path):
    vocab = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            vocab.append(line)
    return vocab

if __name__ == "__main__":
    answers_path = "answers.dict"
    answer_list = load_answers(answers_path)
    simu = WordleSimulator(answer_list)

    dict_path = "dictionary.dict"    
    solver = WordleSolver(dict_path)
    initial_query = "tares"

    simu.simurate_solver_paformance(initial_query, solver)