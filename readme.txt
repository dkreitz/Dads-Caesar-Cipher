Use the Shell to execute the following commands:

(1) python caesarCipher.py

This will take the message in original_message.txt and encrypt it with a random key.
Then it will write the encrypted message into caesar_message.txt.

(2) python bruteHacker.py

This will use a brute force method of stepping through each key.
It will stop when it detects enough English words in the decrypted message.

(3) python freqHacker.py

This will use frequency analysis to guess the key based on the most common letter ('e') used in the English dictionary.
Again, it will stop when it detects enough English words in the decrypted message.

Both the bruteHacker and freqHacker use a timer to determine how long it took to decrypt the caesar cipher message.