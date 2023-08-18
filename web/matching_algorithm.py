from django.utils.timezone import now as datetime_now
from .models import Student, Match

def stable_matching():
    # Get all students
    students = Student.objects.all()

    # Create a dictionary to store the preferences of each student
    preferences = {student: list(student.preferences.all()) for student in students}

    # Create a dictionary to store the current matches
    matches = {student: None for student in students}

    # While there are students who are not matched and still have preferences
    while any(matches[student] is None and preferences[student] for student in students):
        # Pick an arbitrary student who is not matched and still has preferences
        student = next(student for student in students if matches[student] is None and preferences[student])

        # Get the top preference for this student
        top_preference = preferences[student][0]

        # If the top preference is not matched yet, match them
        if matches[top_preference] is None:
            matches[student] = top_preference
            matches[top_preference] = student
        else:
            # If the top preference is already matched, check if it prefers the current student
            current_match = matches[top_preference]

            if preferences[top_preference].index(student) < preferences[top_preference].index(current_match):
                # The top preference prefers the current student, so update the matches
                matches[student] = top_preference
                matches[top_preference] = student
                matches[current_match] = None
            else:
                # The top preference prefers its current match, so remove the top preference from the current student's preferences
                preferences[student].remove(top_preference)

    # At this point, `matches` contains the stable matches
    # You can now create Match objects and save them to the database
    for student, match in matches.items():
        if student.user.id < match.user.id:  # To avoid creating two Match objects for each pair
            Match.objects.create(match_student=student, match_to_student=match, match_date=datetime_now(), match_status='pending')

#stable_matching()