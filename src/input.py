def validate_temperature_input(temperature):
    """ Validate that the temperature is one of the allowed values: 'cold', 'room', 'warm' """
    return temperature in ['cold', 'room', 'warm']

def validate_chemical_indices(chemical_indices, num_chemicals):
    """ Validate the input indices for incompatibility. Ensure they are valid indices and non-repeating. """
    if not chemical_indices:
        return True
    
    for idx in chemical_indices:
        if not (1 <= idx <= num_chemicals):
            return False 
    return len(chemical_indices) == len(set(chemical_indices)) 

def get_input_data():
    while True:
        try:
            num_chemicals = int(input("Enter the number of chemicals: "))
            if num_chemicals <= 0:
                print("The number of chemicals must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the number of chemicals.")
    
    chemicals = {}
    chemical_names = []
    
    for i in range(num_chemicals):
        while True:
            name = input(f"Enter the name of chemical {i+1}: ").strip()
            if not name:
                print("Chemical name cannot be empty. Please try again.")
            elif name in chemical_names:
                print(f"The name '{name}' has already been used. Please enter a different name.")
            else:
                chemical_names.append(name)
                break
    
    for i in range(num_chemicals):
        print(f"\nChemical {chemical_names[i]} (Index {i+1}):")
        
        while True:
            incompatible_str = input(f"Enter the indices of incompatible chemicals (comma-separated, e.g. '1,2'): ")
            if incompatible_str:
                try:
                    incompatible_chemicals = list(map(int, incompatible_str.split(',')))
                    if not validate_chemical_indices(incompatible_chemicals, num_chemicals):
                        print(f"Invalid chemical indices entered. Please ensure indices are within range [1, {num_chemicals}] and unique.")
                        continue
                    break
                except ValueError:
                    print("Please enter valid indices (integers) separated by commas.")
            else:
                incompatible_chemicals = []
                break
        
        while True:
            storage_temperature = input("Enter the required storage temperature (cold/room/warm): ").lower()
            if validate_temperature_input(storage_temperature):
                break
            else:
                print("Invalid temperature. Please enter one of 'cold', 'room', or 'warm'.")
        
        chemicals[i] = {
            "name": chemical_names[i],
            "incompatible_with": incompatible_chemicals,
            "storage_requirements": {"temperature": storage_temperature}
        }
    
    return chemicals, chemical_names