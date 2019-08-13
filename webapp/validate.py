def validate(input):
    labels = {'crime_rate',
              'avg_number_of_rooms',
              'distance_to_employment_centers',
              'property_tax_rate',
              'pupil_teacher_ratio'
              }
    #print(f"Label check: {[x in input for x in labels]}")
    #print(f"Type check: {[isinstance(input[x], (int, float)) for x in labels]}")
    if not all([x in input for x in labels]):
        return False
    elif not all([isinstance(input[x], (int, float)) for x in labels]):
        return False
    else:
        return True