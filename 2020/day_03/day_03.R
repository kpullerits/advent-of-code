library(stringr)

input <- read.delim("day_03/input_03.txt", header = FALSE)
input <- as.matrix(input)

# Part 1 ------------------------------------------------------------------

totalcount <- 0
length <- as.numeric(nchar(input[1]))
for (i in 1:nrow(input)) {
  if(i == 1){
    pos <- 1
  }  else{
    pos <- pos + 3
    if(pos > length){
      pos <- pos %% length
    }
  }
  letter <- str_sub(input[i], pos,pos)
    if(letter == "#"){
      totalcount <- totalcount + 1
    }
}
print(paste0("Part 1: ", totalcount))

# Part 2 ------------------------------------------------------------------

count_vector <- c(totalcount)

#1
totalcount <- 0
pos <- 0
for (i in 1:nrow(input)) {
  if(i == 1){
    pos <- 1
  }  else{
    pos <- pos + 1
    if(pos > length){
      pos <- pos %% length
    }
  }
  letter <- str_sub(input[i], pos,pos)
  if(letter == "#"){
    totalcount <- totalcount + 1
  }
}
count_vector <- append(count_vector, totalcount)
#80

#3
totalcount <- 0
pos <- 0
for (i in 1:nrow(input)) {
  if(i == 1){
    pos <- 1
  }  else{
    pos <- pos + 5
    if(pos > length){
      pos <- pos %% length
    }
  }
  letter <- str_sub(input[i], pos,pos)
  if(letter == "#"){
    totalcount <- totalcount + 1
  }
}
#60
count_vector <- append(count_vector, totalcount)

#4
totalcount <- 0
pos <- 0
for (i in 1:nrow(input)) {
  if(i == 1){
    pos <- 1
  }  else{
    pos <- pos + 7
    if(pos > length){
      pos <- pos %% length
    }
  }
  letter <- str_sub(input[i], pos,pos)
  if(letter == "#"){
    totalcount <- totalcount + 1
  }
}
#63
count_vector <- append(count_vector, totalcount)

#5
totalcount <- 0
pos <- 0
for (i in seq(from = 1, to = (nrow(input)), by = 2)) {
  if(i == 1){
    pos <- 1
  }  else{
    pos <- pos + 1
    if(pos > length){
      pos <- pos %% length
    }
  }
  letter <- str_sub(input[i], pos,pos)
  if(letter == "#"){
    totalcount <- totalcount + 1
  }
  i <- i +1
}
#26
count_vector <- append(count_vector, totalcount)

print(paste0("Part 2: ", prod(count_vector)))
