def validate_chemical_indices(chemical_indices, chemical_amt): # chemical indices validation
    if not chemical_indices: # no incompatible chemicals
        return True
    
    for idx in chemical_indices:
        if not (1 <= idx <= chemical_amt): # index out of range
            return False 
        
    return (len(chemical_indices) == len(set(chemical_indices))) 

def validate_temperature(temp): # temperature validation
    return (temp in ["cold", "room"])

def input_chemical_info():
    while True: # the number of chemicals input
        try:
            chemical_amt = int(input("Enter the number of chemicals: "))
            if chemical_amt <= 0:
                print("The number of chemicals must be positive.")
                continue
            break

        except ValueError:
            print("The number of chemicals must be an integer.")
    
    chemicals = {}
    chemical_names = []
    for i in range(chemical_amt): # chemical name input and validation
        while True:
            name = input(f"Enter the name of chemical {i+1}: ").strip()
            
            if not name:
                print("Chemical name cannot be empty. Please try again.")
            
            elif name in chemical_names:
                print(f"The'{name}' has already been added. Please enter a different chemical.")
            
            else:
                chemical_names.append(name)
                break
    
    for i in range(chemical_amt): 
        print(f"\nChemical {i+1} ({chemical_names[i]})")

        while True: # chemical incompatibility input and validation
            incompatible_str = input(f"Enter the indices of incompatible chemicals: ")
            
            if incompatible_str:
                try:
                    incompatible_chemicals = list(map(int, incompatible_str.split(',')))
                    if not validate_chemical_indices(incompatible_chemicals, chemical_amt):
                        print(f"Invalid chemical indices. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Indicies must be separated by commas. Please try again.")
            
            else:
                incompatible_chemicals = []
                break
        
        while True: # chemical storage temperature input and validation
            storage_temperature = input("Enter the required storage temperature (cold/room): ").lower()
            if validate_temperature(storage_temperature):
                break
            else:
                print("Invalid temperature. Please try again.")
        
        chemicals[i] = {
            "name": chemical_names[i],
            "incompatible_with": incompatible_chemicals,
            "temperature": storage_temperature
        }
    
    return chemicals, chemical_names