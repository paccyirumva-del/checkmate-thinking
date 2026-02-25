# Make decisions under time constraints
def execute_action(time_remaining, importance):
    if time_remaining > importance:
        return "Execute confidently"
    else:
        return "Pause and plan"

print(execute_action(5, 3))
print(execute_action(2, 4))
