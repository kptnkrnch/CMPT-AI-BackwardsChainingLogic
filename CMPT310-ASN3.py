import sys

# Project: CMPT310-ASN3
# Author: Joshua Campbell
# Student Number: 301266191
# Date: November 21, 2016

class Rule: # Rule class: contains the body of the rule and the result of the rule
    def __init__(self, body, result):
        self.body = body # the body of the rule
        self.result = result # the result of the rule
    def __str__(self): # for printing a rule
        ruleString = ""
        if self.body is not None:
            for i in range(len(self.body)):
                ruleString += self.body[i]
                if i < len(self.body) - 1:
                    ruleString += "^"
            ruleString += " => "
            ruleString += self.result
        else:
            ruleString += self.result
        return ruleString

# parseLine is used to parse a line from a rule file. It returns a Rule that it constructs from the line.
def parseLine(line):
    ruleBody = []
    for i in range(len(line)):
        if i == 0:
            result = line[i];
        if i > 0 and line[i].isalpha():
            ruleBody.append(line[i])
    if len(ruleBody) == 0:
        return Rule(None, result)
    else:
        return Rule(ruleBody, result)

def parseRuleFile(fileName): # reading the rule file
    rules = []
    with open(fileName) as f:
        content = f.readlines()
    if len(content) > 0:
        for line in content:
            rule = parseLine(line)  # reading a rule from the ruleFile
            rules.append(rule)

    return rules

def solve(queries, rules, solution, currentChain):
    if len(queries) == 0: # if we have found solutions for all queries/rules used
        return True # we return true
    query = queries.pop(0)
    for rule in rules:
        if rule.result == query:
            currentChain.append(rule) # current chain of rules used for attempting to solve the queries
            temp = []
            if rule.body is not None: # if the rule has a body, append the elements of that body to the new list of queries to solve
                temp += rule.body
            temp += queries # append the remaining queries to the list of atoms/queries to solve
            if solve(temp, rules, solution, currentChain): # if we have found a solution
                if rule not in solution: # if there is a duplicate rule in the solution, we don't add the rule
                    solution.append(rule) # this is for the Solution Rules used with no duplicates output.
                return True # if we have found a solution, we return true back up the recursion tree
            else: # if the solve algorithm returns false, it will output the current solution chain as failed
                print "Failed Solution Chain: ",
                for index in range(len(currentChain)):
                    item = currentChain[index]
                    if index != len(currentChain) - 1:
                        print "%s, " % (item),
                    else:
                        print "%s" % (item)
                currentChain.remove(rule) # once the failed chain has been outputted, the failed rule is removed from the chain
    return False # returns false if the algorithm fails to find a rule that satisfies the query correctly

def mainArgs(): # main program
    fileName = None
    if len(sys.argv) >= 2:
        fileName = sys.argv[1]
    else:
        print "Usage: python CMPT310-ASN3.py <rules fileName>"

    if fileName is not None:
        rules = parseRuleFile(fileName) # parsing the supplied rule file and creating the set of rules
        queries = []
        userInput = "y"
        # obtaining the set of queries from the user
        while userInput != "no" and userInput != "n" and userInput != "N" \
                and (userInput == "yes" or userInput == "y" or userInput == "Y"):
            userInput = raw_input("Enter a query: ")
            queries.append(userInput)
            userInput = raw_input("Would you like to add another query to the set? (yes/no): ")
        solution = [] # altered solution chain, duplicate rules are removed
        currentChain = [] # unaltered solution chain, shows exactly how the queries were derived by the algorithm
        print "--------------------------------------------------------------------------------------------------------"
        print "Query: ",
        for query in queries:
            print "%s, " % (query),
        print
        print "Rules: ",
        for rule in rules:
            print "%s, " % (rule),
        print
        print "--------------------------------------------------------------------------------------------------------"
        solve(queries, rules, solution, currentChain) # solving the queries
        print "Solution Rules (duplicates removed): ",
        if len(solution) > 0: # printing out the solution rules (no duplicates)
            solution.reverse()
            for rule in solution:
                if rule is not solution[len(solution) - 1]:
                    print "%s, " % (rule),
                else:
                    print "%s" % (rule)
        else:
            print "no solution"
        print "Unaltered Solution Chain: ",
        if len(currentChain) > 0: # printing out the solution chain (in the order rules were used)
            for index in range(len(currentChain)):
                rule = currentChain[index]
                if index is not len(currentChain) - 1:
                    print "%s, " % (rule),
                else:
                    print "%s" % (rule)
        else:
            print "no solution"

mainArgs()