import tkinter as tk
from tkinter import filedialog, messagebox
from car_data_analyzer.main import CarDataAnalyzer


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


class CarDataAnalyzerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Data Analyzer")
        self.root.configure(bg='#f0f0f0')  # Background color

        # Styles
        self.label_style = {'bg': '#f0f0f0', 'fg': '#333', 'font': ('Arial', 12)}
        self.entry_style = {'bg': '#fff', 'fg': '#333', 'font': ('Arial', 12)}
        self.button_style = {'bg': '#4CAF50', 'fg': '#fff', 'font': ('Arial', 12), 'activebackground': '#45a049'}
        self.button_style_average = {'bg': '#6495ED', 'fg': '#fff', 'font': ('Arial', 12), 'activebackground': '#45a049'}
        self.button_style_exit = {'bg': '#DE3163', 'fg': '#fff', 'font': ('Arial', 12), 'activebackground': '#45a049'}
        self.button_style_filter_sort = {'bg': '#808080', 'fg': '#fff', 'font': ('Arial', 12), 'activebackground': '#45a049'}

        # Input JSON File
        self.input_file_label = tk.Label(root, text="Input JSON File:", **self.label_style)
        self.input_file_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.input_file_entry = PlaceholderEntry(root, width=80, placeholder="Enter JSON file path", **self.entry_style)
        self.input_file_entry.grid(row=0, column=1, padx=5, pady=5)
        self.browse_input_button = tk.Button(root, text="Browse", command=self.browse_input_file, **self.button_style)
        self.browse_input_button.grid(row=0, column=2, padx=5, pady=5)
        self.input_file_status = tk.Label(root, text="", **self.label_style)
        self.input_file_status.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Output CSV File
        self.output_file_label = tk.Label(root, text="Output CSV File:", **self.label_style)
        self.output_file_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.output_file_entry = PlaceholderEntry(root, width=80, placeholder="Enter CSV file path", **self.entry_style)
        self.output_file_entry.grid(row=2, column=1, padx=5, pady=5)
        self.browse_output_button = tk.Button(root, text="Browse", command=self.browse_output_file, **self.button_style)
        self.browse_output_button.grid(row=2, column=2, padx=5, pady=5)
        self.output_file_status = tk.Label(root, text="", **self.label_style)
        self.output_file_status.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        # Analyze Button
        self.analyze_button = tk.Button(root, text="Analyze Data", command=self.analyze_data, **self.button_style)
        self.analyze_button.grid(row=4, column=1, pady=20)

        # Show Averages Button
        self.show_averages_button = tk.Button(root, text="Show Averages", command=self.show_averages, state=tk.DISABLED,
                                              **self.button_style_average)
        self.show_averages_button.grid(row=5, column=1, pady=5)

        # Show Top/Bottom Cars Button
        self.show_top_bottom_button = tk.Button(root, text="Show Top/Bottom Cars", command=self.show_top_bottom, state=tk.DISABLED,
                                                **self.button_style_average)
        self.show_top_bottom_button.grid(row=6, column=1, pady=5)

        # Status Label
        self.status_label = tk.Label(root, text="Status: Waiting for input...", **self.label_style)
        self.status_label.grid(row=7, column=1, pady=10)

        # Filter by Year
        self.filter_year_label = tk.Label(root, text="Filter by Year Range:", **self.label_style)
        self.filter_year_label.grid(row=8, column=0, padx=5, pady=5, sticky='e')
        self.start_year_entry = PlaceholderEntry(root, width=10, placeholder="Start Year", **self.entry_style)
        self.start_year_entry.grid(row=8, column=1, padx=5, pady=5, sticky='w')
        self.end_year_entry = PlaceholderEntry(root, width=10, placeholder="End Year", **self.entry_style)
        self.end_year_entry.grid(row=8, column=1, padx=5, pady=5, sticky='e')
        self.filter_year_button = tk.Button(root, text="Filter", command=self.filter_by_year, state=tk.DISABLED, **self.button_style_filter_sort)
        self.filter_year_button.grid(row=8, column=2, padx=5, pady=5)

        # Sort by Column
        self.sort_label = tk.Label(root, text="Sort by Column:", **self.label_style)
        self.sort_label.grid(row=9, column=0, padx=5, pady=5, sticky='e')
        self.sort_column_entry = PlaceholderEntry(root, width=20, placeholder="Column name", **self.entry_style)
        self.sort_column_entry.grid(row=9, column=1, padx=5, pady=5)
        self.sort_ascending_var = tk.BooleanVar(value=True)
        self.sort_ascending_check = tk.Checkbutton(root, text="Ascending", variable=self.sort_ascending_var, **self.label_style)
        self.sort_ascending_check.grid(row=9, column=2, padx=5, pady=5)
        self.sort_button = tk.Button(root, text="Sort", command=self.sort_by_column, state=tk.DISABLED, **self.button_style_filter_sort)
        self.sort_button.grid(row=9, column=3, padx=5, pady=5)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, **self.button_style_exit)
        self.exit_button.grid(row=10, column=1, pady=20,sticky='e')

        self.analyzer = None

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
            self.analyzer = CarDataAnalyzer(input_file, output_file)
            self.analyzer.load_data()
            self.analyzer.analyze_data()
            self.status_label.config(text="Status: Data analysis complete. Results saved.")
            messagebox.showinfo("Success", "Data analysis complete. Results saved.")

            # Enable additional function buttons
            self.show_averages_button.config(state=tk.NORMAL)
            self.show_top_bottom_button.config(state=tk.NORMAL)
        except Exception as e:
            self.status_label.config(text=f"Status: Error occurred - {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        self.filter_year_button.config(state=tk.NORMAL)
        self.sort_button.config(state=tk.NORMAL)

    def show_averages(self):
        if not self.analyzer:
            messagebox.showerror("Error", "Please analyze data first.")
            return
        averages = self.analyzer.calculate_averages()
        averages_str = "\n".join([f"{col}: {avg:.2f}" for col, avg in averages.items()])
        messagebox.showinfo("Average Values", averages_str)

    def show_top_bottom(self):
        if not self.analyzer:
            messagebox.showerror("Error", "Please analyze data first.")
            return
        top_bottom = self.analyzer.get_top_bottom_cars('Horsepower')
        top_str = top_bottom['top'].to_string(index=False)
        bottom_str = top_bottom['bottom'].to_string(index=False)
        messagebox.showinfo("Top/Bottom Cars by Horsepower", f"Top 5:\n{top_str}\n\nBottom 5:\n{bottom_str}")

    def filter_by_year(self):
        if not self.analyzer:
            messagebox.showerror("Error", "Please analyze data first.")
            return
        try:
            start_year = int(self.start_year_entry.get())
            end_year = int(self.end_year_entry.get())
            filtered_data = self.analyzer.filter_by_year(start_year, end_year)
            if not filtered_data.empty:
                self.show_dataframe("Filtered Data", filtered_data)
            else:
                messagebox.showinfo("Info", "No data found for the specified year range.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid year values.")

    def sort_by_column(self):
        if not self.analyzer:
            messagebox.showerror("Error", "Please analyze data first.")
            return
        column = self.sort_column_entry.get()
        ascending = self.sort_ascending_var.get()
        sorted_data = self.analyzer.sort_by_column(column, ascending)
        if not sorted_data.empty:
            self.show_dataframe("Sorted Data", sorted_data)
        else:
            messagebox.showerror("Error", f"Unable to sort by column '{column}'.")

    def show_dataframe(self, title, df):
        top = tk.Toplevel(self.root)
        top.title(title)
        text = tk.Text(top, wrap=tk.NONE)
        text.pack(expand=True, fill=tk.BOTH)
        text.insert(tk.END, df.to_string())
        scrollbar = tk.Scrollbar(top, command=text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text.config(yscrollcommand=scrollbar.set)


if __name__ == "__main__":
    root = tk.Tk()
    app = CarDataAnalyzerUI(root)
    root.mainloop()
