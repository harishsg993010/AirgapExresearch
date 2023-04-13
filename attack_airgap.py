import time
import screen_brightness_control as sbc

# Define Morse code dictionary
morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--',
              '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' / '}

# Function to encode text into Morse code
def encode_morse(text):
    encoded_text = []
    for char in text:
        char = char.upper()
        if char in morse_code:
            encoded_text.append(morse_code[char])
    return ' '.join(encoded_text)

# Function to transmit Morse code using screen brightness variation
def transmit_morse(morse_text, delay=0.5, brightness_on=100, brightness_off=80):
    transmission_rate = 0  # Initialize transmission rate to 0
    for symbol in morse_text:
        if symbol == '.':
            # Increase screen brightness
            sbc.set_brightness(brightness_on)
            time.sleep(delay)
            # Decrease screen brightness
            sbc.set_brightness(brightness_off)
            transmission_rate += 1  # Increment transmission rate for dot
        elif symbol == '-':
            # Increase screen brightness
            sbc.set_brightness(brightness_on)
            time.sleep(3 * delay)
            # Decrease screen brightness
            sbc.set_brightness(brightness_off)
            transmission_rate += 1  # Increment transmission rate for dash
        else:
            # Pause between Morse code symbols
            time.sleep(2 * delay)

    return transmission_rate / (len(morse_text) * delay)  # Calculate transmission rate in words per minute   

# Example usage
text = "HELLO WORLD"
morse_text = encode_morse(text)
print("Morse code:", morse_text)
transmission_rate = transmit_morse(morse_text)
print("Transmission rate: {:.2f} words per minute".format(transmission_rate * 60))  # Convert to words per minute
