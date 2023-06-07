import math
import random

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def expand(self):
        moves = self.state.get_possible_moves()
        for move in moves:
            new_state = self.state.make_move(move)
            new_node = Node(new_state, parent=self)
            self.children.append(new_node)

    def select_child(self, exploration_constant=1.4):
        best_score = float('-inf')
        best_child = None
        for child in self.children:
            exploit_score = child.wins / (child.visits+1)
            explore_score = math.sqrt(2 * math.log(self.visits) / (child.visits+1))
            score = exploit_score + exploration_constant * explore_score
            if score > best_score:
                best_score = score
                best_child = child
        return best_child

    def simulate(self):
        state = self.state
        while not state.is_terminal():
            move = random.choice(state.get_possible_moves())
            state = state.make_move(move)
        return state.get_winner()

    def backpropagate(self, result):
        node = self
        while node is not None:
            node.visits += 1
            if result == node.state.current_player:
                node.wins += 1
            node = node.parent

    def mcts_search(self, iterations):
        for _ in range(iterations):
            node = self
            while node.children:
                node = node.select_child()
            if not node.state.is_terminal():
                node.expand()
                node = random.choice(node.children)
            result = node.simulate()
            node.backpropagate(result)

class GameState:
    def __init__(self):
        self.current_player = 1  # Player 1 goes first
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Empty 3x3 board

    def get_possible_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    moves.append((i, j))
        return moves

    def make_move(self, move):
        i, j = move
        new_state = GameState()
        new_state.current_player = -self.current_player  # Switch players
        new_state.board = [row.copy() for row in self.board]
        new_state.board[i][j] = self.current_player
        return new_state

    def is_terminal(self):
        return self.get_winner() != 0 or self.is_board_full()

    def get_winner(self):
        for player in [-1, 1]:
            for i in range(3):
                if self.board[i] == [player] * 3:
                    return player
                if all(self.board[j][i] == player for j in range(3)):
                    return player
            # Check diagonals
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
                return player
            if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
                return player
        return 0

    def is_board_full(self):
        return all(all(cell != 0 for cell in row) for row in self.board)
initial_state = GameState()
root_node = Node(initial_state)
iterations = 1000
root_node.mcts_search(iterations)
best_child = root_node.select_child()
best_move = best_child.state.get_possible_moves()[0]

print("Best move:", best_move)
