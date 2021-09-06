class Garden:
    plant_names = {"V": "Violets", "R": "Radishes", "G": "Grass", "C": "Clover"}

    def __init__(self, diagram, students=()):
        if not students:
            students = (
                "Alice",
                "Bob",
                "Charlie",
                "David",
                "Eve",
                "Fred",
                "Ginny",
                "Harriet",
                "Ileana",
                "Joseph",
                "Kincaid",
                "Larry",
            )

        self.students = sorted(students)
        self.rows = diagram.split("\n")

    def plants(self, name):
        index = self.students.index(name) * 2
        result = [
            self.rows[0][index],
            self.rows[0][index + 1],
            self.rows[1][index],
            self.rows[1][index + 1],
        ]
        result = [self.plant_names.get(plant) for plant in result]

        return result
