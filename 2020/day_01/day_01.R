input <- read.delim("day_01/input_01.txt", header = FALSE)
input <- as.matrix(input)

# Part 1 -----------------------------------------------------------------

i <- 1:length(input)
j <- 1:length(input)
for (i in seq_along(input)){
  n1 <- input[i]
  for (j in seq_along(input)){
    n2 <- input[j]
    sum <- n1 + n2
    if(sum == 2020){
      n1corr <- n1
      n2corr <- n2
    }
  }
}
final <- n1corr * n2corr
print(paste0("Part 1: ", final))

# Part 2 ------------------------------------------------------------------

for (i in seq_along(input)){
  n1 <- input[i]
  for (j in seq_along(input)){
    n2 <- input[j]
    for (y in seq_along(input)){
      n3 <- input[y]
      sum <- n1 + n2 + n3
      if(sum == 2020){
        n1corr <- n1
        n2corr <- n2
        n3corr <- n3
        }
    }
  }
}
final <- n1corr * n2corr *n3corr
print(paste0("Part 2: ", final))

      