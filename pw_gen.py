import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                     use_numbers=True, use_special=True, min_of_each=1):
    """
    Generate a secure password with customizable options.
    
    Args:
        length (int): Length of the password
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_numbers (bool): Include numbers
        use_special (bool): Include special characters
        min_of_each (int): Minimum number of each selected character type
        
    Returns:
        str: Generated password
    """
    # Validate inputs
    char_types_count = sum([use_uppercase, use_lowercase, use_numbers, use_special])
    if min_of_each * char_types_count > length:
        raise ValueError("Password length too short to satisfy minimum requirements")
    
    if not any([use_uppercase, use_lowercase, use_numbers, use_special]):
        raise ValueError("At least one character type must be selected")
    
    # Initialize character pools
    chars = ''
    required_chars = []
    
    if use_uppercase:
        chars += string.ascii_uppercase
        required_chars.extend(random.sample(string.ascii_uppercase, min_of_each))
        
    if use_lowercase:
        chars += string.ascii_lowercase
        required_chars.extend(random.sample(string.ascii_lowercase, min_of_each))
        
    if use_numbers:
        chars += string.digits
        required_chars.extend(random.sample(string.digits, min_of_each))
        
    if use_special:
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        chars += special_chars
        required_chars.extend(random.sample(special_chars, min_of_each))
    
    # Generate remaining characters
    remaining_length = length - len(required_chars)
    password_chars = required_chars + random.choices(chars, k=remaining_length)
    
    # Shuffle the password
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

# Example usage
if __name__ == "__main__":
    try:
        # Generate passwords with different requirements
        default_password = generate_password()
        print(f"Default password (12 chars, all types): {default_password}")
        
        long_password = generate_password(length=16, min_of_each=2)
        print(f"Longer password (16 chars, min 2 of each): {long_password}")
        
        letters_only = generate_password(length=10, use_numbers=False, 
                                      use_special=False, min_of_each=2)
        print(f"Letters-only password (10 chars): {letters_only}")
        
    except ValueError as e:
        print(f"Error: {e}")