students = {
    "Alice": ("Math", "English", "Biology"),
    "Bob": ("Math", "Chemistry", "Physics"),
    "Charlie": ("History", "Math", "English")
}

alice_subject = students["Alice"]
unique_subjects = set(students["Alice"])|set(students["Bob"])|set(students["Charlie"])
charlie = "Math" in set(students["Charlie"])

print(alice_subject)
print(unique_subjects)
print(charlie)