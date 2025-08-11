import pickle
import os

def save_garage(garage, filename="data/garage.pkl"):
    # Ensure the folder exists before saving
    folder = os.path.dirname(filename)
    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(filename, "wb") as f:
        pickle.dump(garage, f)

def load_garage(filename="data/garage.pkl"):
    if not os.path.exists(filename):
        return []
    with open(filename, "rb") as f:
        return pickle.load(f)
