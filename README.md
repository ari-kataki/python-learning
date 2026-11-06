# python-learning

My Python exercises from the ITS course, January to April 2026, in the order I did them. It starts with simple lists and dictionaries and ends with exam-style console programs with classes, packages and JSON.

All the code is Python 3 without external libraries. Most of it is Italian course material (variable names and messages are in Italian). The folders are ordered by how far along I was, so you can see the progression.

| Folder | What it is | When | What I was learning |
|---|---|---|---|
| `01-basics-u4-u6` | Units 4-6 exercises: lists, dicts, try/except, generators, small functions (calculator, dice game) | Jan - Feb 2026 | Basic data structures, functions, error handling |
| `02-modules-u7` | Unit 7: string processing module and a `geometry` package | Feb 2026 | Modules and packages, imports |
| `03-json-intro` | First tests with JSON files and a small class | Feb 2026 | Reading JSON, `__str__` |
| `04-file-io-u8` | Unit 8, exercises 1-7 | Feb 2026 | Reading and writing text files |
| `05-inheritance-testedita` | Person / employee / team classes and 2D/3D points | Feb 2026 | Inheritance, `super()`, operator methods (`__add__`, `__len__`) |
| `06-oop-u9` | Unit 9, exercises 1-11 (triangle, clock, cipher, rectangle, 3D point, record label) | Feb - Mar 2026 | Classes, properties, several classes working together |
| `07-exam-sim-erp` | Practice exam: ERP with customers, suppliers, invoices and balance, saved in JSON | Mar 2026 | Packages (`parte1`, `parte2`), menu loop, JSON save/load |
| `08-library-manager-first-attempt` | Library management exam (users, books, loans), first version | Mar 2026 | Same structure with a loan class and states |
| `09-library-manager-second-attempt` | Same exam reworked: codice fiscale on the person, cross-platform clear/pause, date in the log, sample JSON | Mar 2026 | Refactoring helpers, logging with date |
| `10-football-club-sim` | Practice exam: football club (players, coaches, teams) with JSON | Apr 2026 | Bigger menu program, editing objects, JSON |
| `11-library-manager-final` | Library management again, the cleanest version of the pattern I follow for these exams | Apr 2026 | Applying the exam pattern from memory |

A separate small project, an unfinished gym exam, is in its own repo (`gym-management-python`).

## How to run
Run each file from inside its own folder, because the imports and the txt/json files are relative:
```
cd 02-modules-u7
python3 U7.py
```
For the exam programs (07-11) run `python3 main.py`. They use `cls` and `pause` to clear the screen, so they were written for Windows. On Mac/Linux they work but print a "command not found" for those two commands (09 has its own clear/pause helpers that work everywhere).

## Known issues
These are exercises, so some beginner mistakes are still there on purpose: for example `if __name__ == "__name__"` in a couple of files (so the test block never runs), subtraction/multiplication returning `a + b` in `Calcolatrice.py`, the rectangle area divided by 2 in the geometry package, an indentation mistake in `estraiFrequenzaDi` (`02-modules-u7`), and the `Squadra` class in `05` is unfinished.

A few files only needed small fixes to run again (indentation in `05-inheritance-testedita/squadra.py`, imports and missing `return`/`import math` in `02-modules-u7`, and in `10-football-club-sim` the files had been copied flat so I put them back in the `parte1` package).

The sample names in the JSON files are made up or example data from the course (I replaced a few that could be real people). `log.txt` files created by the exam programs are not kept in the repo.
