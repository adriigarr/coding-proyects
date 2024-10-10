import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import bubblesort

# Function to visualize sorting
def visualize_sorting(algorithm, arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, align='edge')

    ax.set_title("Bubble Sort Visualization")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))

    # Update function for animation
    def update(arr):
        for bar, val in zip(bars, arr):
            bar.set_height(val)

    ani = FuncAnimation(fig, update, frames=algorithm(arr), repeat=False, blit=False)
    plt.show()

# Test the visualization
if __name__ == "__main__":
    # Generate a random array of integers
    np.random.seed(0)
    array = np.random.randint(1, 100, size=20)
    visualize_sorting(bubblesort.bubble_sort, array)
