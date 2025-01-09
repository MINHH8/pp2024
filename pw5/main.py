from input import *
from output import *
from domains.gpa import *

if __name__ == "__main__":
    stdlst = []
    cslst = []
    mrk_list =[]
    
while True:
        Opt = int(
            input("""
        [Student mark management]
        1. Add student information
        2. Add course information
        3. List of students
        4. List of courses
        5. Add mark
        6. List mark
        7. GPA
        8. Sort GPA
        9. Exit
        Opt:
        """
        )
        )
                
        if Opt == 1:
            studentInfo(stdlst)
        elif Opt == 2:
            courseInfo(cslst)
        elif Opt == 3:       
            std_list(stdlst)    
        elif Opt== 4:
            course_list(cslst)
        elif Opt == 5:
            mark_info( cslst,stdlst, mrk_list)
        elif Opt == 6:
            mark_list(mrk_list)
        elif Opt==7:
            avg_gpa(stdlst,mrk_list)
        elif Opt == 8:    
            print_sorted_gpa(gpa_list)
        elif Opt == 9:
            break


