module Main where
{-# LANGUAGE OverloadedStrings #-}
  
import System.IO     
import Data.List
import Text.Regex
import Data.Text (strip, unpack, pack)
import Data.Set (toList, fromList)

uniquify lst = toList $ fromList lst

splitByComma :: String -> [String]
splitByComma [] = [""]
splitByComma (c:cs) | c == ','  = "" : rest
             | otherwise = (c : head rest) : tail rest
    where rest = splitByComma cs

stripWhitespace :: [Char] -> [Char]
stripWhitespace a = filter (\c -> c /= '\n') a

main = do     
    withFile "data/input.txt" ReadMode (\handle -> do  
        content <- hGetContents handle     
        putStr (show 
            $ sum $ map length -- Maps over each item and returns the length, thereafter sums the items
            $ map (\w -> stripWhitespace $ uniquify w) -- Strip whitespaces and find unique chars
            $ splitByComma -- Splits the content into an array by ,
            $ subRegex (mkRegex "\n\n") content ",")) -- Replaces \n\n with , to make it easier to split later