def main():
    """Get scores and determine grades"""
    score = float(input("Enter score: "))
    grade = determine_grade(score)

    if 90 <= score <= 100:
        print("Your score is excellent.")
    elif 50 <= score < 90:
        print("Your score is pass.")
    elif 0 <= score < 50:
        print("Your score is bad.")
    else:
        print("Invalid score")
