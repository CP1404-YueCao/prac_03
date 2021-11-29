def main():
    """Get scores and display grades"""
    score = float(input("Enter score: "))
    grade = determine_grades(score)
    print(f"Your score is {grade}.")


def determine_grades(score):
    """Determine grades"""
    if 90 <= score <= 100:
        return "excellent"
    elif 50 <= score < 90:
        return "pass"
    elif 0 <= score < 50:
        return "bad"
    else:
        return "invalid score"


main()
