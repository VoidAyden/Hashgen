import hashlib

def generate_hash(input_string, algorithm='sha256'):
    # Create a hash object using the specified algorithm
    hash_object = hashlib.new(algorithm)
    
    # Update the hash object with the input string encoded to bytes
    hash_object.update(input_string.encode())
    
    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()

# Example usage:
input_data = input("Enter the string to hash: ")
algorithm_choice = input("Enter the hash algorithm (default: sha256): ") or 'sha256'

hashed_output = generate_hash(input_data, algorithm_choice)
print(f"The generated hash is: {hashed_output}")
