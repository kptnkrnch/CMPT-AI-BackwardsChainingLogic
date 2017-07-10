Program:
	CMPT310-ASN3.py - Used for solving a query using a knowledge base consisting of a set of rules
Prerequisites:
	These programs require Python version 2.7 in order to run.

Extra Supplied Files:
	rules.txt - the first example rules from the assignment specification
	rules2.txt - the second example rules from the assignment specification
	rules3.txt - a set of rules that will experience infinite recursion if the query is p or q

Running:
	CMPT310-ASN3:
		python CMPT310-ASN3.py <rule fileName>
		
Examples:
	Starting CMPT310-ASN3:
		python CMPT310-ASN3.py rules.txt
	Once running CMPT310-ASN3, you will be prompted to enter a query:
		Enter a query: a
	Once you are prompted to add another query to the set, enter "yes" if you want to enter another query or "no" if the set of queries is complete:
		Would you like to add another query to the set? (yes/no): yes
		Enter a query: q
		Would you like to add another query to the set? (yes/no): no
	In this case, the set of queries would look like this: {a, q}