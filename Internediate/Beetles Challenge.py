import json
import math
import sys

def simulate_beetle_population(data):
    """
    Simulates the beetle population dynamics over time based on rainfall events and carrying capacity.

    Args:
        data (dict): JSON input data with carrying capacity, rainfall series, initial phase, and populations.

    Returns:
        list: State of the system at each time step as a list of dictionaries.
    """
    # Extract input values
    carrying_capacity = data['capacity']
    rainfall_series = data['rainfall']
    initial_phase = data['state']['phase']
    populations = data['state']['populations']
    growth_rates = {'Red': 0.17, 'Green': 0.26, 'Blue': 0.11}
    
    # Initialize the output array with the initial state
    result = [{"phase": initial_phase, "populations": populations.copy()}]
    phase = initial_phase

    for rain in rainfall_series:
        # Calculate total population
        total_population = sum(populations.values())
        
        # Check if the carrying capacity is exceeded
        if total_population > carrying_capacity:
            phase = "bust"
        
        # Determine the next populations based on phase
        new_populations = {}
        for species, population in populations.items():
            growth_rate = growth_rates[species]
            if phase == "boom":
                new_population = math.ceil(population * (1 + growth_rate))
            else:  # phase == "bust"
                new_population = math.floor(population * (1 - growth_rate))
            new_populations[species] = new_population
        
        # Update populations
        populations = new_populations
        
        # Check if rainfall switches phase to boom
        if rain:
            phase = "boom"
        
        # Append the current state to the results
        result.append({"phase": phase, "populations": populations.copy()})
    
    return result

def main(input_file='input.json', output_file='output.json'):
    """
    Runs the beetle population simulation and saves the result to a file.

    Args:
        input_file (str): Path to the JSON input file.
        output_file (str): Path to save the JSON output file.
    """
    try:
        # Load input data
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        # Run the simulation
        result = simulate_beetle_population(data)
        
        # Save the result to the output file
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=4)
        
        print(f"Simulation completed. Results saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except json.JSONDecodeError:
        print("Error: Input file is not valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Command-line instructions:
#   python beetle_simulation.py input.json output.json
if __name__ == "__main__":
    # Use sys.argv for command line arguments
    if len(sys.argv) >= 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = 'input.json'
        output_file = 'output.json'
    
    main(input_file, output_file)
