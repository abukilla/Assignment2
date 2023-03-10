from secrets import choice   # Used to produce reliably random hex values
from string import printable # A list of printable characters to validate against


def generate_pad(length:int) -> str:
    """Generates a pad of random printable ASCII characters
    
    Parameters
    ----------
    length : int
        The length of the pad you want to generate
    
    Examples
    --------
    Creating a 5 character long pad
    ```
    pad = generate_pad(5) # Pad == uBV,;
    ```
    Returns
    -------
    str
        The generated one time page
    """
    pad = ""
    for index in range(length):
        # Choose a random printable character
        pad_letter =  choice(printable)
        pad += (pad_letter)

    save(pad, "pad.txt")
    return pad

def encrypt(text:str, pad:str) -> str:
    """Encrypts the input text and returns the ciphertext
    
    Parameters
    ----------
    text : str
        The plaintext to generate a ciphertext
    pad : str
        The one-time pad to use for generating a chiphertext
    
    Examples
    --------
    Encrypting 'Hello'
    ```
    pad = generate_pad(5) # Pad == uBV,;
    ciphertext = encrypt('Hello', pad) # ciphertext == "=':@T"
    ```
    Returns
    -------
    str
        The ciphertext
    
    Raises
    ------
    ValueError
        Raised when one of the characters is not printable ASCII
    """

    # String variable that will contain all the shifted values
    ciphertext = ""

    for text_character, pad_character in zip(text, pad):
        if text_character not in printable:
            raise ValueError(f"Text value: {text_character} provided is not printable ascii")

        # Completed the XOR of the characters ordinance (integer representation)
        xored_value = ord(text_character) ^ ord(pad_character)

        # Takes resulting integer from XOR operation and converts it to a character
        ciphertext_character = chr(xored_value)

        # Add the generated character to the ciphertext
        ciphertext += (ciphertext_character)

    save(ciphertext, "ciphertext.txt")

    return ciphertext

def decrypt(pad:str, ciphertext:str) -> str:
    """Decrypts the ciphertext using the provided pad
    
    Parameters
    ----------
    pad : str
        The pad used to encrypt the one time pad
    ciphertext : str
        The ciphertext to decrypt
    
    Examples
    --------
    Encrypting & Decrypting 'Hello'
    ```
    pad = generate_pad(5) # Pad == uBV,;
    ciphertext = encrypt('Hello', pad) # ciphertext == "=':@T"
    plaintext = decrypt(pad, ciphertext) # plaintext == "Hello"
    ```
    Returns
    -------
    str
        The decrypted plaintext
    """
    plaintext = ""

    for pad_character, ciphertext_number in zip(pad, ciphertext):
        xored_value = ord(pad_character) ^ ord(ciphertext_number)
        plaintext += chr(xored_value)

    save(plaintext, "plaintext.txt")

    return plaintext


def save(text:str, path:str):
    """Takes in text and saves it to the provided path
    
    Parameters
    ----------
    text : str
        The text to save to a file
    path : str
        The path to save it to
    Examples
    --------
    Saving 'Hello' to 'hello.txt'
    ```
    save('hello', 'hello.txt')
    ```
    """
    try:
        with open(path, "w+") as output_file:
            output_file.write(text)
    except:
        print(f"Unable to save file {path}")


if __name__ == "__main__":
    # The text to encrypt
    text = '''Do not go gentle into that good night.'''

    # Generate a pad the same length as the text
    pad = generate_pad(len(text))
    print(f"The pad is: {pad}")

    # Generate a ciphertext from the pad and plaintext
    ciphertext = encrypt(text, pad)
    print(f"\nThe ciphertext is: {ciphertext}")

    # Decrypt and return result
    plaintext = decrypt(pad, ciphertext)
    print(f"\nThe decrypted plaintext is: {plaintext}")