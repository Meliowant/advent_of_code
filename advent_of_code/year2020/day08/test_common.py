from advent_of_code.year2020.conftest import format_name
from advent_of.code.year2020.day08.common import (
    Instruction,
    read_file,
    run_emulation,
    instruction_index,
)
import pytest


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "File with single instruction",
            "filename": "test_input1.txt",
            "exp_result": [(Instruction(cmd="nop", pos=0, arg=0))],
        },
        {
            "test_name": "File with few instructions",
            "filename": "test_input2.txt",
            "exp_result": [
                (Instruction(cmd="nop", pos=0, arg=0)),
                (Instruction(cmd="acc", pos=1, arg=1)),
                (Instruction(cmd="jmp", pos=2, arg=-2)),
            ],
        },
        {
            "test_name": "Reference file from Advent of Code, part 1",
            "filename": "example1.txt",
            "exp_result": [
                (Instruction(cmd="nop", pos=0, arg=0)),
                (Instruction(cmd="acc", pos=1, arg=1)),
                (Instruction(cmd="jmp", pos=2, arg=4)),
                (Instruction(cmd="acc", pos=3, arg=3)),
                (Instruction(cmd="jmp", pos=4, arg=-3)),
                (Instruction(cmd="acc", pos=5, arg=-99)),
                (Instruction(cmd="acc", pos=6, arg=1)),
                (Instruction(cmd="jmp", pos=7, arg=-4)),
                (Instruction(cmd="acc", pos=8, arg=6)),
            ],
        },
    ],
    ids=format_name,
)
def test_read_file(opts):
    acquired_struct = read_file(opts["filename"])
    assert acquired_struct == opts["exp_result"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Instruction exists in list",
            "input_data": [
                [(Instruction(cmd="nop", pos=0, arg=0)), [1]],
                [(Instruction(cmd="acc", pos=1, arg=1)), [2]],
                [(Instruction(cmd="jmp", pos=2, arg=-2)), [3]],
            ],
            "instruction": (Instruction(cmd="acc", pos=1, arg=1)),
            "expected_index": 1,
        },
        {
            "test_name": "Instruction doesn't exist in list",
            "input_data": [
                [(Instruction(cmd="nop", pos=0, arg=0)), [1]],
                [(Instruction(cmd="acc", pos=1, arg=1)), [2]],
                [(Instruction(cmd="jmp", pos=2, arg=-2)), [3]],
            ],
            "instruction": Instruction(cmd="acc", pos=4, arg=1),
            "expected_index": -1,
        },
    ],
    ids=format_name,
)
def test_instruction_index(opts):
    got_index = instruction_index(opts["instruction"], opts["input_data"])
    assert got_index == opts["expected_index"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Single NOP instruction",
            "code": [Instruction(cmd="nop", pos=0, arg=0)],
            "trace": [[Instruction(cmd="nop", pos=0, arg=0), [1]]],
            "acc_value": 0,
        },
        {
            "test_name": "Two instructions. Straight-forward.",
            "code": [
                Instruction(cmd="nop", pos=0, arg=0),
                Instruction(cmd="acc", pos=1, arg=1),
            ],
            "trace": [
                [Instruction(cmd="nop", pos=0, arg=0), [1]],
                [Instruction(cmd="acc", pos=1, arg=1), [2]],
            ],
            "acc_value": 1,
        },
        {
            "test_name": "Three instructions. The last makes loop on "
            "previous one",
            "code": [
                Instruction(cmd="nop", pos=0, arg=0),
                Instruction(cmd="acc", pos=1, arg=1),
                Instruction(cmd="jmp", pos=2, arg=-2),
            ],
            "trace": [
                [Instruction(cmd="nop", pos=0, arg=0), [1, 4]],
                [Instruction(cmd="acc", pos=1, arg=1), [2]],
                [Instruction(cmd="jmp", pos=2, arg=-2), [3]],
            ],
            "acc_value": 1,
        },
        {
            "test_name": "Advent of code, p1. Reference input",
            "code": [
                (Instruction(cmd="nop", pos=0, arg=0)),
                (Instruction(cmd="acc", pos=1, arg=1)),
                (Instruction(cmd="jmp", pos=2, arg=4)),
                (Instruction(cmd="acc", pos=3, arg=3)),
                (Instruction(cmd="jmp", pos=4, arg=-3)),
                (Instruction(cmd="acc", pos=5, arg=-99)),
                (Instruction(cmd="acc", pos=6, arg=1)),
                (Instruction(cmd="jmp", pos=7, arg=-4)),
                (Instruction(cmd="acc", pos=8, arg=6)),
            ],
            "trace": [
                [Instruction(cmd="nop", pos=0, arg=0), [1]],
                [Instruction(cmd="acc", pos=1, arg=1), [2, 8]],
                [Instruction(cmd="jmp", pos=2, arg=4), [3]],
                [Instruction(cmd="acc", pos=3, arg=3), [6]],
                [Instruction(cmd="jmp", pos=4, arg=-3), [7]],
                [Instruction(cmd="acc", pos=6, arg=1), [4]],
                [Instruction(cmd="jmp", pos=7, arg=-4), [5]],
            ],
            "acc_value": 5,
        },
    ],
    ids=format_name,
)
def test_run_emulation(opts):
    got_trace, got_value = run_emulation(opts["code"])
    assert got_trace == sorted(opts["trace"], key=lambda x: x[1][0])
    assert got_value == opts["acc_value"]
