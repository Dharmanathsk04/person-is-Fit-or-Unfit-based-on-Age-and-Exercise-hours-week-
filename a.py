from sklearn.tree import DecisionTreeClassifier


x = [
    [25, 5], [30, 4], [45, 1],
    [50, 0], [35, 3], [60, 2]
]


y = ["fit", "fit", "unfit", "unfit", "fit", "unfit"]


model = DecisionTreeClassifier()
model.fit(x, y)


age = int(input("Enter Age: "))
exercise = int(input("Enter Exercise hours per week: "))

person = [[age, exercise]]
prediction = model.predict(person)

print(f"Person (Age = {age}, Exercise = {exercise}h/week) -> {prediction[0]}")
