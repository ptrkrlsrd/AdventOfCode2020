open System
open System.IO

type ExitCode = OK = 0 | Error = 1

let keepTrees (idx: Char) =
    idx.Equals('#')

[<EntryPoint>]
let main argv =
    let increaseBy = 4
    let mutable count = 0 // TODO: Find a way to avoid mutable
    let mutable column = 0

    let lines = File.ReadLines("data/input.txt")

    let a = 
        lines |> Seq.skip(1)
        |> Seq.map (fun line ->
            column <- column + increaseBy
            line.[column..line.Length]
        )
        |> Seq.concat
        |> Seq.filter keepTrees
        |> String.Concat
        |> Seq.length

    Console.WriteLine(a)

    int ExitCode.OK
