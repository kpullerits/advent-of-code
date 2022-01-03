library(stringr)

input <- read.delim("day_09/input_09.txt", header = FALSE)
input <- as.matrix(input)

# Part 1 ------------------------------------------------------------------

vallow <- 1
n <- 26
answer = integer()
for (i in n:length(input)) {
  valhigh <- i-1
  value <- input[i]
  exist <- FALSE
  
  for (j in vallow:(valhigh-1)) {
    
    for (k in (j+1):valhigh) {
      sum <- input[j] + input[k]
      if(sum == value){
        exist <- TRUE
      }
    }
  }  
  if(exist != TRUE){
    answer = input[i]
    break
  }
  vallow <- vallow +1
}

print(paste0("Part 1: ", answer))

# Part 2 ------------------------------------------------------------------

value <- answer
sumcount <- 0
i <- 1
j <- 1
exist <- FALSE

while (exist == FALSE) {

  for (i in j:length(input)) {
    line_value <- input[i]
    sumcount <- sumcount + line_value
    
    if(sumcount > value){
      j <- j + 1
      sumcount <- 0
      break
    }else if(sumcount == value) {
      exist <- TRUE
      break
    }
  }
}
sum <- min(input_filtered + max(input_filtered))
print(paste0("Part 2: ", sum))
