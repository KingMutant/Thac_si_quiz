import pickle, gzip, os, random
import sys
import os
import collections

from logic import *
from typing import Tuple, List


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    lines = [line for line in lines if line]
    return lines

def process_input(lines):
    query = lines[0]
    size = int(lines[1])
    clauses = lines[2:]

    return query, size, clauses

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

def parse_clause(clause):
    literals = clause.split()
    parsed_literals = []
    for literal in literals:
        if literal == "OR":
            continue
        parsed_literals.append(parse_symbol(literal))
    if len(parsed_literals) == 2:
        result = Or(*parsed_literals)
    elif len(parsed_literals) > 2:
        result = OrList(parsed_literals)
    else:
        result = parsed_literals[0]
    return result

def parse_symbol(symbol):
    if symbol.startswith("-"):
        return Not(Atom(symbol[1:]))
    else:
        return Atom(symbol)

def parse_query(query):
    symbols = query.split()
    parsed_query = []

    for symbol in symbols:
        parsed_query.append(parse_symbol(symbol))

    return parsed_query

def process_clauses(clauses):
    parsed_clauses = []

    for clause in clauses:
        parsed_clauses.append(parse_clause(clause))

    return parsed_clauses

def convert_to_desired_format(expression_str):
    expression_str = expression_str.replace('Or(', '').replace(')', '')

    literals = [literal.strip() for literal in expression_str.split(',')]

    return " Or ".join(literals)

def convert_to_desired_format(expression_str):
    expression_str = expression_str.replace('Or(', '').replace(')', '')

    # Replace "Not(" with "-"
    expression_str = expression_str.replace('Not(', '-')

    # Split the string by commas and remove spaces
    literals = [literal.strip() for literal in expression_str.split(',')]

    # Join literals using " OR "
    return " OR ".join(literals)

def generate_output(clauses):
    output_lines = []
    size_of_clauses = len(clauses)
    output_lines.append(f"{size_of_clauses}")
    for clause in clauses:
        or_expression = convert_to_desired_format(str(clause))
        output_lines.append(or_expression)

    with open('output.txt', 'w') as output_file:
        output_file.write('\n'.join(output_lines))
        output_file.write('\n')

def generate_output_append(clauses):
    output_lines = []
    size_of_clauses = len(clauses)
    output_lines.append(f"{size_of_clauses}")
    for clause in clauses:
        or_expression = convert_to_desired_format(str(clause))
        output_lines.append(or_expression)

    with open('output.txt', 'a') as output_file:
        output_file.write('\n'.join(output_lines))
        output_file.write('\n')

if __name__ == "__main__":
    file_path = "input.txt"
    output_file_path = 'output.txt'
    input_lines = read_input_file(file_path)
    kb_given = createResolutionKB()
    kb_negation_conclusion = createResolutionKB()

    if len(input_lines) >= 3:
        query, size, clauses = process_input(input_lines)
        sorted_clause  = sorted(clauses, key=len, reverse=True)

        print("Query:", query)
        print("Size:", size)
        print("Clauses:", clauses)
        parsed_query = parse_query(query)
        print("Parsed Query:", parsed_query[0])
        # parsed_clauses = process_clauses(sorted_clause)
        # print("Sorted Parsed Clauses:", parsed_clauses)
        clause_1_atom = [item for item in sorted_clause if len(item) <= len('-B')]
        clause_2_atom = [item for item in sorted_clause if len('-B') < len(item) <= len('-B OR -C')]
        clause_3_atom = [item for item in sorted_clause if len('-B OR -C') < len(item) <= len('-A OR -B OR -C')]
        print("Clause 1:", clause_1_atom)
        print("Clause 2:", clause_2_atom)
        print("Clause 3:", clause_3_atom)
        clause_1_atom = process_clauses(clause_1_atom)
        clause_2_atom = process_clauses(clause_2_atom)
        clause_3_atom = process_clauses(clause_3_atom)
        new_parsed_clauses = clause_2_atom + clause_3_atom + clause_1_atom
        # new_parsed_clauses = process_clauses(new_parsed_clauses)

        for clause in new_parsed_clauses:
            response = kb_given.tell(clause)

        for clause_2 in clause_2_atom:
            response = kb_negation_conclusion.tell(clause_2)
        for clause_3 in clause_3_atom:
            response = kb_negation_conclusion.tell(clause_3)
        response = kb_negation_conclusion.tell(Not(parsed_query[0]))

        new_2_atom_negation = []
        for key, value in kb_negation_conclusion.derivations.items():
            if value.cost == 1:
                new_2_atom_negation.append(key)
        for key, value in kb_given.derivations.items():
            if value.cost == 1:
                new_2_atom_negation.append(key)

        new_3_atom_negation = []
        for key, value in kb_negation_conclusion.derivations.items():
            if value.cost == 2:
                new_3_atom_negation.append(key)
        for key, value in kb_given.derivations.items():
            if value.cost == 2:
                new_3_atom_negation.append(key)

        kb_negation_conclusion_1_atom = []
        for key, value in kb_negation_conclusion.derivations.items():
            if value.cost == 1:
                kb_negation_conclusion_1_atom.append(key)

        generate_output(new_2_atom_negation)
        generate_output_append(new_3_atom_negation)

        for clause in kb_negation_conclusion_1_atom:
            response_string = str(kb_given.tell(clause))
            print('Response from KB', response_string)
            if response_string == 'I already knew that.':
                with open('output.txt', 'a') as output_file:
                    output_file.write('0\n')
                    output_file.write('No.\n')

            elif response_string == 'I don\'t buy that.':
                with open('output.txt', 'a') as output_file:
                    output_file.write('{}\n')
                    output_file.write('Yes.\n')


