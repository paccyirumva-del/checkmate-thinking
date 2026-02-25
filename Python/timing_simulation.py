# Simple timing example inspired by chess tempo
def decide_action(time_left, complexity):
    if time_left > complexity:
        return "Proceed with action"
    else:
        return "Pause and reassess"

print(decide_action(5, 3))
