import random # Import random for potential use in patterns (though not heavily used in current ones)


# --- Helper Functions ---
MOD_26 = 26 # Constant for modulo 26, used for wrapping around the alphabet (A-Z)
ASCII_A_UPPER = ord('A') # ASCII value of 'A' (65), used as a base for character-to-index conversion
VOWELS = "AEIOU" # String of uppercase vowels
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73] # List of prime numbers, more than enough for 5-letter words


def is_vowel(char: str) -> bool: # Function to check if a character is a vowel
    return char.upper() in VOWELS # Convert char to uppercase and check if it's in the VOWELS string


def is_consonant(char: str) -> bool: # Function to check if a character is a consonant
    return char.isalpha() and not is_vowel(char) # Check if it's an alphabet character AND not a vowel


def shift_char(char: str, shift: int) -> str: # Function to shift a character by a given amount (Caesar cipher style)
    if 'A' <= char <= 'Z': # Check if the character is an uppercase letter
        # Convert char to 0-25 index, add shift, apply modulo 26, handle negative results, convert back to ASCII char
        return chr(((ord(char) - ASCII_A_UPPER + shift) % MOD_26 + MOD_26) % MOD_26 + ASCII_A_UPPER)
    return char # Return non-alphabetic characters unchanged


def reflect_char(char: str) -> str: # Function to reflect a character across the alphabet (A->Z, B->Y, etc.)
    """Reflect a character across the alphabet (A→Z, B→Y, ..., Z→A)."""
    if 'A' <= char <= 'Z': # Check if the character is an uppercase letter
        original_index = ord(char) - ASCII_A_UPPER # Get the 0-25 index of the character
        transformed_index = MOD_26 - 1 - original_index # Calculate the reflected index (e.g., A=0 -> 25=Z, Z=25 -> 0=A)
        return chr(ASCII_A_UPPER + transformed_index) # Convert the new index back to a character
    return char # Return non-alphabetic characters unchanged




# 1. Alternating Shift (+2, -2)
def alternating_shift_2_minus_2(word: str) -> str: # Pattern: shifts letters at alternating positions by +2 and -2
    transformed = list(word) # Convert the word to a list of characters for mutability
    shifts = [2, -2, 2, -2, 2] # Define the shift values for each of the 5 positions
    for i in range(len(word)): # Iterate through each character by its index
        transformed[i] = shift_char(word[i], shifts[i]) # Apply the specific shift to the character at current index
    return "".join(transformed) # Join the list of characters back into a string


# 2. Vowel/Consonant Opposite Shift
def vowel_consonant_opposite_shift(word: str) -> str: # Pattern: shifts vowels forward, consonants backward
    transformed = [] # Initialize an empty list to build the transformed word
    for char in word: # Iterate through each character in the word
        if is_vowel(char): # If the character is a vowel
            transformed.append(shift_char(char, 3)) # Shift vowels forward by 3
        elif is_consonant(char): # If the character is a consonant
            transformed.append(shift_char(char, -3)) # Shift consonants backward by 3
        else: # If it's neither (e.g., space, number), append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters back into a string


# 3. Position Doubling Shift
def position_doubling_shift(word: str) -> str: # Pattern: shifts each letter by double its 1-based position
    transformed = [] # Initialize an empty list
    shifts = [2, 4, 6, 8, 10] # Define shifts: (1*2), (2*2), (3*2), (4*2), (5*2)
    for i in range(len(word)): # Iterate through each character by its index
        transformed.append(shift_char(word[i], shifts[i])) # Apply the position-doubled shift
    return "".join(transformed) # Join the list of characters


# 4. Odd/Even Position Shift
def odd_even_position_shift(word: str) -> str: # Pattern: shifts letters at odd positions by +1, even by +3
    transformed = [] # Initialize an empty list
    shifts = [1, 3, 1, 3, 1] # Define shifts: +1 for 1st, 3rd, 5th; +3 for 2nd, 4th (1-based positions)
    for i in range(len(word)): # Iterate through each character by its index
        transformed.append(shift_char(word[i], shifts[i])) # Apply the specific shift
    return "".join(transformed) # Join the list of characters


# 5. Reverse Alphabet Substitution (A->Z, B->Y etc.)
def reverse_alphabet_substitution(word: str) -> str: # Pattern: substitutes each letter with its alphabetical opposite
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        if 'A' <= char <= 'Z': # Check if it's an uppercase letter
            # Calculate the reflected index: (25 - original_index)
            transformed.append(chr(ASCII_A_UPPER + (MOD_26 - 1 - (ord(char) - ASCII_A_UPPER))))
        else: # If not a letter, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


# 6. Position Plus Letter Shift
def position_plus_letter_shift(word: str) -> str: # Pattern: shifts each letter by its 1-based position plus a constant
    transformed = [] # Initialize an empty list
    shifts = [i + 2 for i in range(len(word))] # Define shifts: (0+2)=2, (1+2)=3, (2+2)=4, (3+2)=5, (4+2)=6 (1-based position + 1)
    for i in range(len(word)): # Iterate through each character by its index
        transformed.append(shift_char(word[i], shifts[i])) # Apply the calculated shift
    return "".join(transformed) # Join the list of characters


# 7. Vowel Boost Shift
def vowel_boost_shift(word: str) -> str: # Pattern: shifts vowels by a larger amount, consonants by a smaller amount
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        if is_vowel(char): # If it's a vowel
            transformed.append(shift_char(char, 5)) # Shift vowels forward by 5
        elif is_consonant(char): # If it's a consonant
            transformed.append(shift_char(char, 1)) # Shift consonants forward by 1
        else: # If not a letter, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


# 8. Cumulative Position Shift
def cumulative_position_shift(word: str) -> str: # Pattern: each letter's shift is the sum of its position and all previous positions
    transformed = [] # Initialize an empty list
    cumulative_sum = 0 # Initialize cumulative sum for shifts
    shifts = [0] * len(word) # Create a list to store calculated shifts for each position
    for i in range(len(word)): # Iterate through each position (0-based index)
        cumulative_sum += (i + 1) # Add the 1-based position to the cumulative sum
        shifts[i] = cumulative_sum # Store the cumulative sum as the shift for this position
    for i in range(len(word)): # Iterate again to apply the shifts
        transformed.append(shift_char(word[i], shifts[i])) # Apply the cumulative shift
    return "".join(transformed) # Join the list of characters


# 9. Prime Position Shift
def prime_position_shift(word: str) -> str: # Pattern: shifts each letter by the prime number corresponding to its position
    transformed = [] # Initialize an empty list
    if len(word) > len(PRIMES): # Check if there are enough prime numbers defined for the word length
        raise ValueError("Not enough prime numbers defined for word length.") # Raise an error if not
    for i in range(len(word)): # Iterate through each character by its index
        transformed.append(shift_char(word[i], PRIMES[i])) # Apply the prime number shift
    return "".join(transformed) # Join the list of characters


# 10. Alternating Sign Shift
def alternating_sign_shift(word: str) -> str: # Pattern: shifts letters by increasing amounts with alternating positive/negative signs
    transformed = [] # Initialize an empty list
    shifts = [1, -2, 3, -4, 5] # Define the specific alternating shifts
    for i in range(len(word)): # Iterate through each character by its index
        transformed.append(shift_char(word[i], shifts[i])) # Apply the alternating shift
    return "".join(transformed) # Join the list of characters




# 11. Letter Pair Swap
def letter_pair_swap(word: str) -> str: # Pattern: swaps letters in pairs (1st with 2nd, 3rd with 4th)
    if len(word) != 5: return word # Only apply if word is 5 characters long, otherwise return unchanged
    transformed = list(word) # Convert to list for swapping
    transformed[0], transformed[1] = transformed[1], transformed[0] # Swap first two characters
    transformed[2], transformed[3] = transformed[3], transformed[2] # Swap third and fourth characters
    return "".join(transformed) # Join the list of characters


# 12. Reverse Alphabet Cipher (Same as Rule 5)
def reverse_alphabet_cipher(word: str) -> str: # Pattern: alias for reverse_alphabet_substitution
    return reverse_alphabet_substitution(word) # Simply calls the existing substitution function


# 13. Vowel Swap (Positions 0 and 2)
def vowel_swap_0_2(word: str) -> str: # Pattern: swaps vowels at specific positions (0 and 2) if both are vowels
    if len(word) < 3: return word # Only apply if word has at least 3 characters
    transformed = list(word) # Convert to list for swapping
    char0 = transformed[0] # Get character at index 0
    char2 = transformed[2] # Get character at index 2
    if is_vowel(char0) and is_vowel(char2): # Check if both characters are vowels
        transformed[0], transformed[2] = transformed[2], transformed[0] # Swap them
    return "".join(transformed) # Join the list of characters


# 14. Double Index Mod 26
def double_index_mod_26(word: str) -> str: # Pattern: doubles each letter's alphabetical index, then wraps around alphabet
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        if 'A' <= char <= 'Z': # Check if it's an uppercase letter
            original_index = ord(char) - ASCII_A_UPPER # Get 0-25 index
            transformed_index = (original_index * 2) % MOD_26 # Double index and apply modulo 26
            transformed.append(chr(ASCII_A_UPPER + transformed_index)) # Convert back to character
        else: # If not a letter, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


# 15. Consonant Reverse Reflection (uses reflect_char helper)
def consonant_reverse_reflection_old(word: str) -> str: # Pattern: reflects consonants, leaves vowels unchanged (renamed to avoid clash)
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        if is_consonant(char): # If it's a consonant
            original_index = ord(char) - ASCII_A_UPPER # Get 0-25 index
            transformed_index = (MOD_26 - 1 - original_index) # Calculate reflected index
            transformed.append(chr(ASCII_A_UPPER + transformed_index)) # Convert back to character
        else: # If not a consonant, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


# 16. Position Multiply by 3
def position_multiply_by_3(word: str) -> str: # Pattern: multiplies letter's index by its 1-based position, then wraps around
    transformed = [] # Initialize an empty list
    for i in range(len(word)): # Iterate through each character by its index
        char = word[i] # Get the character
        if 'A' <= char <= 'Z': # Check if it's an uppercase letter
            original_index = ord(char) - ASCII_A_UPPER # Get 0-25 index
            position_factor = (i + 1) % MOD_26 # Get 1-based position, modulo 26 to keep factor within range
            transformed_index = (original_index * position_factor) % MOD_26 # Multiply index by position factor and apply modulo 26
            transformed.append(chr(ASCII_A_UPPER + transformed_index)) # Convert back to character
        else: # If not a letter, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


# 17. First-Last Swap
def first_last_swap(word: str) -> str: # Pattern: swaps the first and last characters of the word
    if len(word) < 2: return word # Only apply if word has at least 2 characters
    transformed = list(word) # Convert to list for swapping
    transformed[0], transformed[-1] = transformed[-1], transformed[0] # Swap first and last elements
    return "".join(transformed) # Join the list of characters


# 18. Vowel Forward 2, Consonant Backward 1
def vowel_forward_2_consonant_backward_1(word: str) -> str: # Pattern: shifts vowels forward by 2, consonants backward by 1
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        if is_vowel(char): # If it's a vowel
            transformed.append(shift_char(char, 2)) # Shift forward by 2
        elif is_consonant(char): # If it's a consonant
            transformed.append(shift_char(char, -1)) # Shift backward by 1
        else: # If not a letter, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


# 19. Middle Three Reverse
def middle_three_reverse(word: str) -> str: # Pattern: reverses the middle three characters of a 5-letter word
    if len(word) < 5: return word # Only apply if word has at least 5 characters
    transformed = list(word) # Convert to list for slicing and reversing
    middle_segment = transformed[1:4] # Extract the middle three characters (indices 1, 2, 3)
    middle_segment.reverse() # Reverse the extracted segment in place
    transformed[1:4] = middle_segment # Replace the original middle segment with the reversed one
    return "".join(transformed) # Join the list of characters


# 20. Constant Multiply by 2 (Same as Rule 14)
def constant_multiply_by_2(word: str) -> str: # Pattern: alias for double_index_mod_26
    return double_index_mod_26(word) # Simply calls the existing function






# 21. Alphabet Reflect by Position
def alphabet_reflect_by_position(word: str) -> str: # Pattern: reflects letters at odd positions (1-based)
    transformed = [] # Initialize an empty list
    for i, char in enumerate(word): # Iterate through characters with their 0-based index
        if (i + 1) % 2 != 0: # Check if the 1-based position is odd
            if 'A' <= char <= 'Z': # Check if it's an uppercase letter
                # Calculate reflected index
                transformed.append(chr(ASCII_A_UPPER + (MOD_26 - 1 - (ord(char) - ASCII_A_UPPER))))
            else: # If not a letter, append unchanged
                transformed.append(char)
        else: # If the 1-based position is even, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


# 22. Consonant Double, Vowel Single Shift
def consonant_double_vowel_single_shift(word: str) -> str: # Pattern: consonants shift by 2, vowels by 1
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        if is_consonant(char): # If it's a consonant
            transformed.append(shift_char(char, 2)) # Shift by 2
        elif is_vowel(char): # If it's a vowel
            transformed.append(shift_char(char, 1)) # Shift by 1
        else: # If not a letter, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


# 23. Fibonacci Shift
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21] # Precompute some Fibonacci numbers
def fibonacci_shift(word: str) -> str: # Pattern: shifts each letter by the Fibonacci number corresponding to its position
    transformed = [] # Initialize an empty list
    if len(word) > len(FIBONACCI): # Check if there are enough Fibonacci numbers for the word length
        raise ValueError("Not enough Fibonacci numbers defined for word length.") # Raise an error if not
    for i in range(len(word)): # Iterate through each character by its index
        transformed.append(shift_char(word[i], FIBONACCI[i])) # Apply the Fibonacci shift
    return "".join(transformed) # Join the list of characters


# 24. Character Order Reverse
def character_order_reverse(word: str) -> str: # Pattern: sorts the letters in reverse alphabetical order
    return "".join(sorted(list(word), reverse=True)) # Convert to list, sort in reverse, join back to string


# 25. Palindrome Check (Question doesn't change if palindrome, else reverse)
def palindrome_or_reverse(word: str) -> str: # Pattern: if word is a palindrome, it remains unchanged; otherwise, it's reversed
    if word == word[::-1]: # Check if the word is a palindrome (reads same forwards and backwards)
        return word # If it's a palindrome, return the original word
    else: # Otherwise
        return word[::-1] # Return the reversed word


# 26. Vowel Position Swap
def vowel_position_swap(word: str) -> str: # Pattern: swaps the first and last vowels in the word
    transformed = list(word) # Convert to list for mutability
    vowel_indices = [i for i, char in enumerate(word) if is_vowel(char)] # Find all indices of vowels


    if len(vowel_indices) >= 2: # If there are at least two vowels
        first_vowel_idx = vowel_indices[0] # Get the index of the first vowel
        last_vowel_idx = vowel_indices[-1] # Get the index of the last vowel
        # Swap the characters at these two indices
        transformed[first_vowel_idx], transformed[last_vowel_idx] = \
            transformed[last_vowel_idx], transformed[first_vowel_idx]
    return "".join(transformed) # Join the list of characters


# 27. Consonant Count Shift
def consonant_count_shift(word: str) -> str: # Pattern: shifts all letters by the total count of consonants in the word
    consonant_count = sum(1 for char in word if is_consonant(char)) # Count consonants in the word
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        transformed.append(shift_char(char, consonant_count)) # Apply the shift based on consonant count
    return "".join(transformed) # Join the list of characters


# 28. Even Position Reflection (uses reflect_char helper)
def even_position_reflection_old(word: str) -> str: # Pattern: reflects letters at even positions (1-based), leaves odd unchanged (renamed)
    transformed = [] # Initialize an empty list
    for i, char in enumerate(word): # Iterate through characters with their 0-based index
        if (i + 1) % 2 == 0: # Check if the 1-based position is even
            if 'A' <= char <= 'Z': # Check if it's an uppercase letter
                # Calculate reflected index
                transformed.append(chr(ASCII_A_UPPER + (MOD_26 - 1 - (ord(char) - ASCII_A_UPPER))))
            else: # If not a letter, append unchanged
                transformed.append(char)
        else: # If the 1-based position is odd, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


# 29. Ascending Shift by Letter Index
def ascending_shift_by_letter_index(word: str) -> str: # Pattern: shifts each letter by its own alphabetical index + 1
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        if 'A' <= char <= 'Z': # Check if it's an uppercase letter
            original_index = ord(char) - ASCII_A_UPPER # Get 0-25 index (A=0, B=1...)
            shift_value = original_index + 1 # Shift value is (index + 1) (A shifts by 1, B shifts by 2...)
            transformed.append(shift_char(char, shift_value)) # Apply the calculated shift
        else: # If not a letter, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


# 30. Last Letter Shift
def last_letter_shift(word: str) -> str: # Pattern: shifts all letters in the word by the alphabetical index of the last letter
    if not word: return "" # If the word is empty, return empty string
    last_char = word[-1] # Get the last character of the word
    if 'A' <= last_char <= 'Z': # Check if the last character is an uppercase letter
        shift_value = ord(last_char) - ASCII_A_UPPER # Get its 0-25 index as the shift value
    else: # If the last character is not an alphabetic letter
        shift_value = 0 # No shift applied
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character in the word
        transformed.append(shift_char(char, shift_value)) # Apply the same shift value to all characters
    return "".join(transformed) # Join the list of characters







def consonant_reverse_reflection(word: str) -> str: # Pattern: reflects consonants, leaves vowels unchanged (new version)
    """Reflect consonants using reflect_char; vowels unchanged."""
    if len(word) != 5: return word # Only apply if word is 5 characters long
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        if is_consonant(char): # If it's a consonant
            transformed.append(reflect_char(char)) # Apply the reflection using the helper function
        else: # If not a consonant, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


def alphabet_reflect_by_position_new(word: str) -> str: # Pattern: reflects letters at odd positions (1-based), leaves evens unchanged (new version)
    """Reflect letters in odd positions (1, 3, 5) using reflect_char; even positions unchanged."""
    if len(word) != 5: return word # Only apply if word is 5 characters long
    transformed = [] # Initialize an empty list
    for i, char in enumerate(word): # Iterate through characters with their 0-based index
        if (i + 1) % 2 != 0:  # Check if the 1-based position is odd
            transformed.append(reflect_char(char)) # Apply reflection
        else: # If even position, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


def even_position_reflection_new(word: str) -> str: # Pattern: reflects letters at even positions (1-based), leaves odds unchanged (new version)
    """Reflect letters in even positions (2, 4) using reflect_char; odd positions unchanged."""
    if len(word) != 5: return word # Only apply if word is 5 characters long
    transformed = [] # Initialize an empty list
    for i, char in enumerate(word): # Iterate through characters with their 0-based index
        if (i + 1) % 2 == 0:  # Check if the 1-based position is even
            transformed.append(reflect_char(char)) # Apply reflection
        else: # If odd position, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


def all_vowel_reflection(word: str) -> str: # Pattern: reflects all vowels, leaves consonants unchanged
    """Reflect all vowels (e.g., A=1→Z=26); consonants unchanged."""
    if len(word) != 5: return word # Only apply if word is 5 characters long
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        if is_vowel(char): # If it's a vowel
            transformed.append(reflect_char(char)) # Apply reflection
        else: # If not a vowel, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


def index_square_mod_26(word: str) -> str: # Pattern: squares each letter's alphabetical index, then wraps around alphabet
    """Square each letter’s index, take mod 26, map to a letter."""
    if len(word) != 5: return word # Only apply if word is 5 characters long
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        if 'A' <= char <= 'Z': # Check if it's an uppercase letter
            original_index = ord(char) - ASCII_A_UPPER # Get 0-25 index
            transformed_index = (original_index * original_index) % MOD_26 # Square the index and apply modulo 26
            transformed.append(chr(ASCII_A_UPPER + transformed_index)) # Convert back to character
        else: # If not a letter, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


def position_index_product(word: str) -> str: # Pattern: multiplies each letter's index by its 1-based position, then wraps around
    """Multiply each letter’s index by its 1-based position, take mod 26."""
    if len(word) != 5: return word # Only apply if word is 5 characters long
    transformed = [] # Initialize an empty list
    for i, char in enumerate(word): # Iterate through characters with their 0-based index
        if 'A' <= char <= 'Z': # Check if it's an uppercase letter
            original_index = ord(char) - ASCII_A_UPPER # Get 0-25 index
            transformed_index = (original_index * (i + 1)) % MOD_26 # Multiply index by (1-based position) and apply modulo 26
            transformed.append(chr(ASCII_A_UPPER + transformed_index)) # Convert back to character
        else: # If not a letter, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters


def letter_index_double_mod_10(word: str) -> str: # Pattern: doubles each letter's index, takes modulo 10, maps to A-J (0-9)
    """Double each letter’s index, take mod 10, map to A=0, ..., J=9."""
    if len(word) != 5: return word # Only apply if word is 5 characters long
    transformed = [] # Initialize an empty list
    print(f"\n--- Debugging letter_index_double_mod_10 for '{word}' ---") # Debug print statement
    for i, char in enumerate(word): # Iterate through characters with their 0-based index
        if 'A' <= char <= 'Z': # Check if it's an uppercase letter
            original_index = ord(char) - ASCII_A_UPPER # Get 0-25 index
            transformed_index = (original_index * 2) % 10 # Double index and apply modulo 10 (result will be 0-9)
            transformed_char = chr(ASCII_A_UPPER + transformed_index) # Convert new index (0-9) back to A-J
            print(f"Char: {char} (OrigIdx: {original_index}) -> Doubled: {original_index*2} -> Mod 10: {transformed_index} -> Transformed Char: {transformed_char}") # Detailed debug print
            transformed.append(transformed_char) # Append the transformed character
        else: # If not a letter, append unchanged
            transformed.append(char)
    result = "".join(transformed) # Join the list of characters
    print(f"Final transformed word: {result}") # Debug print for final word
    print("-------------------------------------------------------") # Debug separator
    return result # Return the transformed word


def consonant_index_triple_mod_26(word: str) -> str: # Pattern: triples consonants' indices, wraps around; vowels unchanged
    """Triple consonants’ indices, take mod 26; vowels unchanged."""
    if len(word) != 5: return word # Only apply if word is 5 characters long
    transformed = [] # Initialize an empty list
    for char in word: # Iterate through each character
        if is_consonant(char): # If it's a consonant
            original_index = ord(char) - ASCII_A_UPPER # Get 0-25 index
            transformed_index = (original_index * 3) % MOD_26 # Triple the index and apply modulo 26
            transformed.append(chr(ASCII_A_UPPER + transformed_index)) # Convert back to character
        else: # If not a consonant, append unchanged
            transformed.append(char)
    return "".join(transformed) # Join the list of characters




# --- List of ALL Pattern Functions ---
ALL_PATTERNS = [ # This list holds references to all the pattern functions
    alternating_shift_2_minus_2, # Function reference
    vowel_consonant_opposite_shift, # Function reference
    position_doubling_shift, # Function reference
    odd_even_position_shift, # Function reference
    reverse_alphabet_substitution, # Function reference
    position_plus_letter_shift, # Function reference
    vowel_boost_shift, # Function reference
    cumulative_position_shift, # Function reference
    prime_position_shift, # Function reference
    alternating_sign_shift, # Function reference


    letter_pair_swap, # Function reference
    reverse_alphabet_cipher, # Function reference (alias)
    vowel_swap_0_2, # Function reference
    double_index_mod_26, # Function reference
    consonant_reverse_reflection_old, # Function reference (older version, renamed)
    position_multiply_by_3, # Function reference
    first_last_swap, # Function reference
    vowel_forward_2_consonant_backward_1, # Function reference
    middle_three_reverse, # Function reference
    constant_multiply_by_2, # Function reference (alias)


    alphabet_reflect_by_position, # Function reference (older version, might clash with new one)
    consonant_double_vowel_single_shift, # Function reference
    fibonacci_shift, # Function reference
    character_order_reverse, # Function reference
    palindrome_or_reverse, # Function reference
    vowel_position_swap, # Function reference
    consonant_count_shift, # Function reference
    even_position_reflection_old, # Function reference (older version, renamed)
    ascending_shift_by_letter_index, # Function reference
    last_letter_shift, # Function reference


    consonant_reverse_reflection, # Function reference (newer version, intended to replace old one)
    alphabet_reflect_by_position_new, # Function reference (newer version)
    even_position_reflection_new, # Function reference (newer version)
    all_vowel_reflection, # Function reference
    index_square_mod_26, # Function reference
    position_index_product, # Function reference
    letter_index_double_mod_10, # Function reference
    consonant_index_triple_mod_26, # Function reference
]


# --- Example Usage (for testing the backend directly) ---
if __name__ == "__main__": # This block runs only when patterns.py is executed directly
    print("\n--- Testing All Patterns with Sample Words ---") # Informative print statement
    sample_words = ["APPLE", "BRAIN", "CRANE", "DRIVE", "ELITE", "FABLE", "GUISE", "HOUSE", "KINGS", "PLANT", "THINK", "TRAIN", "EARTH", "MAGIC"] # List of sample words for testing


    for word in sample_words: # Iterate through each sample word
        print(f"\nOriginal Word: {word}") # Print the original word
        for pattern_func in ALL_PATTERNS: # Iterate through each pattern function in the ALL_PATTERNS list
            try: # Use a try-except block to catch potential errors during pattern application
                transformed_word = pattern_func(word) # Apply the current pattern function to the word
                print(f"   {pattern_func.__name__}: {transformed_word}") # Print the pattern name and the transformed word
            except Exception as e: # Catch any exception that occurs
                print(f"   Error with {pattern_func.__name__}: {e}") # Print an error message if a pattern fails



