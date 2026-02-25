# Recognizing simple patterns (chess-inspired)
patterns = ["fork", "pin", "skewer"]
board_threats = ["fork", "check"]

for threat in board_threats:
    if threat in patterns:
        print(f"Detected important pattern: {threat}")
