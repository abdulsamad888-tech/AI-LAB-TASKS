
class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None
    def act(self, temp, occupied):
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"
        command_should_be_sent = (
            target_mode != self.previous_mode
        )

        self.previous_mode = target_mode

        return target_mode, command_should_be_sent


agent = ClassroomAgent()

percepts = [(29, True),(29, True),(20, True),(26, True),(19, True),(29, False),(29, False)]

print("Step | Previous | Percept | Target | Outcome")

for step, percept in enumerate(percepts, 1):
    previous = agent.previous_mode

    target, send_command = agent.act(*percept)

    outcome = "SEND" if send_command else "NO SEND"

    print(step, previous, percept, target, outcome)
