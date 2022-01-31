import random
from solver import WordleSolver, to_pattern
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
            cue = to_pattern(query, self.answer)
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