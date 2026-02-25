# Simple risk vs reward analysis inspired by chess
def analyze_risk(risk, reward):
    if reward > 2 * risk:
        return "High reward, low risk – take it"
    elif reward > risk:
        return "Moderate reward – evaluate carefully"
    else:
        return "Too risky – wait"
    
print(analyze_risk(3, 7))
print(analyze_risk(4, 5))
