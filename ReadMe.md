## Information Security I: From Cryptography to Buffer Overflows
October: [CS50 Intro to CyberSecurity](https://cs50.harvard.edu/cybersecurity/2023/zoom/#lecture-2-securing-systems)   

The objective of taking this [course](https://www.edx.org/course/unlocking-information-security-i-from-cryptography-to-buffer-overflows) ($125/per class (with discount) for access to exercises/quizzes/tests) was to learn more about cryptographic primitives, hash functions, and a lower level cybersecurity exploits.    
 - Check https://haveibeenpwned.com/ and test if you've been compromised.
 - [Hiroki39 Github](https://github.com/Hiroki39/IsraelX-Unlocking-Information-Security) - for hackxercises   
 - [AmosYeah](https://github.com/AmosYeah/IsraelX-Unlocking-Information-Security-II--An-Internet-Perspective) - for hackxercises   

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

`domain name system` - DNS, hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network that convert between names like tau.ac.il to IP addresses like 132.66.11.1   
`local area network` or LAN, computer network that interconnects computers within a limited area such as a residence, school, laboratory, university campus or office building. Ethernet and Wi-Fi are the two most common technologies in use for local area networks.   
`internet protocol` - (IP) the principal communications protocol in the Internet protocol suite for relaying datagrams (message packets) across network boundaries. Its routing function enables internetworking, and essentially establishes the Internet.   
`End-to-End Encryption` - system of communication where only the communicating users can read the messages, prevents potential eavesdroppers – including telecom providers, Internet providers, and even the provider of the communication service from being able to access the cryptographic keys needed to decrypt the conversation.   
`firewall` - monitors and controls incoming and outgoing network traffic based on predetermined security rules.   
`packets` - formatted unit of data carried by a packet-switched network; consists of control information and user data, which is known as the payload.   
`headers` - in a data packet sent via the Internet, the data (payload) are preceded by header information such as sender's and recipient's IP addresses, the protocol governing the format of the payload and several other formats.   
`VPN` - (Virtual Private Network) -  provides a private pathway (tunnel) for data to travel, keeps data secret (encryption), and hides location: 
 - Phase 1 - Establishing the Tunnel: Two VPN endpoints authenticate each other
 - Phase 2 - Data Transfer    

The 7 Layers Model (OSI (Open Systems Interconnection)): A P S T N D P
* All People Seem To Need Data Processing   
- Layer 1 - the `physical layer` 
 - Functionality: in charge of converting bits into signals and vice versa.
 - Implementation: The physical layer is always implemented in hardware.
- Layer 2 - the `data link layer` also called the `medium access control (MAC)` layer.
  - Functionality: Layer 2 is in charge of a `local area network (LAN)` - it’s restricted to a geographical area like your home, a cafe hotspot, a hallway in a building - at most a whole building or campus. Layer 2 communication is unreliable: messages can get garbled in transit due to electronic or radio interference - in which case they get silently dropped.
  - Protocol: The most common layer 2 protocols are WiFi (wireless) and Ethernet (over wires).
  - Implementation: Layer 2 is implemented either as hardware or “firmware” - software burned into the network interface cards (NICs).
 - Layer 3 - the `network layer`
   - Functionality: Responsible for connecting millions of LANs into one giant wide-area network which is the Internet. It’s like the postal system, moving messages (called packets) from senders to receivers. And like the postal system, it’s also unreliable: packet delivery is done on a best-effort basis: if there is congestion en-route (an Internet traffic jam), packets get dropped. Protocol: the Internet the network layer uses the Internet Protocol (IP).Implementation:  IP is usually implemented in software as part of the operating system of the connected devices, and also in the infrastructure devices called routers that are the Internet’s postal workers.
- Layer 4 - the `transport layer`
  - Functionality: Layer 4’s main job is to create reliable message channels through the unreliable layers below it. It does this like registered mail: the sender side assigns sequence numbers to packets, and the receiver side has to acknowledge each packet it gets. If the sender doesn’t receive an expected ”ack” fast enough, it retransmits the packet, under the assumption that it was dropped.
Note that a connection at layer 4 is bi-directional: both sides are simultaneously senders and receivers. Each assigns sequence numbers to the packets that it sends, and acknowledges the packets the other side sends. Protocol: In the Internet the transport layer most commonly uses the Transmission Control Protocol (TCP). There is also a more basic transport protocol in the Internet called UDP, which is used by applications that do not require all of TCP’s functionality. Implementation: Like IP, both TCP and UDP are implemented in software as part of the operating system.
- Layer 5 (called “session”) 
- Layer 6 (“presentation”) 
- Layer 7 (“application”)
- But these definitions (5-7) didn’t catch on. The Internet designers stopped at layer 4, and lumped all the higher layer functions into one big undefined application layer.

`address-resolution protocol poisoning` - an attacker sends (spoofed) Address Resolution Protocol (ARP) messages onto a local area network with the aim to associate the attacker's MAC address with the IP address of another host, such as the default gateway, causing traffic meant for that IP address to be sent to the attacker instead.   
`DNS poisoning` - type of attack that exploits vulnerabilities in the domain name system (DNS) to divert Internet traffic away from legitimate servers and towards fake ones. 
   
`IP address spoofing` - creation of Internet Protocol (IP) packets with a false source IP address, for the purpose of impersonating another computing system.   
`IP spoofing` - creation of Internet Protocol (IP) packets with a false source IP address, for the purpose of impersonating another computing system.   

`sniffer` - computer software or hardware that can intercept and log traffic passing over a digital network.   
`Man in the Middle attack` - MiTM, attacker secretly relays and alters communications between two parties who believe they are directly communicating with each other.   

---   
## Advanced Cryptography

`Diffie Hellman Key Exchange` - method of securely exchanging cryptographic keys over a public channel.   
`Rivest–Shamir–Adleman` - RSA, One of the first public-key cryptosystems, widely used for secure data transmission.   

`asymmetric encryption` - form of encryption where keys come in pairs. What one key encrypts, only the other can decrypt; asymmetric encryption because the communicating parties, Alice and Bob, have asymmetric roles: one side can only encrypt, while only the other side can decrypt.

---   
## Web Vulnerabilities and Defenses
 
`traffic sniffing` - https://www.wireshark.org/   
[Scapy](https://scapy.net/) - powerful python package for packet manipulation    
`Ping of death` - outdated blaster worm   
`smurf attack` -    

`Mimikatz` - [exploit](https://en.wikipedia.org/wiki/Mimikatz) on Microsoft Windows that extracts passwords stored in memory and software that performs that exploit   
`Air gap` - [air gap, air wall, or disconnected network](https://en.wikipedia.org/wiki/Air_gap_(networking)) - a network security measure employed on one or more computers to ensure that a secure computer network is physically isolated from unsecured networks, such as the public Internet or an unsecured local area network   

---   
## Computer Viruses and How to Beat Them

`trojan Horse` - Any malware which misleads users of its true intent. The term is derived from the Ancient Greek story of the deceptive Trojan Horse that led to the fall of the city of Troy.   
`virus` - type of computer program that, when executed, replicates itself by modifying other computer programs and inserting its own code into them.   
`worm` - standalone malware computer program that replicates itself in order to spread to other computers.    

`backdoor malware` - malware that negates normal authentication procedures to access a system. As a result, remote access is granted to resources within an application, such as databases and file servers, giving perpetrators the ability to remotely issue system commands and update malware. Core War: A 1984 programming game created by D. G. Jones and A. K. Dewdney in which two or more battle programs (called "warriors") compete for control of a virtual computer. These battle programs are written in an abstract assembly language called Redcode.

`creeper` - experimental computer program written by Bob Thomas at BBN in 1971. Its original iteration was designed to move between DEC PDP-10 mainframe computers running the TENEX operating system using the ARPANET, with a later version by Ray Tomlinson designed to copy itself between computers rather than simply move.

`metamorphic code` - code that when run outputs a logically equivalent version of its own code under some interpretation.

`Non-Resident Malware` - variant of computer related malicious software that exists exclusively as a computer memory-based artifact, e.g. in RAM. It does not write any part of its activity to the computer's hard drive.
`Resident Malware` - variant of computer related malicious software that hides and stores itself on the computer's hard drive.

`polymorphic code` - code that uses a polymorphic engine to mutate while keeping the original algorithm intact. That is, the code changes itself each time it runs, but the function of the code (its semantics) will not change at all.
Quine: A computer program which takes no input and produces a copy of its own source code as its only output.
Reaper: The first anti-virus software. It was created by Ray Tomlinson to move across the ARPANET and delete the self-replicating Creeper worm.

`resource theft` - theft of processing power.

`rootkit` - collection of computer software, typically malicious, designed to enable access to a computer or an area of its software that is not otherwise allowed (for example, to an unauthorized user) and often masks its existence or the existence of other software.

`Self-Replicating Automata (Universal Constructor)` - abstract machine which, when run, would replicate itself. In his design, the machine consists of three parts: a 'blueprint' for itself, a mechanism that can read any blueprint and construct the machine (sans blueprint) specified by that blueprint, and a 'copy machine' that can make copies of any blueprint.

`static signatures` - signatures that looks at static characteristics of the malware, such as strings, code snippets or their hashes.

`steganography` - method of hiding secret data, by embedding it into an audio, video, image or text file.

`Morris Worm` - one of the first computer worms distributed via the Internet, and the first to gain significant mainstream media attention. It also resulted in the first felony conviction in the US under the 1986 Computer Fraud and Abuse Act.   

`Advanced Research Projects Agency Network` ARPANET, early packet-switching network and the first network to implement the TCP/IP protocol suite.

---   
## ETC

[Stuxnet](https://en.m.wikipedia.org/wiki/Stuxnet) 
 - [Protective Relay](https://en.wikipedia.org/wiki/Protective_relay)   
 - [DARPA](https://en.wikipedia.org/wiki/DARPA) experiment on [plum island](https://www.wired.com/story/black-start-power-grid-darpa-plum-island/)
   
[Havex](https://en.m.wikipedia.org/wiki/Havex)   
[Killnet](https://en.m.wikipedia.org/wiki/Killnet)   
[Blackenergy](https://en.m.wikipedia.org/wiki/BlackEnergy)   
[Industroyer](https://en.wikipedia.org/wiki/Industroyer)   
[NotPetya](https://en.wikipedia.org/wiki/Petya_and_NotPetya) - The Untold Story of NotPetya, the Most Devastating Cyberattack in History [Link](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/)   
 - [Fancy Bear](https://en.wikipedia.org/wiki/Fancy_Bear)
 - [Guccifer 2.0](https://en.wikipedia.org/wiki/Guccifer_2.0) 

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

`turbulence` - request goes through servers; turmoil - guard - passive collections, copies data coming through (if flagged as suspicious goes to turbine)    
`turbine` - active collection, tampering (programs of quantum suite)   

`flipper zero` - a portable Tamagotchi-like multi-functional device developed for interaction with access control systems.[1] The device is able to read, copy, and emulate RFID and NFC tags, radio remotes, iButton, and digital access keys, along with a GPIO interface; [wiki](https://en.wikipedia.org/wiki/Flipper_Zero)   

Andy Greenberg - [Sandworm](https://www.amazon.com/Sandworm-Cyberwar-Kremlins-Dangerous-Hackers/dp/0385544405) and [Tracers in the Dark](https://www.amazon.com/Tracers-Dark-Global-Crime-Cryptocurrency/dp/0385548095)       
Nicole Perlroth NYT - [Twitter](https://twitter.com/NicolePerlroth).  

[Keybase](https://keybase.io/) - for end to end encryption 
