biodata = {
    "name": "Varad",
    "subject": ["C", "PYTHON", "JAVA", "HTML", "CSS"],
    "age": 17,
    "citizenship": "INDIAN",
    "topics learned": "dictionary",
}

print(biodata["subject"])
print(biodata["age"])
print(biodata["citizenship"])
print(biodata["topics learned"])
print(biodata)
biodata["name"] = "SHARAD"
print(biodata["name"])

print(biodata)
# 2
students = {
    "student_name": "VARAD",
    "subjects": {
        "physics": 97,
        "chemistry": 91,
        "maths": 90,
        "english": 89,
    },
    "other_activity": {
        "sports": ["cricket", "football", "chess"],
        "technical_events": "Enigma",
    }
}
print(students)
print(students["other_activity"]["sports"])
print(students["subjects"]["maths"])
print(len(students))
print(list(students.keys()))
print(students.values()) #returns all values
print(students.items())#returns all (key, val) pairs as tuples
#pratice dictionary
information={
    "name" : "varad",
    "cars" :["jaguar","bugati","lamborgini","supra","fortuner"],
    "date of order" : "17/1/2025",
    "date of delivery" : "29/1/2025",
}
print(information["cars"])
print(information.keys())
print(information.values())
print(information.items())
print(information)
