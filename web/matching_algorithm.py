from django.utils.timezone import now as datetime_now
from .models import Student, Preference, PreferenceOption, Match

# matching_algorithm.py

def stable_matching():
    # Get all students
    students = Student.objects.all()

    # Create a dictionary to store the preferences of each student
    preferences = {student: list(student.preferences.all()) for student in students}

    # Create a dictionary to store the current matches
    matches = {student: None for student in students} 
    #matches = {preference: None for preference in students}

    # Debugging: Print the preferences dictionary
    #print("Preferences:")
    #for student, prefs in preferences.items():
    #    print(student, prefs)

    # While there are students who are not matched and still have preferences
    while any(matches[student] is None and preferences[student] for student in students):
        # Pick an arbitrary student who is not matched and still has preferences
        student = next(student for student in students if matches[student] is None and preferences[student])

        # Get the top preference for this student
        top_preference = preferences[student][0]

        # Debugging: Print the current student and top preference
        #print("Current Student:", student)
        #print("Top Preference:", top_preference)
        #code tested OK up till this point

        # If the top preference is not matched yet, match them
        #if matches[top_preference] is None:
        if matches[student] is None:
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
        
        # Debugging: Print the matches dictionary
        #print("Matches:")
        #for student, match in matches.items():
         #   print(student, match)

        return matches
'''
    # At this point, `matches` contains the stable matches
    # You can now create Match objects and save them to the database
    for student, match in matches.items():
        if student.user.id < match.user.id:  # To avoid creating two Match objects for each pair
            Match.objects.create(match_student=student, match_to_student=match, match_date=datetime_now(), match_status='pending')

#stable_matching()
'''