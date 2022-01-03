library(stringr)

input <- read.delim("day_02/input_02.txt", header = FALSE)
input <- as.matrix(input)


# Part 1 ------------------------------------------------------------------

split_input <- read.table(textConnection(input))
split_input <- as.matrix(split_input)
minmax <- strsplit(split_input, "-")
minmax <- minmax[1:1000]
minmax <- matrix(unlist(minmax), ncol = 2, byrow = TRUE)
letters <- split_input[,2]
letters <- gsub(":", "", letters)
pw <- split_input[,3]

totalcount <- 0
for (i in 1:nrow(split_input)) {
  min <- as.numeric(minmax[i,1])
  max <- as.numeric(minmax[i,2])
  letter <- letters[i]
  count <- as.numeric(str_count(pw[i], letter))
  if(count >= min && count <= max){
    totalcount <- totalcount + 1
  }
}

print(paste0("Part 1: ", totalcount))


# Part 2 ------------------------------------------------------------------

totalcount <- 0
for (i in 1:nrow(split_input)) {
  pos1 <- as.numeric(minmax[i,1])
  pos2 <- as.numeric(minmax[i,2])
  letter <- letters[i]
  pos1val <- str_sub(pw[i], pos1,pos1)
  pos2val <- str_sub(pw[i], pos2,pos2)
  pos1valYN <- letter == pos1val
  pos2valYN <- letter == pos2val
  
  if((pos1valYN | pos2valYN) == TRUE && (pos1valYN && pos2valYN) == FALSE){
    totalcount <- totalcount + 1
  }
}

print(paste0("Part 2: ", totalcount))


