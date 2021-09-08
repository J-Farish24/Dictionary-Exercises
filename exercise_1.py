#Create dictionaries 
course_and_room = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755,
'NT110': 1244, 'CM241': 1411}

course_and_instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich',
'NT110': 'Burke', 'CM241': 'Lee'}

course_and_meetingtime = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.',
'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}

course = input('Please enter a couse number to view its information: ')

print(course_and_room[course])
print(course_and_instructor[course])
print(course_and_meetingtime[course])