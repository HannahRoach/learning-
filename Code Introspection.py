class Vehicle:
    name = ""
    kind = "truck"
    color = ""
    value = 1000.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

print(dir(Vehicle))