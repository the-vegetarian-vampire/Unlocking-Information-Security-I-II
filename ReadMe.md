## Information Security I: From Cryptography to Buffer Overflows
Check out https://haveibeenpwned.com/ and test your own email address to see if any of your accounts have been compromised.   

Class [Link](https://www.edx.org/course/unlocking-information-security-i-from-cryptography-to-buffer-overflows)    
Pros:
 - excellent content/high-mid level overview
 - good problem sets or 'hackxercises"

Cons
 - videos aren't very detailed (found more info searching on my own)
 - not on youtube (can't download/have to watch on the site)

---

## Vulnerabilities and Exploits
`vulnerability` a flaw in a system's design, implementation or operation, that can be exploited to violate the system's security policy.    
 `exploit` leverages a vulnerability to violate a system's security policy, usually with malicious intent. One of the most popular exploits is denial of service.    
`remote code execution` - an attacker gets to execute software, code, of her own, on the victim's machine.  

Design.  
Implimentation.  
Operation.  
Integration.  

Vault 7 - [wikileaks](https://en.wikipedia.org/wiki/Vault_7)    

`Speculative execution` - an optimization technique where a computer system performs some task that may not be needed. Work is done before it is known whether it is actually needed, so as to prevent a delay that would have to be incurred by doing the work after it is known that it is needed. If it turns out the work was not needed after all, most changes made by the work are reverted and the results are ignored. [Vox](https://www.youtube.com/watch?v=d1BRw32nMqg)    

Vulnerability in the cache.  

[Time-of-check to time-of-use](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use)   

---

## Cryptography
Symmetric Cipher.  
XOR Cipher.  
Stream cipher     
Block cipher  

---

## Hash Functions

`hash function` - function that takes an input (a large amount of data) and produces a fixed-size output (hash or digest) that represents the input in a way that is useful for a variety of purposes, such as verifying the integrity of the data or detecting duplicates.      

f(x) =(x \* 127) mod 13

---

## Authentication
`Two-factor authentication` (2FA) a security process in which a user provides two different authentication factors to verify their identity; factors can be something the user knows (such as a password or PIN), something the user has (such as a security token or mobile device), or something the user is (such as a biometric identifier like a fingerprint or facial recognition).   

`replay attacks`.  

Authentication schemes    
 - A: something you know: passwords
 - B: something you are: biometrics 
 - C: something you have: phone

According to David Mitnik's [Art of Invisibility](https://www.goodreads.com/book/show/30363785-the-art-of-invisibility) create non sequitur passwords:   
- MyFavoriteNumisOrange
- MyDogsNameIs24

---

## Buffer Overflows

---   
