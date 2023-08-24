from django.utils.timezone import now as datetime_now
from .models import Student, Preference, PreferenceOption, Match

def stable_matching():
    # Get all students
    students = Student.objects.all()

    # Create a dictionary to store the preferences of each preference option
    preferences = {preference_option: list(Student.objects.filter(preferences=preference_option)) for preference_option in PreferenceOption.objects.all()}

    # Create a dictionary to store the current matches
    matches = {student: None for student in students}

    while any(matches[student] is None for student in students):
        student = next(student for student in students if matches[student] is None)

        # Get the top preference for this student
        top_preference = preferences[student.preferences.all()[0]][0]

        if matches[top_preference] is None:
            matches[student] = top_preference
            matches[top_preference] = student
        else:
            current_match = matches[top_preference]

            if preferences[top_preference].index(student) < preferences[top_preference].index(current_match):
                matches[student] = top_preference
                matches[top_preference] = student
                matches[current_match] = None
            else:
                # Remove the top preference from the current student's preferences
                preferences[student.preferences.all()[0]].remove(top_preference)
        
    return matches
