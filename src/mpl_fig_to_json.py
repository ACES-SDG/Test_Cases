import matplotlib.pyplot as plt
import json

# Create a sample figure
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Sample Plot')
# plt.show()
# Save the figure as an image (e.g., PNG)
figure_filename = "sample_plot.png"
plt.savefig(figure_filename)

# Create a dictionary to store relevant information
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "figure_filename": figure_filename  # Store the filename of the saved figure
}

# Serialize the dictionary to JSON
json_data = json.dumps(data)

# Print or save the JSON data
print(json_data)

# Close the figure to free up resources
plt.close()
