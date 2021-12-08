def get_num_intersection(subject_1 : str, subject_2 : str, choices) -> int: 
    counter : int = 0;  
    for student_choices in choices:
        if (subject_1 in student_choices) and (subject_2 in student_choices):
            counter += 1;
    return counter;
    
   
   
subject_dict = {
    "CompSci" : [0,0], 
    "Physics" : [0,0],
    "Chemistry" : [0,0],
    "Classics" : [0,0],
    "Geography" : [0,0],
    
    "Biology" : [0,0],
    "History" : [0,0],
    "Art" : [0,0],
    "Music" : [0,0],
    "Business" : [0,0],
    "Accounting" : [0,0],
    "Jewish Studies" : [0,0]
    }
 
# sample student choices in order of priority
student_choices = [
    ["CompSci", "Biology", "Physics", "Chemistry"],
     ["Classics", "CompSci", "Geography", "Biology"], 
     ["Art", "Geography", "Classics", "Biology"],
     ["CompSci", "Music", "Art", "Geography"],
     ["Physics", "Music", "Art", "Biology"],
     ["Chemistry", "Physics", "Music", "CompSci"],
     ["Geography", "History", "Classics", "Art"],
    ["Geography", "History", "Classics", "Art"],
     ["Classics", "CompSci", "Geography", "Biology"], 
     ["Art", "Geography", "Classics", "Biology"],
     ["CompSci", "Music", "Art", "Geography"],
     ["Physics", "Music", "Art", "Biology"],
      ["Classics", "CompSci", "Geography", "Biology"], 
       ["Classics", "CompSci", "Geography", "Biology"]
 
];


 
for student in student_choices:
    for priority, subject in enumerate(student):
        # priority is inverse of priority given
        subject_dict[subject][0] += (1/(priority+1));
        # update subject counter
        subject_dict[subject][1] += 1;
        
# creates a unit for "importantness" based on priority * num students
for subject in subject_dict:
    subject_dict[subject][0] *= subject_dict[subject][1];
    subject_dict[subject] = subject_dict[subject][0];
 
# fix sciences into individual bands
subject_dict["Physics"] *= 100;
subject_dict["Chemistry"] *= 100;
subject_dict["Biology"] *= 100;
subject_dict["CompSci"] *= 100;
 

bands_dict = {
    "b1" : 0,
    "b2" : 0,
    "b3" : 0,
    "b4" : 0
}


 
array_dict = {
    "b1" : [],
    "b2" : [],
    "b3" : [],
    "b4" : []
}



subjects_list = sorted(subject_dict, key=subject_dict.get, reverse=True);
 
 # iterate over each subject in subject list and each subject in band to calculate optimal band placement
for subject in subjects_list:
    for band in bands_dict:
        for sbj_in_band in array_dict[band]:
            # calculate "distance" defined by the product of the subject "importantness" multiplied by the number of students studying both subjects
            distance = subject_dict[subject] * subject_dict[sbj_in_band] * get_num_intersection(subject, sbj_in_band, student_choices);
            # add "distance" to total band "distance"
            bands_dict[band] += distance;
 
    # hack: forgot what this does
    if len(array_dict[min(bands_dict, key=bands_dict.get)]) > 2:
        bands_dict[min(bands_dict, key=bands_dict.get)] = 100000000000000000000000000000;
 
    # put subject into band of least "distance" hence least conflict between subjects
    array_dict[min(bands_dict, key=bands_dict.get)].append(subject);
    # reset band totals
    for i in bands_dict:
        bands_dict[i] = 0;
    


 
print(array_dict)   
