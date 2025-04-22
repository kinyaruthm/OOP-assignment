# Parent class
class Phone:
    def __init__(self, brand, camera, display):
        self.brand = brand
        self.camera = camera
        self.display = display

    def show_details(self):
        return f"{self.brand} Phone\nCamera: {self.camera}\nDisplay: {self.display}"

    def feature(self):
        return "Basic phone features."


# childclass 1
class Smartphone(Phone):
    def __init__(self, camera, display):
        super().__init__("Samsung", camera, display)

    def feature(self):
        return "Has compelling features including advanced camera systems."


# childclass 2
class BasicPhone(Phone):
    def __init__(self, camera, display):
        super().__init__("Nokia", camera, display)

    def feature(self):
        return "User-friendly interface with essential functions."


# Instantiate objects
phone1 = Smartphone("zoom capabilities", "Bright display")
phone2 = BasicPhone("8MP", "LCD")

# Polymorphism: Loop over both
for phone in [phone1, phone2]:
    print(phone.show_details())
    print("Features:", phone.feature())
    print("-" * 40)
