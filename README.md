# Sprint Challenge: Hash Tables and Blockchain
This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains.

demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Description

This sprint challenge is divided up into three parts:  Hash tables coding, blockchain coding, and a short interview covering parts of hash tables and blockchain.

# # # # # # # # # # # # # # # # # # # Interview Questions  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, 
O(1)
* add or remove from the front
O(n)  - we have to shift every single item to a new index in the array one by one
* and add or remove from the back?
O(1)
* What is the worse case scenario if you try to extend the storage size of a dynamic array?
O(n)
We try to double it, there's not enough contiguous free space, so we'd have to find a empty space in memory large enough, then move the old array data one by one into the new, larger array

# Explain how blockchain networks remain in consensus:
* What does a node do if it gets a message from another in the network with a new block?
Sent to everyone on the network, each node verifies the new block to make sure it hasn't been tampered with. If it's approved, it's added to their blockchain (this is called concensus)
* Why can't someone cheat by changing a transaction from an earlier block to give themselves coins?
The falsified block will have a different hash than before, therefore, in the subsequent blocks, the fingerprint of previous-block would not match. Someone would have to change every block onward in the distributed ledger. To add complications, We use a proof-of-work mechanism to slow down the creation of blocks (for example, bitcoin takes 10 minutes for 1 block) and with the use of distribution among a peer-to-peer network, a nefarious person would have to get approval from/take control of over 50% of the p2p network

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced, built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.  

## Minimum Viable Product

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables)

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain)


### Rubric

| *OBJECTIVE*                                                                                                     | *TASK*             | *1 - DOES NOT MEET EXPECTATIONS*                                                                                            | *2 - MEETS EXPECTATIONS*                                                                                                       | *3 - EXCEEDS EXPECTATIONS                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| implement and describe how high-level array functions work down to the memory level                             | Interview Question | If you were evaluating this candidate for a position with your company, your would object to them being added to your team. | If you were evaluating this candidate for a position with your company, you would be pleased to have this person on your team. | If you were evaluating this candidate for a position with your company, you would go out of your way to make sure this person is hired for your team. |
| implement and utilize basic hash table + handle collisions and resizing in a hash table                         | Hash Problem 1 & 2 | Tests do not pass on one or both problems, or solutions do not use hash tables.                                             | Tests pass on both problems.  Solution utilizes a hash table.                                                                  | Tests pass on on both problems with solutions utilizing hash tables, linear runtime complexity, no flake8 complaints.                                 |
| diagram and code a simple blockchain, utilizing a cryptographic hash                                            | Interview Question | If you were evaluating this candidate for a position with your company, your would object to them being added to your team. | If you were evaluating this candidate for a position with your company, you would be pleased to have this person on your team. | If you were evaluating this candidate for a position with your company, you would go out of your way to make sure this person is hired for your team. |
| utilize a Proof of Work process to protect a blockchain from attack                                             | Blockchain Problem | The student is unable to mine a coin before the end of lunch.                                                               | The student was able to mine a coin before the end of lunch.                                                                   | The student presented a unique solution that was able to mine more than 100 coins before the end of lunch.                                            |
| build a protocol to allow nodes in a blockchain network to communicate to share blocks and determine consensus. | Interview Question | If you were evaluating this candidate for a position with your company, your would object to them being added to your team. | If you were evaluating this candidate for a position with your company, you would be pleased to have this person on your team. | If you were evaluating this candidate for a position with your company, you would go out of your way to make sure this person is hired for your team. |
