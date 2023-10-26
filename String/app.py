# String for multiple line's
email = '''
Hello there,

welcome to the course.
it's really helpful course to me. I want to
explore it.

Thank you.
'''
print(email)

course = 'Python course for Beginners'
print(course[0])  # index of each character. P
print(course[-1])  # index from last. s
print(course[0:3])  # index 0 to 2, 3 index exclude. Pyt
print(course[1:])  # index 1 to last. ython course for Beginners
print(course[:5])  # default 0 to 4. Pytho
print(course[:])  # 0 index to length, use for copying string. Python course for Beginners
another_course = course[:]
print(another_course)  # copying. Python course for Beginners

name = "Jennifer"
print(name[1:-1])  # excluding -1 index. ennife
