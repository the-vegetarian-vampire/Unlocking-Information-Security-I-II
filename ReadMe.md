## Information Security I: From Cryptography to Buffer Overflows
The objective of taking this course was to learn more about cryptographic primitives, hash functions, and a lower level introduction to cybersecurity and various exploits.    

- Check https://haveibeenpwned.com/ and test if you've been compromised.     
- Class [Link](https://www.edx.org/course/unlocking-information-security-i-from-cryptography-to-buffer-overflows) $125/per class (with discount) for access to exercises/quizzes/tests.      

Pros:
 - excellent content/mid level overview
 - problem sets/"hackxercises"   
 
Cons
 - video format not on youtube (can't download/have to watch on site)
 - quizzes and tests require exact syntax (missed a few, despite being technically correct)

---

## Vulnerabilities and Exploits
`vulnerability` - a flaw in a system's design, implementation or operation, that can be exploited to violate the system's security policy.    
`exploit` - leverages a vulnerability to violate a system's security policy, usually with malicious intent. One of the most popular exploits is denial of service.     
`remote code execution` - an attacker gets to execute software, code, of her own, on the victim's machine.  

#### Vulnerabilities
`Design` - flaw in the way a system is designed; most commonly, an unconsidered usage (logical vulnerability).   
`Implimentation` - flaw in the way a system system is implemented; a programming mistake (technical vulnerability).   
`Operation.` -  flaw in the way the users interact with the system (social engineering) the psychological manipulation of people   
`Integration` - components are insecurely combined.    

`privilege escalation` - elevating permission from a regular user to an “admin” or “root”.  

`speculative execution` - an optimization technique where a computer system performs some task that may not be needed. Work is done before it is known whether it is actually needed, so as to prevent a delay that would have to be incurred by doing the work after it is known that it is needed. If it turns out the work was not needed after all, most changes made by the work are reverted and the results are ignored. [Vox](https://www.youtube.com/watch?v=d1BRw32nMqg); Vulnerability in the cache.     

`side-channel attack` - attack based on byproducts of the system, ie time it takes the system to run or the sounds emitted by the CPU.  
`zero day attack` - no one knows about the attack; minute is discovered engineers have zero days to fix it     
`meltdown` - vulnerability on the hardware level, can read memory not authorized to access.      
`watering hole attack` - an attacker guesses or observes which websites an organization often uses and infects one or more of them with malware. Eventually, some member of the targeted group will become infected. [wiki](https://en.wikipedia.org/wiki/Watering_hole_attack)       
`machine address code[1]` - `medium access control[2]` - `message authentication code[3]` or (mac) muiltiple meanings depending on context - [wiki1](https://en.wikipedia.org/wiki/MAC_address) or [wiki2](https://en.wikipedia.org/wiki/Medium_access_control) or [wiki3](https://en.wikipedia.org/wiki/Message_authentication_code)     

Vault 7 - [wikileaks](https://en.wikipedia.org/wiki/Vault_7)    
[Time-of-check to time-of-use](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use)    

Cryptanalyis Github via [DominicBreuker](https://github.com/DominicBreuker/cryptanalysis)

---

## Cryptography

`plaintext` - unencrypted information pending input into cryptographic algorithms   
`ciphertext` - encrypted plaintext  
`initialization vector` - an initialization vector (IV) or starting variable is an input to a cryptographic primitive being used to provide the initial state. The IV is typically required to be random or pseudorandom, but sometimes an IV only needs to be unpredictable or unique. Randomization is crucial for some encryption schemes to achieve semantic security, a property whereby repeated usage of the scheme under the same key does not allow an attacker to infer relationships between (potentially similar) segments of the encrypted message.   
`Pseudo-Random Generator (PRG)` - deterministic procedure that maps a random seed to a longer pseudorandom string so no statistical test can distinguish between the output of the generator and the uniform distribution.   

`Symmetric Cipher` - use same cryptographic keys for encryption of plaintext and decryption of ciphertext.   
`XOR Cipher` - boolean operator on two variables that has the value of one if one but not both of the variables has a value of one.     
`Stream cipher` - a cryptographic key and algorithm are applied to each binary digit in a data stream, one bit at a time.  
  - susceptible to bit-flipping attacks
    
`Block cipher`  - a cryptographic key and algorithm are applied to a block of data as a group rather tha one bit at a time.  

[Kerckhoff’s principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle) - a cryptosystem should be secure, even if everything about the system, except the key, is public knowledge   
`One Time Pad` - encryption technique that cannot be cracked but requires a one-time pre-shared key the same size or longer than the message sent.

`PGP` - [Pretty Good Privacy](https://en.m.wikipedia.org/wiki/Pretty_Good_Privacy#Digital_signatures)_used for signing, encrypting, and decrypting texts, e-mails, files, directories, and whole disk partitions and to increase the security of e-mail communications. Phil Zimmermann developed PGP in 1991.   

---

## Hash Functions

`hash function` - function that takes an input (a large amount of data) and produces a fixed-size output (hash or digest) that represents the input in a way that is useful for a variety of purposes, such as verifying the integrity of the data or detecting duplicates.   

`salt` - or [salting](https://en.wikipedia.org/wiki/Salt_(cryptography)) random data that is used as an additional input to a one-way function that hashes data, a password or passphrase. Salts are used to safeguard passwords in storage   

f(x) =(x \* 127) mod 13

`message digest 5` – a popular hash function from 1991 (outdated/no longer secure)   

---

## Authentication
`Two-factor authentication` (2FA) a security process in which a user provides two different authentication factors to verify their identity; factors can be something the user knows (such as a password or PIN), something the user has (such as a security token or mobile device), or something the user is (such as a biometric identifier like a fingerprint or facial recognition).   

`replay attacks` - [pass-the-hash attacks](https://www.crowdstrike.com/cybersecurity-101/pass-the-hash/); an adversary steals a “hashed” user credential and uses it to create a new user session on the same network   
`dictionary attacks` - an attack using a restricted subset of a keyspace to defeat a cipher or authentication mechanism by trying to determine its decryption key or passphrase, sometimes trying thousands or millions of likely possibilities[1] often obtained from lists of past security breaches   
`evil maid attack` - an attacker with physical access alters it in some undetectable way so that they can later access the device, or the data on it [wiki](https://en.wikipedia.org/wiki/Evil_maid_attack)    

`insult rate` - percentage of times a valid user is rejected by the system      
`fraud rate` - percentage of times an invalid user is accepted by the system   

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

`stack overflow` - buffer overflow overwriting a function's return address.

`canary` - values that are placed between a buffer and control data on the stack to monitor buffer overflows.   
`data execution prevention` - DEP, prevents code on the stack; prevents memory from being executable and writable

`W^X princicple` - memory should be writeable or executable, never both.    

`ASLR` - [address space layout randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization) technique involved in preventing exploitation of memory corruption vulnerabilities. In order to prevent an attacker from reliably jumping to, for example, a particular exploited function in memory, ASLR randomly arranges the address space positions of key data areas of a process, including the base of the executable and the positions of the stack, heap and libraries.   

---   

## Unlocking Information Security II: An Internet Perspective
---   
## Network Vulnerabilities and Defenses 

The 7 Layers Model
- Layer 1 - the `physical layer` 
 - Functionality: in charge of converting bits into signals and vice versa.
 - Implementation: The physical layer is always implemented in hardware.
- Layer 2 - the `data link layer` also called the `medium access control (MAC)` layer.
  - Functionality: Layer 2 is in charge of a `local area network (LAN)` - it’s restricted to a geographical area like your home, a cafe hotspot, a hallway in a building - at most a whole building or campus. Layer 2 communication is unreliable: messages can get garbled in transit due to electronic or radio interference - in which case they get silently dropped.
  - Protocol: The most common layer 2 protocols are WiFi (wireless) and Ethernet (over wires). I
  - mplementation: Layer 2 is implemented either as hardware or “firmware” - software burned into the network interface cards (NICs).
 - Layer 3 - the `network layer`
   - Functionality: Responsible for connecting millions of LANs into one giant wide-area network which is the Internet. It’s like the postal system, moving messages (called packets) from senders to receivers. And like the postal system, it’s also unreliable: packet delivery is done on a best-effort basis: if there is congestion en-route (an Internet traffic jam), packets get dropped. Protocol: the Internet the network layer uses the Internet Protocol (IP).Implementation:  IP is usually implemented in software as part of the operating system of the connected devices, and also in the infrastructure devices called routers that are the Internet’s postal workers.
- Layer 4 - the `transport layer`
  - Functionality: Layer 4’s main job is to create reliable message channels through the unreliable layers below it. It does this like registered mail: the sender side assigns sequence numbers to packets, and the receiver side has to acknowledge each packet it gets. If the sender doesn’t receive an expected ”ack” fast enough, it retransmits the packet, under the assumption that it was dropped.
Note that a connection at layer 4 is bi-directional: both sides are simultaneously senders and receivers. Each assigns sequence numbers to the packets that it sends, and acknowledges the packets the other side sends. Protocol: In the Internet the transport layer most commonly uses the Transmission Control Protocol (TCP). There is also a more basic transport protocol in the Internet called UDP, which is used by applications that do not require all of TCP’s functionality. Implementation: Like IP, both TCP and UDP are implemented in software as part of the operating system.
- Layer 5 (called “session”) 
- layer 6 (“presentation”) 
- layer 7 (“application”) But these definitions didn’t catch on.
- The Internet designers stopped at layer 4, and lumped all the higher layer functions into one big undefined application layer.
 
---   
## Advanced Cryptography
---   
## Web Vulnerabilities and Defenses

`MiTM` Man in the Middle attack -    
`Traffic sniffing` - https://www.wireshark.org/   
`Scapy` - https://scapy.net/ - powerful python package for packet manipulation   
`sniffer` -    
`Ping of death` - outdated blaster worm   
`smurf attack` -    

`Mimikatz` - [exploit](https://en.wikipedia.org/wiki/Mimikatz) on Microsoft Windows that extracts passwords stored in memory and software that performs that exploit   
`Air gap` - [air gap, air wall, or disconnected network](https://en.wikipedia.org/wiki/Air_gap_(networking)) - a network security measure employed on one or more computers to ensure that a secure computer network is physically isolated from unsecured networks, such as the public Internet or an unsecured local area network   

---   
## Computer Viruses and How to Beat Them
---   
## ETC

[Stuxnet](https://en.m.wikipedia.org/wiki/Stuxnet)   
[Havex](https://en.m.wikipedia.org/wiki/Havex)   
[Killnet](https://en.m.wikipedia.org/wiki/Killnet)   
[Blackenergy](https://en.m.wikipedia.org/wiki/BlackEnergy)   
[Industroyer](https://en.wikipedia.org/wiki/Industroyer)   
NotPetya - The Untold Story of NotPetya, the Most Devastating Cyberattack in History [Link](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/)   

From Snowden’s book [Permanent Record](https://www.amazon.com/Permanent-Record-Edward-Snowden/dp/1250237238)   
- The 5 eyes: U.S., UK, Australia, Canada, New Zealand  
- 6 Protocols: 
  - sniff it-all (find data source)
  - know it all (find out what data was)
  - collect it all (capturing data) 
  - process it all (analyze data for usable intel)
  - exploit it all (using intel to further agency aim)
  - partner it all (share with Allies)

`SIGINT` - [SIGINT Activity Designator](https://en.wikipedia.org/wiki/SIGINT_Activity_Designator) - signals intelligence (SIGINT) line of collection activity associated with a signals collection station   
`HUMINT` - [human intelligence](https://en.wikipedia.org/wiki/Human_intelligence_(intelligence_gathering))   
`Prism collection` - from servers of service providers   
`Upstream collection` - direct collection from internet infrastructure    

`Turbulence` - request goes through servers; turmoil - guard - passive collections, copies data coming through (if flagged as suspicious goes to turbine)    
`Turbine` - active collection, tampering (programs of quantum suite)   

Flipper zero - a portable Tamagotchi-like multi-functional device developed for interaction with access control systems.[1] The device is able to read, copy, and emulate RFID and NFC tags, radio remotes, iButton, and digital access keys, along with a GPIO interface; [wiki](https://en.wikipedia.org/wiki/Flipper_Zero)   

Andy Greenberg - Sandworm and [Tracers in the Dark](https://www.amazon.com/Tracers-Dark-Global-Crime-Cryptocurrency/dp/0385548095)       
Nicole Perlroth NYT - [Twitter](https://twitter.com/NicolePerlroth).  
