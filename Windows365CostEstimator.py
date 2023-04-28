import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_cost(*args):
    num_users = int(users_slider.get())
    cost_per_user = int(cost_slider.get())
    hardware_cost_per_user_annually = int(hardware_cost_slider.get())
    
    cloud_annual_cost_per_user = cost_per_user * 12
    total_cloud_cost = num_users * cloud_annual_cost_per_user
    total_hardware_cost = num_users * hardware_cost_per_user_annually
    potential_savings = total_hardware_cost - total_cloud_cost
    
    users_label.config(text=f'Number of Users: {num_users}')
    cost_label.config(text=f'Cost per User per Month (Cloud): ${cost_per_user:.2f}')
    hardware_cost_label.config(text=f'Hardware Cost per User Annually: ${hardware_cost_per_user_annually:.2f}')
    total_cost_label.config(text=f'Total Annual Cloud Cost: ${total_cloud_cost:.2f}')
    total_hardware_cost_label.config(text=f'Total Annual Hardware Cost: ${total_hardware_cost:.2f}')
    potential_savings_label.config(text=f'Potential Annual Savings: ${potential_savings:.2f}')

    update_chart(total_cloud_cost, total_hardware_cost)

def update_hardware_cost():
    try:
        laptop_cost = float(laptop_cost_entry.get())
        hardware_cost_slider.set(laptop_cost / 3)
        update_cost()
    except ValueError:
        pass

def update_chart(cloud_cost, hardware_cost):
    ax.clear()
    ax.bar(['Cloud Cost', 'Hardware Cost'], [cloud_cost, hardware_cost], color=['blue', 'orange'])
    ax.set_ylim(0, max(cloud_cost, hardware_cost) * 1.2)
    for index, value in enumerate([cloud_cost, hardware_cost]):
        ax.text(index, value + 0.05 * max(cloud_cost, hardware_cost), f'${value:.2f}', ha='center')
    chart_canvas.draw()

root = tk.Tk()
root.title('Windows 365 Cost Estimator')

# Create sliders, labels, and input box
users_slider = ttk.Scale(root, from_=1, to=150, command=update_cost, orient='horizontal')
users_label = ttk.Label(root, text='Number of Users: 1')

cost_slider = ttk.Scale(root, from_=28, to=132, command=update_cost, orient='horizontal')
cost_label = ttk.Label(root, text='Cost per User per Month (Cloud): $28.00')

hardware_cost_slider = ttk.Scale(root, from_=300, to=2000, command=update_cost, orient='horizontal')
hardware_cost_label = ttk.Label(root, text='Hardware Cost per User Annually: $300.00')

laptop_cost_label = ttk.Label(root, text='Average Laptop Cost:')
laptop_cost_entry = ttk.Entry(root, width=10)
update_hardware_cost_button = ttk.Button(root, text='Update Hardware Cost', command=update_hardware_cost)

total_cost_label = ttk.Label(root, text='Total Annual Cloud Cost: $0.00')
total_hardware_cost_label = ttk.Label(root, text='Total Annual Hardware Cost: $0.00')
potential_savings_label = ttk.Label(root, text='Potential Annual Savings: $0.00')

# Refactor the layout using grid
users_slider.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
users_label.grid(row=0, column=1, padx=10, pady=5)
cost_slider.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
cost_label.grid(row=1, column=1, padx=10, pady=5)
hardware_cost_slider.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
hardware_cost_label.grid(row=2, column=1, padx=10, pady=5)
laptop_cost_label.grid(row=3, column=0, padx=10, pady=5)
laptop_cost_entry.grid(row=3, column=1, padx=10, pady=5)
update_hardware_cost_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
total_cost_label.grid(row=5, column=0, padx=10, pady=10)
total_hardware_cost_label.grid(row=5, column=1, padx=10, pady=10)
potential_savings_label.grid(row=6, column=0, padx=10, pady=10)

# Create the bar chart
figure, ax = plt.subplots(figsize=(5, 4))
chart_canvas = FigureCanvasTkAgg(figure, root)
chart_canvas.get_tk_widget().grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Update the labels when the sliders are moved
users_slider.config(command=update_cost)
cost_slider.config(command=update_cost)
hardware_cost_slider.config(command=update_cost)


update_chart(0, 0)  # Initialize the chart with zero values
root.mainloop()