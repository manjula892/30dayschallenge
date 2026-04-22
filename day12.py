student = {
    "name": "Manju",
    "age": 18,
    "course": "Python"
}
# Access value
print("Name:", student["name"])
# Add new key-value pair
student["grade"] = "A"
# Loop through dictionary
print("Student details:")
for key, value in student.items():
    print(key, ":", value)