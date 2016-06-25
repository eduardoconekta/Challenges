module Main where

{-
 - Problem Statement:
 - http://code.google.com/codejam/contest/351101/dashboard#s=p1
 -
 - Usage either compile or use runhaskell / runghc
 - Pass the input file as the sole command line argument
 - Redirect output if you want the results to go in a file
 -}

import System.Environment
import Data.List

reverseWords :: String -> String
reverseWords = unwords . reverse . words

boilerPlate :: [String]
boilerPlate = ["Case #" ++ show n ++ ": " | n <- [1..]]

standardOutput :: [String] -> [String]
standardOutput = zipWith (++) boilerPlate

main =  do
  (f:_) <- getArgs
  file  <- readFile f

  let cases     = tail $ lines file
      solutions = standardOutput $ map reverseWords cases
  putStrLn $ unlines $ solutions