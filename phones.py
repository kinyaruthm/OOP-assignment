# assignment 2
class Smartphone:
    def use(self):
        raise NotImplementedError("Subclasses must implement this method")

class iPhone(Smartphone):
    def use(self):
        print("Using iPhone Smooth iOS experience with Face ID")

class Samsung(Smartphone):
    def use(self):
        print("Using Samsung Android multitasking and S-Pen features")

class Pixel(Smartphone):
    def use(self):
        print("Using Google Pixel Clean Android and top-tier camera")

phone1 = iPhone()
phone2 = Samsung()
phone3 = Pixel()

for phone in [phone1, phone2, phone3]:
    phone.use()
