from strutils import Digits, parseInt
import sequtils, sugar
import strformat

proc task01(numbers: seq[int]): int =
  for i in numbers:
    for x in numbers:
      if i + x == 2020:
        return i * x

proc task02(numbers: seq[int]): int =
  for i in numbers:
    for x in numbers:
      for y in numbers:
        if i + x + y == 2020:
          return i * x * y

when isMainModule:
  let file = open("data/input.txt")
  var numbers = collect(newSeq):
    for line in file.lines:
      var parsedNumber = parseInt(line)
      parsedNumber

  echo fmt"Day 01. Task 01: {task01(numbers)}"
  echo fmt"Day 01. Task 02: {task02(numbers)}"
  

  file.close()