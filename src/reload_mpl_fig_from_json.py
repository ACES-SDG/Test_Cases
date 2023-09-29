import matplotlib.pyplot as plt
import json

# Load your JSON data (replace this with your actual JSON data)
json_data = '{"name": "John", "age": 30, "city": "New York", "figure_filename": "sample_plot.png"}'

# Parse the JSON data into a Python dictionary
data = json.loads(json_data)

# Read the filename of the saved figure from the dictionary
figure_filename = data.get("figure_filename")

# Load and display the figure
if figure_filename:
    loaded_figure = plt.imread(figure_filename)  # Load the image
    
    print( loaded_figure , type(loaded_figure))
    plt.imshow(loaded_figure)  # Display the image
    plt.axis("off")  # Turn off axis labels and ticks (optional)
    plt.show()
    
else:
    print("Figure filename not found in JSON data.")
