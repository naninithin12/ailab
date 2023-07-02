class PuzzleState:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.heuristic = self.calculate_heuristic()
    def calculate_heuristic(self):
        misplaced = 0
        goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        for i in range(9):
            if self.puzzle[i] != goal_state[i]:
                misplaced += 1
        return misplaced
    
    def is_goal_state(self):
        return self.puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_next_moves(self):
        moves = []
        empty_index = self.puzzle.index(0)
        possible_moves = [
            empty_index - 3,  # move up
            empty_index + 3,  # move down
            empty_index - 1,  # move left
            empty_index + 1   # move right
        ]
        for move in possible_moves:
            if 0 <= move < 9:
                new_puzzle = self.puzzle[:]
                new_puzzle[empty_index], new_puzzle[move] = new_puzzle[move], new_puzzle[empty_index]
                moves.append(PuzzleState(new_puzzle))
        return moves

    def print_state(self):
        for i in range(0, 9, 3):
            print(self.puzzle[i:i+3])

def greedy_best_first_search(initial_state):
    visited = set()
    current_state = initial_state

    while not current_state.is_goal_state():
        current_state.print_state()
        print()

        visited.add(tuple(current_state.puzzle))
        next_moves = current_state.get_next_moves()

        next_moves = sorted(next_moves, key=lambda x: x.heuristic)

        found_new_state = False
        for move in next_moves:
            if tuple(move.puzzle) not in visited:
                current_state = move
                found_new_state = True
                break

        if not found_new_state:
            print("No solution found.")
            return

    print("Goal state reached!")
    current_state.print_state()

puzzle = PuzzleState([1, 2, 3, 4, 0, 5, 7, 8, 6])
greedy_best_first_search(puzzle)
