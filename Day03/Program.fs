open System
open System.IO

type ExitCode = OK = 0 | Error = 1

type Slope(x, y) = 
    member this.X = x
    member this.Y = y

[<EntryPoint>]
let main argv =
    let mutable count = 0 
    let mutable right = 0 // TODO: Find a way to avoid mutable and make the code more functional
    let mutable down = 0

    let slope = Slope(3, 1)
    let lines = File.ReadLines "data/input.txt" |> Seq.toArray

    while down < Seq.length lines do
        let line = lines.[down]
        let lineLength = String.length(line)
        if line.[right % lineLength].Equals('#') then
            count <- count + 1

        right <- right + slope.X
        down <- down + slope.Y

    Console.WriteLine(count)
    int ExitCode.OK
