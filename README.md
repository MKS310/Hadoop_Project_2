# Hadoop_Project_2
Big Data:High Performance Computing MapReduce Project


In this project, I worked with input, output, Python and the MapReduce framework. The mappers and reducers to solve a few different problems, listed below.

## Background
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

