"""
* Assignment: RE Search Time
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use regular expressions to check `DATA` [1]
       contains time in UTC (24 hour clock compliant with ISO-8601)
    2. Define `result: str` with matched time
    3. Use real checking `xx:xx UTC`,
       where `x` is a valid digit at the position
    4. Text contains invalid date `24:56 UTC`
    5. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych do sprawdzenia czy `DATA` [1]
       zawiera godzinę w UTC (format 24 godzinny zgodny z ISO-8601)
    2. Zdefiniuj `result: str` ze znalezionym czasem
    3. Użyj poprawnego sprawdzania: `xx:xx UTC`,
       gdzie `x` to odpowiedni znak na danym miejscu
    4. Tekst zawiera niepoprawną godzinę: `24:56 UTC`
    5. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Wikipedia Apollo 11,
        URL: https://en.wikipedia.org/wiki/Apollo_11
        Year: 2019
        Retrieved: 2019-12-14

Hints:
    * `re.Match.group()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str, 'result must be a str'
    >>> assert result.endswith('UTC'), 'result must contain timezone'

    >>> result
    '02:56 UTC'
"""

import re


DATA = """Apollo 11 was the American spaceflight that first landed
humans on the Moon. Commander (CDR) Neil Armstrong and lunar module
pilot (LMP) Buzz Aldrin landed the Apollo Lunar Module (LM) Eagle on
July 20th, 1969 at 24:17 UTC, and Armstrong became the first person
to step (EVA) onto the Moon's surface (EVA) 6 hours 39 minutes later,
on July 21st, 1969 at 02:56 UTC. Aldrin joined him 19 minutes later.
They spent 2 hours 31 minutes exploring the site they had named
Tranquility Base upon landing. Armstrong and Aldrin collected 47.5 pounds
(21.5 kg) of lunar material to bring back to Earth as pilot Michael Collins
(CMP) flew the Command Module (CM) Columbia in lunar orbit, and were on the
Moon's surface for 21 hours 36 minutes before lifting off to rejoin
Columbia."""


# Pattern for searching time with timezone in 24 format, i.e. '23:59 UTC'
# Text contains invalid date `24:56 UTC`
# type: str
pattern = ...

# use re.search() to find pattern in DATA, get result text
# use .group() to get the value from re.Match object
# type: str
result = ...

