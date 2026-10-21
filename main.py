from pyscript import display, document




def add_member(e):
    document.getElementById('add').innerHTML = ' '
    fname = document.getElementById('first_name').value
    lname = document.getElementById('last_name').value
    grade_7 = {'Nathan Gonzales'}
    grade_8 = {'Sean Bautista'}
    grade_9 = {'Ethan Pascua'}
    grade_10 = {'Rachmiel Lozada'}
    master_set = grade_7 | grade_8 | grade_9 | grade_10
    master_set.add(fname and lname)

    display(master_set, target='add')