library(stringr)

input <- read.delim("day_12/input_12.txt", header = FALSE)
input <- as.matrix(input)

#part 1
nor_sou <- 0
eas_wes <- 0
face <- 90
action <- c()
value <- c()

for (i in 1:length(input)) {
  action <- substring(input[i], 1, 1)
  value <- as.numeric(substring(input[i], 2))
  if(action == "N"){
    nor_sou <- nor_sou + value
  }
  if(action == "S"){
    nor_sou <- nor_sou - value
  }
  if(action == "E"){
    eas_wes <- eas_wes + value
  }
  if(action == "W"){
    eas_wes <- eas_wes - value
  }
  if(action == "R"){
    face <- (face + value)%%360
  }
  if(action == "L"){
    face <- (face - value)%%360
  }
  if(action == "F"){
    if(face == 0){
      nor_sou <- nor_sou + value
    }
    if(face == 90){
      eas_wes <- eas_wes + value
    }
    if(face == 180){
      nor_sou <- nor_sou - value
    }
    if(face == 270){
      eas_wes <- eas_wes - value
    }
  }
}
sum <- abs(nor_sou)+abs(eas_wes)
print(paste0("Part 1: ", sum))
