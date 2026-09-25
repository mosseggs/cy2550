1.1)
PBKDF2 = Password-Based Key Derivation Function 2
Why it's necessary: Its one of many kinds of hashing functions, but its USEFUL because of it's broad compatibility, and it's resistance to brute force attacks thanks to the use of a salt and multiple iterations of its hash function.

1.2)
Why are the checksums different: The Salt applies a random number before encryption, making 2 of the same command produce different results.
What would go wrong if they were: Someone could brute force till they get the same command and now they know your password and also your true message.

1.3)
How many distinct blocks: 3
How many times does the most frequent one appear: 24
What did ECB Leak: The amount of repeating strings. 
How does this help attackers: This could be used to find common words such as "The" or "I"
Questions I would ask: How easily could they figure out how many times a phrase is repeated? 

2.2)
Why the SHA-256 hash does not protect your colleague: They don't know what was changed, they only know what the new data is?
What changes with HMAC: HMAC can tell when a file is different from the intended file, since the expected and recieved hash are different. 
What the attacker can and cannot do in each situation: 
SHA-256: They can Alter the file, but they cant make it have the same output.
HMAC: They can't alter the file without being caught, but if they have the key, they get free reign

3.3)
What does this check prove: You have access to the email
What does it not prove: You own the email

Describe a procedure for checking that the key really belongs to your classmate in a way that would defeat an attacker who controls the network between you. Explain why your procedure works: Have the classmate show you in person. It defeats the attacker by going through real life connections.

4.2)
What is contained in each packet?
pubkey enc packet: 4095 bits???
symkey enc packet: seskey 256 bits? + a salt?
encrypted data packet: "length 76" and MDC2, a cryptographic hashing method, according to wikipedia.
Why does GPG use this approach instead of encrypting the entire message with RSA: More protection is better, and more often than not they cover the weaknesses of having RSA alone.
What is this construction called: Hybrid Encryption

4.3)
Which key is used for signing: public
Which key is used for verifying: private
Which key is used for encryption: public
Which key is used for decryption: private
What is one security property provided by signing that encryption does not include: Authenticity

5)
Explain in two sentences why the much smaller Ed25519 key is not necessarily the weaker key: While RSA is based on multiplication, Ed is based on group theory and hence has much more complexity stuffed in a smaller package.This is also because it achieves similar results to RSA with a shorter keys and faster computations in terms of security level.
