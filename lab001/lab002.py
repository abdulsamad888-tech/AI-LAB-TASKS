
test_cases = [
    (80, True, 80, True, "Approved",
     "All conditions are satisfied"),

    (80, True, 70, True, "Rejected",
     "Attendance is below 75%"),

    (80, True, 80, False, "Rejected",
     "Interview was not passed"),

    (70, True, 75, True, "Approved",
     "Score and attendance meet the minimum thresholds")
]

for score, documents, attendance, interview, expected, reason in test_cases:

    if score >= 70 and documents and attendance >= 75 and interview:
        actual = "Approved"
    else:
        actual = "Rejected"

    print("Score:", score)
    print("Documents complete:", documents)
    print("Attendance:", attendance)
    print("Interview passed:", interview)

    print("Expected result:", expected)
    print("Actual result:", actual)
    print("Reason:", reason)
