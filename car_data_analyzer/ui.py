# ui.py
import tkinter as tk
from tkinter import filedialog, messagebox
from car_data_analyzer.main import CarDataAnalyzer


class CarDataAnalyzerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Data Analyzer")
        self.root.configure(bg='#f0f0f0')  # Background color

        # Styles
        self.label_style = {'bg': '#f0f0f0', 'fg': '#333', 'font': ('Arial', 12)}
        self.entry_style = {'bg': '#fff', 'fg': '#333', 'font': ('Arial', 12)}
        self.button_style = {'bg': '#4CAF50', 'fg': '#fff', 'font': ('Arial', 12), 'activebackground': '#45a049'}

        # Input JSON File
        self.input_file_label = tk.Label(root, text="Input JSON File:", **self.label_style)
        self.input_file_label.pack(pady=5)
        self.input_file_entry = tk.Entry(root, width=80, **self.entry_style)
        self.input_file_entry.pack(pady=5)
        self.browse_input_button = tk.Button(root, text="Browse", command=self.browse_input_file, **self.button_style)
        self.browse_input_button.pack(pady=5)
        self.input_file_status = tk.Label(root, text="", **self.label_style)
        self.input_file_status.pack(pady=5)

        # Output CSV File
        self.output_file_label = tk.Label(root, text="Output CSV File:", **self.label_style)
        self.output_file_label.pack(pady=5)
        self.output_file_entry = tk.Entry(root, width=110, **self.entry_style)
        self.output_file_entry.pack(pady=5)
        self.browse_output_button = tk.Button(root, text="Browse", command=self.browse_output_file, **self.button_style)
        self.browse_output_button.pack(pady=5)
        self.output_file_status = tk.Label(root, text="", **self.label_style)
        self.output_file_status.pack(pady=5)

        # Analyze Button
        self.analyze_button = tk.Button(root, text="Analyze Data", command=self.analyze_data, **self.button_style)
        self.analyze_button.pack(pady=20)

        # Status Label
        self.status_label = tk.Label(root, text="Status: Waiting for input...", **self.label_style)
        self.status_label.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, **self.button_style)
        self.exit_button.pack(pady=20)

    def browse_input_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.input_file_entry.delete(0, tk.END)
            self.input_file_entry.insert(0, file_path)
            self.input_file_status.config(text=f"Selected: {file_path}")

    def browse_output_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.output_file_entry.delete(0, tk.END)
            self.output_file_entry.insert(0, file_path)
            self.output_file_status.config(text=f"Selected: {file_path}")

    def analyze_data(self):
        input_file = self.input_file_entry.get()
        output_file = self.output_file_entry.get()

        if not input_file or not output_file:
            messagebox.showerror("Error", "Please specify both input and output files.")
            return

        try:
            self.status_label.config(text="Status: Analyzing data...")
            self.root.update()  # Refresh the status label immediately
            analyzer = CarDataAnalyzer(input_file, output_file)
            analyzer.load_data()
            analyzer.analyze_data()  # Default analysis
            self.status_label.config(text="Status: Data analysis complete. Results saved.")
            messagebox.showinfo("Success", "Data analysis complete. Results saved.")
        except Exception as e:
            self.status_label.config(text=f"Status: Error occurred - {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CarDataAnalyzerUI(root)
    root.mainloop()
