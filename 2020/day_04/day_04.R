library(stringr)
library(stringi)

test <- readLines("day_04/input_04.txt", n = -1)

input <- as.matrix(test)

j <- 1
passports <- vector(mode="character", length=length(input))
passports_merge <- vector(mode="character", length=length(input))
for (i in 1:length(input)) {
  if(input[i] == ""){
    j <- j +1
  }
  
  passports_merge[j] <- paste(passports_merge[j],input[i], sep = " ")
  }
passports_merge <- as.matrix(passports_merge)

passports_merge_filt <- as.matrix(passports_merge[passports_merge != ""])

count <- 0
for (i in 1:length(passports_merge_filt)) {
  pwline <- as.character(passports_merge_filt[i])
  byr <- 0
  iyr <- 0
  eyr <- 0
  hgt <- 0
  hcl <- 0
  ecl <- 0
  pid <- 0
  cid <- 0
  if(stri_detect_fixed(pwline, "byr")){
    byr <- 1
  }
  if(stri_detect_fixed(pwline, "iyr")){
    iyr <- 1
  }
  if(stri_detect_fixed(pwline, "eyr")){
    eyr <- 1
  }
  if(stri_detect_fixed(pwline, "hgt")){
    hgt <- 1
  }
  if(stri_detect_fixed(pwline, "hcl")){
    hcl <- 1
  }
  if(stri_detect_fixed(pwline, "ecl")){
    ecl <- 1
  }
  if(stri_detect_fixed(pwline, "pid")){
    pid <- 1
  }
  if(stri_detect_fixed(pwline, "cid")){
    cid <- 1
  }
  present <- byr + iyr + eyr + hgt + hcl + ecl + pid
  if(present > 6)
    count <- count + 1
}
print(paste0("Part 1: ", count))


# Part 2 ------------------------------------------------------------------


j <- 1
passports <- vector(mode="character", length=length(input))
passports_merge <- vector(mode="character", length=length(input))
for (i in 1:length(input)) {
  if(input[i] == ""){
    j <- j +1
  }
  
  passports_merge[j] <- paste(passports_merge[j],input[i], sep = " ")
}
passports_merge <- as.matrix(passports_merge)

passports_merge_filt <- as.matrix(passports_merge[passports_merge != ""])

count <- 0
for (i in 1:length(passports_merge_filt)) {
  pwline <- as.character(passports_merge_filt[i])
  byr <- 0
  iyr <- 0
  eyr <- 0
  hgt <- 0
  hcl <- 0
  ecl <- 0
  pid <- 0
  cid <- 0
  if(stri_detect_fixed(pwline, "byr")){
    pwline2 <- unlist(strsplit(pwline, " "))
    for (q in 1:length(pwline2)) {
      if(stri_detect_fixed(pwline2[q], "byr")){
        byr_val <- as.numeric(as.character(unlist(strsplit(pwline2[q], ":"))[2]))
        if(byr_val >= 1920 && byr_val <= 2002){
          byr <- 1
        }else{
          byr <- 0
        }
        
      }
    }
  }
  if(stri_detect_fixed(pwline, "iyr")){
    pwline2 <- unlist(strsplit(pwline, " "))
    for (w in 1:length(pwline2)) {
      if(stri_detect_fixed(pwline2[w], "iyr")){
        iyr_val <- as.numeric(as.character(unlist(strsplit(pwline2[w], ":"))[2]))
        if(iyr_val >= 2010 && iyr_val <= 2020){
          iyr <- 1
        }else{
          iyr <- 0
        }
        
      }
    }
  }
  if(stri_detect_fixed(pwline, "eyr")){
    pwline2 <- unlist(strsplit(pwline, " "))
    for (e in 1:length(pwline2)) {
      if(stri_detect_fixed(pwline2[e], "eyr")){
        eyr_val <- as.numeric(as.character(unlist(strsplit(pwline2[e], ":"))[2]))
        if(eyr_val >= 2020&& eyr_val <= 2030){
          eyr <- 1
        }else{
          eyr <- 0
        }
        
      }
    }
  }
  if(stri_detect_fixed(pwline, "hgt")){
    pwline2 <- unlist(strsplit(pwline, " "))
    for (r in 1:length(pwline2)) {
      if(stri_detect_fixed(pwline2[r], "hgt")){
        hgt_val <- as.character(unlist(strsplit(pwline2[r], ":"))[2])
      }
    }
    if(stri_detect_fixed(hgt_val, "cm")){
      hgt_val_num <- as.numeric(str_remove(hgt_val, "cm"))
      if(hgt_val_num >= 150 && hgt_val_num <= 193){
        hgt <- 1
      }else{
        hgt <- 0
      }
    }
    if(stri_detect_fixed(hgt_val, "in")){
      hgt_val_num <- as.numeric(str_remove(hgt_val, "in"))
      if(hgt_val_num >= 59 && hgt_val_num <= 76){
        hgt <- 1
      }else{
        hgt <- 0
      }
    }
    
  }
  if(stri_detect_fixed(pwline, "hcl")){
    pwline2 <- unlist(strsplit(pwline, " "))
    for (t in 1:length(pwline2)) {
      if(stri_detect_fixed(pwline2[t], "hcl")){
        hcl_val <- as.character(unlist(strsplit(pwline2[t], ":"))[2])
      }
    }
    if(stri_detect_fixed(hcl_val, "#") && nchar(hcl_val) == 7){
      hcl <- 1
    }else{
      hcl <- 0
    }
  }
  if(stri_detect_fixed(pwline, "ecl")){
    pwline2 <- unlist(strsplit(pwline, " "))
    for (y in 1:length(pwline2)) {
      if(stri_detect_fixed(pwline2[y], "ecl")){
        ecl_val <- as.character(unlist(strsplit(pwline2[y], ":"))[2])
      }
    }
    if (ecl_val == "amb" | ecl_val == "blu" | ecl_val == "brn" | ecl_val == "gry" | ecl_val == "grn" | ecl_val == "hzl" | ecl_val == "oth"){
      ecl <- 1
    }else{
      ecl <- 0
    }
    
  }
  if(stri_detect_fixed(pwline, "pid")){
    pwline2 <- unlist(strsplit(pwline, " "))
    for (u in 1:length(pwline2)) {
      if(stri_detect_fixed(pwline2[u], "pid")){
        pid_val <- as.character(unlist(strsplit(pwline2[u], ":"))[2])
      }
    }
    if(nchar(pid_val) == 9){
      pid <- 1
    }else{
      pid <- 0
    }
    
  }
  if(stri_detect_fixed(pwline, "cid")){
    cid <- 1
  }
  present <- byr + iyr + eyr + hgt + hcl + ecl + pid
  if(present > 6)
    count <- count + 1
}
print(paste0("Part 2: ", count))





