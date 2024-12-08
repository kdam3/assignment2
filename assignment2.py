#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py 
Author: "Kameron Dam"
Semester: "Fall 2024"

The python code in this file is original work written by
"Kameron Dam". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <github.com/kdam3/assignment2-versionA>

'''

import argparse
import os, sys

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts",epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    parser.add_argument(
        "-H", "--human-readable",
        action="store_true",
        help="Prints human readable format"
    )
    # check the docs for an argparse option to store this as a boolean.
    parser.add_argument("program", type=str, nargs='?', help="if a program is specified, show memory use of all associated processes. Show only total use is not.")
    args = parser.parse_args()
    return args
# create argparse function
# -H human readable
# -r running only

def percent_to_graph(percent: float, length: int=20) -> str:
    "turns a percent 0.0 - 1.0 into a bar graph"
    ...
    num_hashes = int(percent * length)
    num_spaces = length - num_hashes
    graph = "#" * num_hashes + " " * num_spaces
    return graph
# percent to graph function

def get_sys_mem() -> int:
    "return total system memory (used or available) in kB"
    ...
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if line.startswith("MemTotal"):
                mem_total = int(line.split()[1])
                return mem_total


def get_avail_mem() -> int:
    "return total memory that is available"
    ...
    with open('/proc/meminfo', 'r') as f:
        mem_free = None
        swap_free = None
        mem_available = None
        for line in f:
            if line.startswith("MemAvailable"):
                mem_available = int(line.split()[1])
            elif line.startswith("MemFree"):
                mem_free = int(line.split()[1])
            elif line.startswith("SwapFree"):
                swap_Free = int(line.split()[1])

        if mem_available is not None:
            return mem_available
        else:
            return mem_free + swap_free

def pids_of_prog(app_name: str) -> list:
    "given an app name, return all pids associated with app"
    ...
    pid = []
    result = os.open(f"pgrep {app_name}").read().strip()
    if result:
        pigs = result.splitlines()
    return pids


def rss_mem_of_pid(proc_id: str) -> int:
    "given a process id, return the resident memory used, zero if not found"
    ...
    try:
        with open(f"/proc/{proc_id}/stat", 'r') as f:
            stat_info = f.read().split()
            rss_kb = int(stat_info[23])
        return rss_kb

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:
        ...
        total_mem = get_sys_mem()
        available_mem = get_avail_mem()
        used_mem = total_mem - available_mem
        percent_used = (used_mem / total_mem) * 100
        graph = percent_to_graph(percent_used, args.length)

    else:
        ...
    # process args
    # if no parameter passed, 
    # open meminfo.
    total_mem = get_sys_mem()
    available_mem = get_avail_mem()

    # get used memory
    used_mem = total_mem - available_mem
    # get total memory
    # call percent to graph
    # print
    print(f"Total Memory: {total_mem) in kB")
    print(f"Available Memory: {available_mem} in kB")
    print(f"Memory Used: {used_mem} in kB")

    # if a parameter passed:
    # get pids from pidof
    # lookup each process id in /proc
    # read memory used
    for pid in pids:
        pid_mem = rss_mem_of_pid(pid)
        total_used_mem_program += pid_mem
    # add to total used
    # percent to graph
    # take total our of total system memory? or total used memory? total used memory.
    # percent to graph.
