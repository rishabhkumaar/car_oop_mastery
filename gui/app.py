import tkinter as tk
from core.vehicle import Car, ElectricCar, SportsCar
from core.engine import Engine

def show_car_info():
    car = Car("Toyota", "Corolla", 2022, Engine("Petrol"))
    label.config(text=car.car_info())

root = tk.Tk()
root.title("Car Info GUI")

label = tk.Label(root, text="Click to show car info")
label.pack(pady=10)

btn = tk.Button(root, text="Show Car", command=show_car_info)
btn.pack()

root.mainloop()
