import datetime
import tkinter as tk
from tkinter import ttk
import sqlite3

from Measurement import Measurement


class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.measurements = None
        self.title("Measurements")
        self.geometry("950x250")
        self.create_widgets()

        # Connect to the SQLite database
        self.conn = sqlite3.connect("measurements.db")
        self.cursor = self.conn.cursor()

    def create_widgets(self):
        # Buttons and label
        label = tk.Label(self, text="Measurements")
        label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        heartbeat_button = tk.Button(self, text="Heartbeat", command=self.heartbeat)
        heartbeat_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        alcohol_button = tk.Button(self, text="Alcohol", command=self.alcohol)
        alcohol_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # List with data
        self.measurements = ttk.Treeview(self, columns=("Day", "Average", "State", "Difference"), show="headings")
        self.measurements.heading("Day", text="Day")
        self.measurements.heading("Average", text="Average")
        self.measurements.heading("State", text="State")
        self.measurements.heading("Difference", text="Difference")
        self.measurements.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

        # Create a vertical scrollbar for the measurements treeview
        scrollbar_measurements = ttk.Scrollbar(self, orient="vertical", command=self.measurements.yview)
        scrollbar_measurements.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="ns")

        # Configure the measurements treeview to use the scrollbar
        self.measurements.configure(yscrollcommand=scrollbar_measurements.set)

    currently_heartbeat = False
    currently_alcohol = False
    alcohol_limit = 10

    def heartbeat(self):
        if not self.currently_heartbeat:
            self.currently_heartbeat = True
            self.currently_alcohol = False
            self.clear_data_list()

        self.display_heartbeat_data()

    def alcohol(self):
        if not self.currently_alcohol:
            self.currently_heartbeat = False
            self.currently_alcohol = True
            self.clear_data_list()

        self.display_alcohol_data()

    def clear_data_list(self):
        self.measurements.delete(*self.measurements.get_children())

    def add_item_to_data_list(self, day, average, state, difference):
        self.measurements.insert("", "end", values=(day, average, state, difference))

    def display_heartbeat_data(self):
        self.clear_data_list()

        # Fetch measurements from the database
        self.cursor.execute("SELECT * FROM measurement")
        measurements = self.cursor.fetchall()

        prev_measurement = 0;
        for measurement in measurements:
            day = measurement[0]
            value = measurement[2]
            healthytext = "Healthy"
            if value > 60 or value < 100:
                healthytext = "Unhealthy"
            self.add_item_to_data_list(day, str(value) + " BPM", healthytext,
                                       self.give_arrow(value - prev_measurement))
            prev_measurement = value

    def display_alcohol_data(self):
        self.clear_data_list()

        # Fetch measurements from the database
        self.cursor.execute("SELECT * FROM measurement")
        measurements = self.cursor.fetchall()

        prev_measurement = 0;
        for measurement in measurements:
            day = measurement[0]
            value = measurement[1]
            healthytext = "Healthy"
            if value < 60 or value > 100:
                healthytext = "Unhealthy"
            self.add_item_to_data_list(day, str(value) + "%", healthytext,
                                       self.give_arrow(value - prev_measurement))
            prev_measurement = value

    def give_arrow(self, number):
        if number < 0:
            number = number * -1;
            return "▼" + str(number)
        if number > 0:
            return "▲" + str(number)
        return "■" + str(number)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
