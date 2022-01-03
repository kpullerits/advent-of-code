library(stringr)


# Part 1 ------------------------------------------------------------------

input <- readLines("day_06/input_06.txt", n = -1)
input <- as.matrix(input)
inputlist <- as.list(input)

j <- 1
groups <- vector(mode="character", length=length(input))
groups_merge <- vector(mode="character", length=length(input))
group <- input[1]
group <- c("")
list <- list()
list <- append(list,group)

my_list <- list() 
list_index = 1
current_vector = c() 


for (i in 1:length(input)) {
  if(input[i] == ""){
    my_list[[list_index]] <- current_vector
    current_vector <- c()
    list_index <- list_index +1
    
  }else{
    current_vector <- append(current_vector, input[i])
  }
}
my_list[[list_index]] <- current_vector

counter <- c()
for (j in 1:length(my_list)){
  group <- unlist(my_list[[j]])
  current_set <- unlist(strsplit(group[1], ""))
  for (i in 1:length(group)) {
    current_set <- union(current_set, unlist(strsplit(group[i], "")))
  }
  counter[j] <- length(current_set)
}
print(paste0("Part 1: ", sum(counter)))


# Part 2 ------------------------------------------------------------------

counter <- c()
for (j in 1:length(my_list)){
  group <- unlist(my_list[[j]])
  current_set <- unlist(strsplit(group[1], ""))
  for (i in 1:length(group)) {
    current_set <- intersect(current_set, unlist(strsplit(group[i], "")))
  }
  counter[j] <- length(current_set)
}
print(paste0("Part 2: ", sum(counter)))

