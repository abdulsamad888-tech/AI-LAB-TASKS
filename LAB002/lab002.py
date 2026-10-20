
previous_mode = None

def control_system(temperature, occupied):
    global previous_mode

    if not occupied:
        target_mode = "OFF"
    elif temperature < 18:
        target_mode = "HEAT"
    elif temperature > 28:
        target_mode = "COOL"
    else:
        target_mode = "OFF"

    if target_mode != previous_mode:
        command = "SEND CMD"
    else:
        command = "NO CMD"

    old_mode = previous_mode
    previous_mode = target_mode

    return old_mode, target_mode, command


percepts = [
    (15, True),
    (15, True),
    (18, True),
    (28, True),
    (30, True),
    (30, True),
    (22, False)
]

for temperature, occupied in percepts:
    old, target, command = control_system(temperature, occupied)


    print("Percept:", temperature, "C, CMD:", occupied)
    print("Target mode:", target)
    print("Outcome:", command)