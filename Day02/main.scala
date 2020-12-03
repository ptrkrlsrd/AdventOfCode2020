import scala.io.Source

object CheckPasswords {
  case class PasswordLine(low: Int, high: Int, checkChar: Char, password: String)

  def main(args: Array[String]): Unit = {
    val filename = "data/input.txt"
    val pattern = """(?:(\d+)\-(\d+) (\w)(?:\:) (\w+))""".r
    var passwordLines : Array[PasswordLine] = Array()

    for (line <- Source.fromFile(filename).getLines()) {
      val allMatches = pattern.findAllMatchIn(line)
      allMatches.foreach { m =>
        // TODO: How to destruct a string from regex into variables in Scala to clean up this mess?
        val low = m.group(1).toInt
        val high = m.group(2).toInt
        val char = m.group(3).charAt(0)
        val password = m.group(4)
        val passwordLine = PasswordLine(low, high, char, password)
        passwordLines :+= passwordLine
      }
    }

    var followsRule1 = 0
    var followsRule2 = 0

    // TODO: Find a better way to solve this
    for(line <- passwordLines) {
        val charCount = line.password.count(_ == line.checkChar)

        if (charCount >= line.low && charCount <= line.high) {
          followsRule1 += 1
        }

        val lowEqualsChar = line.password.charAt(line.low-1) == line.checkChar
        val highEqualsChar = line.password.charAt(line.high-1) == line.checkChar

        if (lowEqualsChar ^ highEqualsChar) {
          followsRule2 += 1
        }
    }

    println(followsRule1, followsRule2)
  }
}

