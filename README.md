# Hadoop_Project_2
Big Data:High Performance Computing Project


In this project, I worked with input, output, Python and the MapReduce framework. The mappers and reducers to solve a few different problems, listed below.

##Background
The map function is stateless and this is especially important when dealing with Hadoop and distributed work. We can’t guarantee that any 1 mapper will read in all of the data. 
Nor can we guarantee that certain input will end up on the same machine for mapping. Rather, 1 mapper will likely read in a small portion of the data. 
The output that the mapper produces must only depend on the current input value.

## The File Naming Convention 
The task was to write a mapper file and a reducer file to solve each of the following problems. The files in this repo are named mapperX.py and reducerX.py where X is the problem number. 

For each problem, along with the mapper and reducer, I created a final script to combine the partial output files into one file. 

## Problem 1: Sorting
Assume you work for a large business and have access to all orders made in any given time period (download the orders.csv file from http://www.uwosh.edu/faculty_staff/krohne/ds730/orders.csv). The column headings are fairly self-explanatory. Your company wants you to find the big spenders for each month and country so they can market more heavily to them. Your goal is this: for each month/country combination, display the customerID of the top spender for that month/country combination. The amount spent in each row is determined by multiplying the Quantity by the UnitPrice. A few caveats:
The InvoiceDate is in Month/Day/Year format.
An InvoiceNo that starts with a C is a return. You must ignore these rows.
A row may not have a CustomerID. These rows must be ignored.
We were not looking for month/year/country combinations here. There are two years worth of data and I am only interested in the month and country.


This final output file should contain the following data:

Month,Country : CustomerID

It should be sorted by month first. If the months are the same, then sort them by country second. If there is a tie, you can print out either customer or you can print out all of them who tied.

## Problem 2: Palindrome-ness
Solve only one of the following two problems:
This is a very difficult problem. In many real world problems, the mapping and reducing part will be quite trivial but the computation to determine the intermediate values is quite difficult. This problem looks at a problem that is computationally difficult. For this problem, you will be grouping words together based on a strange characteristic. Palindromes are important in the field of computational biology. The characteristic we are interested in is called palindromedness (not a word). Palindromedness is defined as the minimum number of edits that must happen to a word in order to make it a palindrome. The palindrome that is created with the edits need not be an actual word. An edit can be any of the following:
Removing a letter in any spot.
Adding a letter in any spot.
Replacing a letter in any spot with any other letter.

We’ll define it as p(X) where X is some word. For example, p(“cat”) == 1. If you replace ‘c’ with ‘t’ the word becomes “tat” and that word is a palindrome. Another example, p(“that”) == 1. If you remove the ‘h’ the word becomes “tat” and that word is a palindrome. Another example, p(“tart”) == 1. If you add an ‘r’ after the first t, it becomes “trart” which is a palindrome. As another example, p(“tater”) = 2. If you remove the ‘r’ and remove the ‘e’ you have a palindrome. As a final example, p(“hello”) == 2. You can remove the ‘e’ to get “hllo” and then replace the ‘h’ with an ‘o’ to get “ollo.”
The type of edits to make a palindrome do not have to be the same. You can mix and match edits to get a palindrome. In general, p(someWord) == k if there are k edits of any type that turn someWord into a palindrome and no sequence of (k-1) edits can turn someWord into a palindrome. Your goal is this, calculate the palindromedness of every word that is passed in and group words in the output by their palindromedness value. For example, assume the input is:

hello this is a test

The output would be:

0 : a
1 : is, test
2 : hello, this

The words on the righthand side must be in alphabetical order. You can assume that the words will contain only letters. However, they may be upper or lowercase and that should not affect the palindromedness. For example, Tat is a palindrome even though ‘T’ is not identical to ‘t’ but they are the same letter. There will be no numbers or special symbols in the input. All words will be separated by whitespace (either a space, tab or newline). Your output should be what you see above. The palindromedness value on the left, followed by a colon and then followed by a list of words with that palindromedness value separated by a comma. If there are duplicate words in the input file, you should print out both words in the final output.

In my opinion, this is difficult but not as difficult as 2a. On many social media websites, it is common for the company to provide a list of suggested contacts for you to connect with. Many of these suggestions come from your own list of current contacts. The basic idea behind this concept being: I am connected with person A and person B but not person C. Person A and person B are both connected to person C. None of my contacts are connected to person D. It is more likely that I know person C than some other random person D who is connected to no one I know. In this problem, you will read in an input file that is formatted in the following manner:
	PersonA : PersonX PersonY PersonZ PersonQ
	PersonB : PersonF PersonY PersonX PersonG PersonM
	…
The person to the left of the colon will be the current person. All people to the right of the colon are the people that the current person is connected to. All people will be separated by a single space. In the example above, PersonA is connected to PersonX, Y, Z and Q. In all inputs, all people will be replaced with integer ids to keep things simple. The following is a sample input file:

	1 : 3 5 8 9 10 12
2 : 3 4 7 6 13
3 : 9 11 10 1 2 13
4 : 2 5 7 8 9
5 : 4 1 7 11 12
6 : 2 9 8 10
7 : 5 2 4 9 12
8 : 1 6 4 11
9 : 12 1 3 6 4 7
10 : 1 3 6 11
11 : 3 5 10 8
12 : 1 7 5 9
13 : 2 3


The ordering of people on the right hand side can be in any random order. Your goal is this: you must output potential contacts based on the following 2 criteria:
Someone who might be someone you know. For someone to be suggested here, the person must not currently be a connection of yours and that person must be a connection of 2 or 3 of your current connections. For example, consider person 2 in the above example. Person 2 is connected with 3, 4, 6, 7 and 13. Person 4 is connected to 8, person 6 is connected to 8, person 3 is not connected to 8, person 7 is not connected to 8 and person 13 is not connected to 8. Therefore, person 2 has two connections (4 and 6) that are connected to 8 and person 2 is not currently connected to 8. Therefore, person 2 might know person 8. 
Someone you probably know. For someone to be suggested here, the person must not currently be a connection of yours and that person must be a connection of 4 or more of your current connections. For example, consider person 2 in the above example. Person 2 is connected with 3, 4, 6, 7 and 13. Person 4 is connected to 9, person 6 is connected to 9, person 3 is connected to 9 and person 7 is connected to 9. Therefore, person 2 has at least four connections that are connected to 9 and person 2 is not currently connected to 9. Therefore, person 2 probably knows person 9. 

Your output should be formatted in the following fashion:

personID : Might(personA,…, personX) Probably(personA, … personX)

You have the person’s id following by a colon. The colon is followed by the list of Might’s separated by commas. If a person has no one they might be connected to, this list is not printed at all (see person 9 below for example). The Might list is followed by the Probably list separated by commas. If a person has no one they probably are connected to, this list is not printed at all (see person 3 for example). If a person has neither a might list or a probably list, that person only has their id along with a colon (see person 13 for example). As a concrete example from the above sample input, this would be the sample output:

1 : Might(4, 6, 7) Probably(11)
2 : Might(5, 8, 10) Probably(9)
3 : Might(4, 5, 6, 7, 8, 12) 
4 : Might(1, 3, 6, 11, 12) 
5 : Might(2, 3, 8, 10) Probably(9)
6 : Might(1, 3, 4, 7, 11) 
7 : Might(1, 3, 6) 
8 : Might(2, 3, 5, 9, 10) 
9 : Might(8, 10) Probably(2, 5)
10 : Might(2, 5, 8, 9) 
11 : Might(4, 6) Probably(1)
12 : Might(3, 4) 
13 : 

## Problem 3: Generating Data, Counting
Assume you work for a pet store and you want to know where to spend your marketing money. A “pet census” was sent to all cities in your area. Each city compiled the data and sent you the results. Each city compiled the data in different ways but they all followed a basic rule. For each citizen, a string appears in the file with the following information:
If the citizen owns 3 cats, 3 C’s show up in the string.
If the citizen owns 2 dogs, 2 D’s show up in the string.
If the citizen owns 4 fish, 4 F’s show up in the string.
If the citizen owns 1 monkey, 1 M shows up in the string.

For example, the citizen with 3 cats, 2 dogs, 4 fish and 1 monkey might appear as CCCDDFFFFM. However, another city may have compiled their information differently and that same citizen living in another city might have the string of CCDFDFCFMF. Your goal is to print out how many citizens have the exact same number of pets. For example, assume this is the input file:
        	CCDFM CDCDM FFDM FMDCC CDMFC MDFF
Your output would be:
        		CCDFM : 3
		CCDDM : 1
		DFFM : 2
All strings were separated by whitespace (either a space, tab or newline). The output should be what you see above. The string of pets on the left in alphabetical order, followed by a colon and then followed by the number of citizens with exactly those pets.


When you are working with Hadoop and other software at your job, you will likely be given some large dataset and have to work with it. This is the case with number 1. However, you will not be given a set of sample input and output files to test your code. Therefore, part of this project is coming up with your own sample input and output files. These samples can be completely random or you can generate them using some real world data (i.e. there are many more dogs and cats than fish and monkeys). You can expand some of the examples given in the questions and manually check if your answer is correct. If it is correct for several small cases, then you should feel good about your answer being correct for a large case that you can’t manually check.

