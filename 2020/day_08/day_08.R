library(stringr)


input <- read.delim("day_08/input_08.txt", header = FALSE)
input <- as.matrix(input)


# Part 1 ------------------------------------------------------------------

checkline <- vector(mode="numeric", length=length(input))
acc_count <- 0 
i <- 1

while (2 %in% checkline != TRUE) {
  line_type <- as.character(unlist(strsplit(input[i], " "))[1])
  line_val <- as.numeric(as.character(unlist(strsplit(input[i], " "))[2]))
  
  if(line_type == "acc"){
    checkline[i] <- checkline[i] + 1
    if(2 %in% checkline){
      break
    }
    acc_count <- acc_count + line_val

    i <- i + 1
  }
  if(line_type == "jmp"){
    checkline[i] <- checkline[i] + 1
    if(2 %in% checkline){
      break
    }
    i <- i + line_val 
  }
  if(line_type == "nop"){
    checkline[i] <- checkline[i] + 1
    if(2 %in% checkline){
      break
    }
    i <- i + 1
  }

}

while (checkline[i] < 1) {
  print(i)
  line_type <- as.character(unlist(strsplit(input[i], " "))[1])
  line_val <- as.numeric(as.character(unlist(strsplit(input[i], " "))[2]))
  
  if(line_type == "acc"){
    checkline[i] <- checkline[i] + 1
    acc_count <- acc_count + line_val
    
    i <- i + 1
  }
  if(line_type == "jmp"){
    checkline[i] <- checkline[i] + 1
    i <- i + line_val 
  }
  if(line_type == "nop"){
    checkline[i] <- checkline[i] + 1
    i <- i + 1
  }
  
}
print(paste0("Part 1: ", acc_count))


