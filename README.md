# Lab-8
SY402 Lab 8

hash.py takes in 2 arguments, the root directory and output file.

sudo python3 hash.py [root directory] [output file]

The program creates a dictionary of each file recursively found starting at the root directory. 
The dictionary is of format path/file : [sha256 hash, date / time accessed]
The programn then checks if there is already an output file and writes the dictionary to the file if not.
If there is already an output file, the program analyzes the old dictionary and compares it to the new one.
