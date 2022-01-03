library(stringr)
library(dplyr)

input <- read.delim("day_05/input_05.txt", header = FALSE)
input <- as.matrix(input)


# Part 1 ------------------------------------------------------------------

range <- c(0, 127)
i <- 1
row <- vector(mode="numeric", length=length(input))

while (range[1] != range[2]) {
  if(i == length(input)+1){
    break
  }
  for (j in 1:7) {
    if(str_sub(input[i], j,j) == "F"){
      range[2] <- floor((range[2] + range[1])/2)
    }
    if(str_sub(input[i], j,j) == "B"){
      range[1] <- ceiling((range[2] + range[1])/2)
    }
  }
  row[i] <- range[1]
  i <- i +1
  range <- c(0, 127)

}

col <- vector(mode="numeric", length=length(input))
range <- c(0, 7)
i <- 1
while (range[1] != range[2]) {
  if(i == length(input)+1){
    break
  }
  for (j in 8:10) {
    if(str_sub(input[i], j,j) == "L"){
      range[2] <- floor((range[2] + range[1])/2)
    }
    if(str_sub(input[i], j,j) == "R"){
      range[1] <- ceiling((range[2] + range[1])/2)
    }
  }
  col[i] <- range[1]
  i <- i +1
  range <- c(0, 7)
}

rowcol <- cbind(row,col)
rowcoldf <- as.data.frame(rowcol)
rowcoldf$seat_ID <- (rowcoldf$row * 8)+rowcoldf$col
print(paste0("Part 1: ", max(rowcoldf$seat_ID))) 

# Part 2 ------------------------------------------------------------------

rowcoldf2 <- arrange(rowcoldf, desc(seat_ID))
# setdiff(1:805, rowcoldf$seat_ID)
# setdiff(1:890, rowcoldf$seat_ID)
print(paste0("Part 2: ", max(setdiff(1:max(rowcoldf$seat_ID), rowcoldf$seat_ID))))
