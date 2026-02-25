# Simple chess-inspired move logic
def choose_move(risk_level, reward):
    if reward > risk_level:
        return "Make the move"
    else:
        return "Wait and improve position"

print(choose_move(3, 5))
