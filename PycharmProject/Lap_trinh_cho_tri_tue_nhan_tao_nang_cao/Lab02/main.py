import pickle, gzip, os, random
import sys
import os
import collections

from logic import *
from typing import Tuple, List


def checkFormula(name, predForm, preconditionForm=None):
    filename = os.path.join('models', name + '.pklz')
    objects, targetModels = pickle.load(gzip.open(filename))

    # If preconditionion exists, change the formula to
    preconditionPredForm = And(preconditionForm, predForm) if preconditionForm else predForm
    predModels = performModelChecking([preconditionPredForm], findAll=True, objects=objects)
    ok = True

    def hashkey(model):
        return tuple(sorted(str(atom) for atom in model))

    targetModelSet = set(hashkey(model) for model in targetModels)
    predModelSet = set(hashkey(model) for model in predModels)
    for model in targetModels:
        if hashkey(model) not in predModelSet:
            print("Your formula (%s) says the following model is FALSE, but it should be TRUE:" % predForm)
            ok = False
            printModel(model)
            return
    for model in predModels:
        if hashkey(model) not in targetModelSet:
            print("Your formula (%s) says" % targetModelSet)
            printModel(model)
            return

    print(f"You matched the {len(targetModels)} models")
    print(f"Example model: {rstr(random.choice(targetModels))}")
    return True


def checkFormulaCustom(exampleForm, predForm, preconditionForm=None):
    objects = []

    # If preconditionion exists, change the formula to
    preconditionPredForm = And(preconditionForm, predForm) if preconditionForm else predForm
    predModels = performModelChecking([preconditionPredForm], findAll=True, objects=objects)
    examplePredForm = And(preconditionForm, exampleForm) if preconditionForm else exampleForm
    exampleModels = performModelChecking([examplePredForm], findAll=True, objects=objects)
    ok = True

    def hashkey(model):
        return tuple(sorted(str(atom) for atom in model))

    targetModelSet = set(hashkey(model) for model in exampleModels)
    predModelSet = set(hashkey(model) for model in predModels)
    return targetModelSet == predModelSet


def formula1a() -> Formula:
    Summer = Atom('Summer')
    California = Atom('California')
    Rain = Atom('Rain')
    SummerCalifornia = And(Summer, California)
    return Or(SummerCalifornia, Not(Rain), Rain, )
#
# assert checkFormula('1a', formula1a()) == True

# def formula1b() -> Formula:
#     # Predicates to use:
#     Rain = Atom('Rain')              # whether it is raining
#     Wet = Atom('Wet')                # whether it it wet
#     Sprinklers = Atom('Sprinklers')  # whether the sprinklers are on
#     # YOUR CODE HERE
#     RainAndSpinklers = Or(Rain, Sprinklers)
#     return Equiv(Wet, RainAndSpinklers)
#     raise NotImplementedError()
#
# assert checkFormula('1b', formula1b()) == True

# def formula1c() -> Formula:
#     # Predicates to use:
#     Day = Atom('Day')     # whether it's day
#     Night = Atom('Night') # whether it's night
#     # YOUR CODE HERE
#     return And(Or(Day, Night), Not(And(Day, Night)))
#     raise NotImplementedError()
#
# assert checkFormula('1c', formula1c()) == True

# def formula2a() -> Formula:
#     # Predicates to use:
#     def Person(x): return Atom('Person', x)        # whether x is a person
#     def Mother(x, y): return Atom('Mother', x, y)  # whether x's mother is y
#
#     # Note: You do NOT have to enforce that the mother is a "person"
#     # YOUR CODE HERE
#     return Forall('$x', Exists('$y', Implies(Person('$x'), Mother('$x', '$y'))))
#     raise NotImplementedError()
#
# formula2a_precondition = AntiReflexive('Mother')
# assert checkFormula('2a', formula2a(), formula2a_precondition) == True

# def formula2b() -> Formula:
#     # Predicates to use:
#     def Person(x): return Atom('Person', x)        # whether x is a person
#     def Child(x, y): return Atom('Child', x, y)    # whether x has a child y
#
#     # Note: You do NOT have to enforce that the child is a "person"
#     # YOUR CODE HERE
#     return Exists('$x', Forall('$y', And(Person('$x'), Not(Child('$x', '$y')))))
#     raise NotImplementedError()
#
# formula2b_precondition = AntiReflexive('Child')
# assert checkFormula('2b', formula2b(), formula2b_precondition) == True

# def formula2c() -> Formula:
#     # Predicates to use:
#     def Female(x): return Atom('Female', x)  # whether x is female
#
#     def Child(x, y): return Atom('Child', x, y)  # whether x has a child y
#
#     def Daughter(x, y): return Atom('Daughter', x, y)  # whether x has a daughter y
#
#     # YOUR CODE HERE
#     return Forall('$x', Forall('$y', Equiv(Daughter('$x', '$y'), And(Female('$y'), Child('$x', '$y')))))
#     raise NotImplementedError()
#
# formula2c_precondition = AntiReflexive('Child')
# assert checkFormula('2c', formula2c(), formula2c_precondition) == True

# Note: It is ok for a person to be her own parent
# def formula2d() -> Formula:
#     # Predicates to use:
#     def Female(x): return Atom('Female', x)                  # whether x is female
#     def Parent(x, y): return Atom('Parent', x, y)            # whether x has a parent y
#     def Grandmother(x, y): return Atom('Grandmother', x, y)  # whether x has a grandmother y
#     # YOUR CODE HERE
#     return Forall('$x', Forall('$z', Equiv(Grandmother('$x', '$z'), Exists('$y', AndList([Female('$z'), Parent('$x', '$y'), Parent('$y', '$z')])))))
#     raise NotImplementedError()
#
# formula2d_precondition = AntiReflexive('Parent')
# assert checkFormula('2d', formula2d(), formula2d_precondition) == True

# Problem 3: Liar puzzle

# Facts:
# 0. John: "It wasn't me!"
# 1. Susan: "It was Nicole!"
# 2. Mark: "No, it was Susan!"
# 3. Nicole: "Susan's a liar."
# 4. Exactly one person is telling the truth.
# 5. Exactly one person crashed the server.
# Query: Who did it?

# This function returns a list of 6 formulas corresponding to each of the
# above facts. Be sure your formulas are exactly in the order specified.


# Hint: For fact 4 & 5, you might want to use the Equals predicate, defined as:
# def Equals(x, y): return Atom('Equals', x, y)
# This predicate is used to assert that two objects are the same.
# In particular, Equals(x,x) = True and Equals(x,y) = False iff x is not equal to y.
# It can also be solved in other ways, without the Equals predicate!

def liar() -> Tuple[List[Formula], Formula]:
    def TellTruth(x): return Atom('TellTruth', x)

    def CrashedServer(x): return Atom('CrashedServer', x)

    john = Constant('john')
    susan = Constant('susan')
    nicole = Constant('nicole')
    mark = Constant('mark')
    formulas = []
    # We provide the formula for fact 0 here.
    formulas.append(Equiv(TellTruth(john), Not(CrashedServer(john))))

    # You should add 5 formulas, one for each of facts 1-5.
    # YOUR CODE HERE
    formulas.append(Equiv(TellTruth(susan), CrashedServer(nicole)))
    formulas.append(Equiv(TellTruth(mark), CrashedServer(susan)))
    formulas.append(Equiv(TellTruth(nicole), Not(TellTruth(susan))))
    formulas.append(Exists('$x', And(TellTruth('$x'), Forall('$y', Implies(TellTruth('$y'), Equals('$x', '$y'))))))
    formulas.append(Exists('$x', And(CrashedServer('$x'), Forall('$y', Implies(CrashedServer('$y'), Equals('$x', '$y'))))))
    # raise NotImplementedError()
    query = CrashedServer('$x')
    return (formulas, query)


predForms, predQuery = liar()
assert len(predForms) == 6

predForms, predQuery = liar()
formula_id = 0
assert checkFormula('3a-' + str(formula_id), predForms[formula_id]) == True

predForms, predQuery = liar()
formula_id = 1
assert checkFormula('3a-' + str(formula_id), predForms[formula_id]) == True

predForms, predQuery = liar()
formula_id = 2
assert checkFormula('3a-' + str(formula_id), predForms[formula_id]) == True

predForms, predQuery = liar()
formula_id = 3
assert checkFormula('3a-' + str(formula_id), predForms[formula_id]) == True

predForms, predQuery = liar()
formula_id = 4
assert checkFormula('3a-' + str(formula_id), predForms[formula_id]) == True

predForms, predQuery = liar()
formula_id = 5
assert checkFormula('3a-' + str(formula_id), predForms[formula_id]) == True

predForms, predQuery = liar()
assert checkFormula('3a-all', AndList(predForms)) == True

# Run this cell to solve the puzzle and find out who was the liar!
predForms, predQuery = liar()
kb = createModelCheckingKB()

filename = os.path.join('models', '3a-all.pklz')
objects, targetModels = pickle.load(gzip.open(filename))
for obj in objects:
    kb.tell(Atom('Object', obj))

for predForm in predForms:
    response = kb.tell(predForm)

response = kb.ask(predQuery)
showKBResponse(response)

# def read_input_file(file_path):
#     with open(file_path, 'r') as file:
#         lines = file.read().splitlines()
#     lines = [line for line in lines if line]
#     return lines
#
# def process_input(lines):
#     query = lines[0]
#     size = int(lines[1])
#     clauses = lines[2:]
#
#     return query, size, clauses
#
# def parse_clause(clause):
#     literals = clause.split()
#     parsed_literals = []
#     for literal in literals:
#         if literal == "OR":
#             continue
#         parsed_literals.append(parse_symbol(literal))
#     if len(parsed_literals) == 2:
#         result = Or(*parsed_literals)
#     elif len(parsed_literals) > 2:
#         result = OrList(parsed_literals)
#     else:
#         result = parsed_literals[0]
#     return result
#
# def parse_symbol(symbol):
#     if symbol.startswith("-"):
#         return Not(Atom(symbol[1:]))
#     else:
#         return Atom(symbol)
#
# def parse_query(query):
#     symbols = query.split()
#     parsed_query = []
#
#     for symbol in symbols:
#         parsed_query.append(parse_symbol(symbol))
#
#     return parsed_query
#
# def process_clauses(clauses):
#     parsed_clauses = []
#
#     for clause in clauses:
#         parsed_clauses.append(parse_clause(clause))
#
#     return parsed_clauses
#
# def convert_to_desired_format(expression_str):
#     expression_str = expression_str.replace('Or(', '').replace(')', '')
#
#     literals = [literal.strip() for literal in expression_str.split(',')]
#
#     return " Or ".join(literals)
#
# def convert_to_desired_format(expression_str):
#     expression_str = expression_str.replace('Or(', '').replace(')', '')
#
#     # Replace "Not(" with "-"
#     expression_str = expression_str.replace('Not(', '-')
#
#     # Split the string by commas and remove spaces
#     literals = [literal.strip() for literal in expression_str.split(',')]
#
#     # Join literals using " OR "
#     return " OR ".join(literals)
#
# def generate_output(clauses):
#     output_lines = []
#
#     for clause in clauses:
#         or_expression = convert_to_desired_format(str(clause))
#         output_lines.append(or_expression)
#
#     with open('output.txt', 'w') as output_file:
#         output_file.write('\n'.join(output_lines))
#
# if __name__ == "__main__":
#     file_path = "input.txt"
#     output_file_path = 'output.txt'
#     input_lines = read_input_file(file_path)
#
#     if len(input_lines) >= 3:
#         query, size, clauses = process_input(input_lines)
#         print("Query:", query)
#         print("Size:", size)
#         print("Clauses:", clauses)
#         parsed_query = parse_query(query)
#         print("Parsed Query:", parsed_query[0])
#         parsed_clauses = process_clauses(clauses)
#         print("Parsed Clauses:", parsed_clauses)
#         # A = Atom('A')
#         # B = Atom('B')
#         # C = Atom('C')
#         # example = Or(Or(A, B), C)
#         # example_result = str(example)
#         # formatted_string = convert_to_desired_format(example_result)
#         # print(formatted_string)
#
#         generate_output(parsed_clauses)




