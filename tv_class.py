
"""
TV class
TVClass - Base class
LedTV class
PlasmaTV class
Part - A
Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume. Specify brand in a constructor parameter. Channel should be 1 by default. Volume should be 50 by default.
Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will stay at the current channel.
Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor).
It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, volume 75".
Part - B : LED , Plasma
Inherit a TV class add additional properties like screen thickness, energy usage , Lifespan , Refresh rate , functionalities like viewingAngle , Backlight, DisplayDetails , which displays the detailed features of the TV

"""
# Part A: TV Class
class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.channel = 1
        self.price = price
        self.inches = inches
        self.OnOFF = False
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

# Part B: LED TV and Plasma TV Classes
class LedTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        return (f"Brand: {self.brand}, Price: {self.price}, Inches: {self.inches}, Screen Thickness: {self.screen_thickness}, "
                f"Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}, "
                f"Viewing Angle: {self.viewing_angle}, Backlight: {self.backlight}")

class PlasmaTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle

    def display_details(self):
        return (f"Brand: {self.brand}, Price: {self.price}, Inches: {self.inches}, Screen Thickness: {self.screen_thickness}, "
                f"Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}, "
                f"Viewing Angle: {self.viewing_angle}")

# Example usage:
tv = TV("Panasonic", 500, 42)
tv.increase_volume()
tv.set_channel(10)
print(tv.status())  # Panasonic at channel 10, volume 51
tv.reset()
print(tv.status())  # Panasonic at channel 1, volume 50

led_tv = LedTV("Samsung", 1000, 55, "Thin", "Low", "10 years", "120Hz", "Wide", "LED")
print(led_tv.display_details())

plasma_tv = PlasmaTV("LG", 800, 50, "Thick", "High", "8 years", "60Hz", "Narrow")
print(plasma_tv.display_details())
