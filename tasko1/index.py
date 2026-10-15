
def check_eligibility(score, documents_complete, attendance, no_disciplinary_record):

    if score < 70:
        return "FAIL", "Score is below 70"

    if not documents_complete:
        return "FAIL", "Documents are incomplete"

    if not attendance:
        return "FAIL", "Attendance condition failed"

    if not no_disciplinary_record:
        return "FAIL", "Disciplinary record condition failed"

    return "PASS", "All conditions satisfied"


test_cases = [
    {
        "name": "Case 1: Pass",
        "input": (85, True, True, True),
        "expected": "PASS"
    },
    {
        "name": "Case 2: Attendance Failure",
        "input": (85, True, False, True),
        "expected": "FAIL"
    },
    {
        "name": "Case 3: Disciplinary Condition Failure",
        "input": (85, True, True, False),
        "expected": "FAIL"
    },
    {
        "name": "Case 4: Threshold Boundary",
        "input": (70, True, True, True),
        "expected": "PASS"
    }
]

for case in test_cases:
    score, documents, attendance, record = case["input"]

    actual, reason = check_eligibility(
        score, documents, attendance, record
    )

    print("\n", case["name"])
    print("Input:", case["input"])
    print("Expected Result:", case["expected"])
    print("Actual Result:", actual)
    print("Reason:", reason)

    if actual != case["expected"]:
        print("Test Status: FAILED")
    else:
        print("Test Status: PASSED")
