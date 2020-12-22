#!/usr/bin/python3
import sys
import os

up1 = os.path.abspath('..')
sys.path.insert(0, up1)

from conftest import read_blocks_data

def extract_groups_unique_answers(answers_list):
    all_answers = []
    for answer_group in answers_list:
        ag = []
        for answer in answer_group:
            ag.extend(answer)
        all_answers.append(set(ag))

    if len(all_answers) == 0:
        return set()
    return set.intersection(*all_answers)


def extract_answers(all_answers):
    all_answers_count = [len(extract_groups_unique_answers(x)) for x in all_answers]
    total_yes_answers = sum(all_answers_count)
    return total_yes_answers


def solve_the_task(filename="answers.txt"):
    answers_by_groups = read_blocks_data(filename)
    total_answers = extract_answers(answers_by_groups)
    print(f"Collected answers from {len(answers_by_groups)} groups")
    print(f"Totally '{total_answers}' were 'yes' answers")
    return total_answers


if __name__ == "__main__":
    solve_the_task()
