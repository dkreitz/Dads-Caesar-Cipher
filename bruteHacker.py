import time

import detectEnglish

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# read in the message from the input file:
with open('caesar_message.txt', 'r') as file:
    message = file.read()

# Start the timer
startTime = time.time()

# Loop through every possible key (brute force):
for key in range(len(SYMBOLS)):

    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''

    # The rest of the program is almost the same as the original program:

    # Loop through each symbol in `message`:
    for symbol in message:

        if symbol in SYMBOLS:

            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wrap-around:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))

    # Test if the decrypted message is in English:
    if detectEnglish.isEnglish(translated):
        # Stop the timer
        endTime = time.time()
        
        print('Message is in English!')
        print('Key #%s: %s' % (key, translated))
        print('Found English text after %.6f seconds.' % (endTime - startTime))
        break
