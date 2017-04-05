# def names(students):
#     for i in range(len(students)):
#         print students[i]["first_name"], students[i]["last_name"]
#
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# names(students)

def user_names(users):
    # print users['Students'][1]
    print "Students"
    for i in range(len(users['Students'])):
        print i+1,"-", users['Students'][i]['first_name'], users['Students'][i]['last_name'],'-',len(users['Students'][i]['first_name']+users['Students'][i]['last_name'])
    print "Instructors"
    for x in range(len(users['Instructors'])):
        print x+1,"-", users['Instructors'][x]['first_name'], users['Instructors'][x]['last_name'],'-',len(users['Instructors'][x]['first_name']+users['Instructors'][x]['last_name'])


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
user_names(users)
