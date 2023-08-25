from datetime import datetime 
from django.db.models import Q
from .models import Student, Match

from collections import defaultdict

def match_students(students):
    """
    Matches students based on their shared preferences.
    
    Args:
        students (list of Student): List of student objects.
        
    Returns:
        dict: A dictionary where keys are matched student pairs and values are their shared preferences.
    """
    # Create a dictionary to store preferences for each student
    student_preferences = defaultdict(list)
    
    # Populate student_preferences dictionary
    for student in students:
        for preference_option in student.preferences.all():
            student_preferences[student].append(preference_option)
    
 # Create a dictionary to store matched student pairs and their shared preferences
    matched_pairs = {}
    
    # Create a set to keep track of matched students
    matched_students = set()
    
    # Create a dictionary to store the current matches for each student
    current_matches = {}
    
    # Iterate through student_preferences dictionary to find matches
    for student1, preferences1 in student_preferences.items():
        for student2, preferences2 in student_preferences.items():
            if student1 != student2 and student1 not in matched_students and student2 not in matched_students:
                shared_preferences = set(preferences1) & set(preferences2)
                if shared_preferences:
                    if student2 not in current_matches or shared_preferences > current_matches[student2][1]:
                        # Update student1's match to student2
                        if student1 in current_matches:
                            matched_students.remove(current_matches[student1][0])
                        current_matches[student1] = (student2, shared_preferences)
                        matched_students.add(student2)
                        
                        # Add the match to the matched_pairs dictionary
                        matched_pairs[(student1, student2)] = shared_preferences

# Persist matched pairs into the database
    for matched_pair, shared_preferences in matched_pairs.items():
        student1, student2 = matched_pair
        
        # Check if a match between these students already exists
        existing_match = Match.objects.filter(
            (Q(match_student=student1) & Q(match_to_student=student2)) |
            (Q(match_student=student2) & Q(match_to_student=student1))
        ).first()
        
        if not existing_match:
            # Create Match instances for both directions
            match1 = Match.objects.create(
                match_student=student1,
                match_to_student=student2,
                match_date=datetime.now(),
                match_status='pending'
            )
            match2 = Match.objects.create(
                match_student=student2,
                match_to_student=student1,
                match_date=datetime.now(),
                match_status='pending'
            )
            
            # ... (add shared_preferences to the Match instances)
    
    return matched_pairs 


def get_matched_students():
    # Get all students from the database
    all_students = Student.objects.all()
    
    # Use the matching algorithm to find matched student pairs
    matched_pairs = match_students(all_students)
    
    return matched_pairs
