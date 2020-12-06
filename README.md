# AdventOfCode2020

Languages in order of appearance:
- [Nim](https://nim-lang.org/), [Scala](https://www.scala-lang.org/), [F#](https://fsharp.org/), [Python](https://fsharp.org/), [Haskell](https://haskell.org)

Languages I want to solve the upcoming tasks with:
- Definitely: C++, C, Rust, Elixir/Erlang, C#
- Maybe: Cobol, Bash, Powershell(*jikes, what a way to make 2020 worse!*), Java, Prolog

## Day 01 - https://nim-lang.org/
* Have I used it before? No
* Did I like it? Yeah, kind of. At times it felt like a fast Python with even more syntax sugar than the newest versions of Python(and that says a lot!). On top of it all I love that it's compiled(or transpiled?).
## Day 02 - https://www.scala-lang.org/
* Have I used it before? Yes, but only tested it
* Did I like it? I initially tried this challenge using Lua, but quickly figured out Lua wasn't for me. I saw Scala as a good choice for this task from what I'd seen and I was right! There's a lot to the code I know can be simplified. For example the initialization of variables from the regex groups. I hate how slow it compiles and that it outputs jar-files.
* How would I improve the code? By utilizing more of Scalas features I think it would be possible to simplify the code a lot.
## Day 03 - https://fsharp.org/
* Have I used it before? Yes, but only tested it
* Did I like it? I liked it quite a lot. If I had the opportunity to use it instead of C# at work, I'd easily do it.
* Day 3 was really difficult, and therefore I haven't finished the solution yet.
## Day 04 - https://www.python.org/
* Have I used it before? Yes, quite a lot
* First approach: I began with using regex to validate the passports, but didn't like how it turned out. Then I found `scheme` and felt it was a great solution.
* Did I like it? Using Python3.9 for this task really made me miss my old Python days. Writing the code was a breeze! I hadn't used the `scheme`library before but it's way nicer than using dang if-tests to validate code.
* TIL: 
https://stackoverflow.com/questions/4764547/creating-dictionary-from-space-separated-key-value-string-in-python
```python
import shelex
print(dict(token.split('=') for token in shlex.split(s)))
```

## Day 06 - https://www.haskell.org/
* Have I used it before? Yes, a little bit.
* This task was a perfect match for Haskell in my opinion. I'm not all that happy about the part of the solution where I replace multiple newlines with a comma to then split the string by commas, but it worked.
* Did I like it? I love working with Haskell as it puts problem solving in focus, and because there are so many great libraries out there.
