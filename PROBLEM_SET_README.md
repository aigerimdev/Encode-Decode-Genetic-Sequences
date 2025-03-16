# Problem Set - Debugging Dahlia’s Project

## Overview 

Dahlia is a geneticist and programmer who is stuck while debugging her program. She has been tasked with analyzing genetic sequences which are provided as strings of characters. She needs to determine if each sequence is DNA or RNA, and compress the sequence for storage. 

`main.py` holds the driving code to run or test the application, while `part_one.py` and `part_two.py` contain the functions for working with the genetic sequences as strings. `sequence_tests.py` holds tests for both Part 1 and Part 2 of the activity.

Dahlia's code can either be ran in test mode or production mode. To run the project, execute `python3 main.py` in the console and you will see a prompt to enter `t` to test the project, or `r` to run the code in production mode.

## Categorizing & Compressing Sequences

### DNA vs RNA

Dahlia knows that:
- Every genetic sequence (both DNA & RNA) can contain the letters G, A, and C. 
- Only DNA can contain the character T  
- Only RNA can contain the character U.

Dahlia wants to use these facts to sort the sequences by placing all sequences that contain T in a DNA list, and all sequences that contain U in a RNA list. 

Thinking about edge cases, Dahlia also plans for a third list: “uncategorized". Here she’ll place sequences that need further study because they can't be easily categorized: 
- valid sequences without any T or U characters
- invalid sequences that contain both T and U characters. 

### Compressing a string of characters

For storage, Dahlia compresses the sequences by replacing repeating characters in the string with a single character followed by a count. 

For example, the string `GGGGAAACCCCC` becomes `G4A3C5` when compressed with this strategy. Take a look at the `sequence_tests.py` file for more examples.

## Debugging Part 1

### Part 1 Explanation

When Dahlia runs her project, it crashes and she isn’t sure where. To complete this Problem Set:
- Identify and fix the bugs in Dahlia’s code.
- Only use manual debugging strategies such as adding print statements, using a debugger, or searching for the error online. Do not use tools like ChatGPT for this exercise.
- As you go along, answer the questions about Part 1 on the Debugging Cont. Learn lesson's Problem Set Page.

### Potential WorkfLow

If you’d like some direction getting started, feel free to use the flow below:
1. Run the code in both test and production mode to see the errors Dahlia’s receiving.
2. Rubber duck by yourself or with another person to understand what is happening.
3. If helpful, do a web search for the error to see what kind of information surfaces. 
4. Use your current manual debugging tools to identify where in the code the issue is happening.
5. Once you understand what is happening and where, identify what piece or pieces of our code could be the cause.
6. Determine a fix, and apply it.
7. Test to make sure our fix worked as expected.

## Debugging Part 2

### Before Starting Part 2

We need to change the code in a couple places to ensure all of the Part 2 code is accessible.
Make the following changes before trying to debug Part 2:
1. In `main.py` at the top of the file:
   - comment out the part 1 import statement `from part_one import driver`
   - uncomment the part 2 import line `# from part_two import driver`
2. In `sequence_tests.py` uncomment line 17 `part_two_tests()`

### Part 2 Explanation

Dahlia realizes that the compressed sequences still have the information she needs to categorize them as DNA or RNA. Since it takes less time to iterate through a compressed string than the full sequence, Dahlia can save a little time by categorizing the sequences after they are compressed. 

She refactors her code in a new file `part_two.py`, but finds a new issue when categorizing the strings. 
1. Debug the `part_two.py` file using the techniques you practiced in Part 1 of this activity. 
2. As you move through Part 2, answer the questions about Part 2 on the Debugging Cont. Learn lesson's Problem Set Page. 