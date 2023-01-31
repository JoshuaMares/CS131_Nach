dedup :: [Integer]->[Integer]
dedup [] = []
dedup (x:[]) = [x]
dedup (x:xs) =
  if x == head xs
    then dedup xs
    else x : dedup xs
