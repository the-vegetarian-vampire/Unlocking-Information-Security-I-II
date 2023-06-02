## Information Security I: From Cryptography to Buffer Overflows
The objective of taking this course was to learn more cryptographic primitives and hash functions regarding security. Not wanting a full Cryptography course, I wanted a lower lever introduction to security and various exploits.    

Check out https://haveibeenpwned.com/ and test your own email address to see if your accounts have been compromised.     

Class [Link](https://www.edx.org/course/unlocking-information-security-i-from-cryptography-to-buffer-overflows)   
$125 (with discount) for access to exercises/quizzes/test.   

Pros:
 - excellent content/high-mid level overview
 - problem sets/"hackxercises"   
 
Cons
 - videos aren't very detailed (found more info searching on my own)
 - not on youtube (can't download/have to watch on the site)

---

## Vulnerabilities and Exploits
`vulnerability` - a flaw in a system's design, implementation or operation, that can be exploited to violate the system's security policy.    
 `exploit` - leverages a vulnerability to violate a system's security policy, usually with malicious intent. One of the most popular exploits is denial of service.     
`remote code execution` - an attacker gets to execute software, code, of her own, on the victim's machine.  

`Design vuln.` - flaw in the way a system is designed; most commonly, an unconsidered usage (logical vulnerability).   
`Implimentation vuln` - flaw in the way a system system is implemented; a programming mistake (technical vulnerability).   
`Operation vuln.` -  flaw in the way the users interact with the system (social engineering) the psychological manipulation of people   
`Integration vuln.` - components are insecurely combined.    

`privilege Escalation` - elevating permission from a regular user to an “admin” or “root”.   

`side-channel attack` - attack based on byproducts of the system, ie time it takes the system to run or the sounds emitted by the CPU.   

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

`replay attacks` pass-the-hash attacks.   
`pseudo-random generator (PRG)` -    

`evil maid attack`.  

[IMSI-catcher](https://en.wikipedia.org/wiki/IMSI-catcher) - a telephone eavesdropping device used for intercepting mobile phone traffic and tracking location data of mobile phone users   

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
## ETC
From Snowden’s book [Permanent Record](https://www.amazon.com/Permanent-Record-Edward-Snowden/dp/1250237238)   
- The 5 eyes: U.S., UK, Australia, Canada, New Zealand  
- 6 Protocols: 
  - sniff it-all (find data source)
  - know it all (find out what data was)
  - collect it all (capturing data) 
  - process it all (analyze data for usable intel)
  - exploit it all (using intel to further agency aim)
  - partner it all (share with Allies)


`Prism collection` - from servers of service providers   
`Upstream collection` - direct collection from internet infrastructure    

`Turbulence` - request goes through servers; turmoil - guard - passive collections, copies data coming through (if flagged as suspicious goes to turbine)    
`Turbine` - active collection, tampering (programs of quantum suite)    

Nicole Perlroth NYT - [Twitter](https://twitter.com/NicolePerlroth).  
