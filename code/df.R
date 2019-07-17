library(magrittr)

df = 
  data.frame(
    one   = rnorm(5),
    two   = rnorm(5),
    three = rnorm(5)
  )

df

df$one %>% sum
