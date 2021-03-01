import pytest
from advent_of_code.year2020.conftest import format_name
from advent_of_code.year2020.day08.common import Instruction
from advent_of_code.year2020.day08.infinity_loop_detector_p2 import (
    solve_task, run_emulation
)


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


@pytest.mark.parametrize(
    "opts",
    [
        {
            "test_name": "Filename is provided",
            "filename": "example1.txt",
        },
        {
            "test_name": "Filename is absent",
            "filename": "",
        }
    ],
    ids=format_name
)
def test_solve_task(opts):
    got_trace, got_acc = solve_task(opts["filename"])
    assert isinstance(got_trace, list)
    assert isinstance(got_acc, int)
