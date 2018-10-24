# Name: Quyen Do
# Homework: #11 Python
# File: wordCloud.R
# Summary: Text mining and creating wordCloud in R

# Load necessary packages
library(tm)
library(wordcloud)
library(RColorBrewer)
library(SnowballC)


#Load the text file
constitution <- readLines("11_Python/constitution.txt")

#Load the data as a corpus
docs <- Corpus((VectorSource(constitution)))

#Inspect the content of the document
#inspect(docs)

# Cleaning the text

# Convert the text to lower case
docs <- tm_map(docs, content_transformer(tolower))

# Remove numbers
docs <- tm_map(docs, removeNumbers)

# Remove common English stopwords
docs <- tm_map(docs , removeWords, stopwords("en"))

# Eliminate stopwords specifically to the text
stop.words <- c("section", "article","the","shall","may")
docs <- tm_map(docs,removeWords,stop.words)

#Remove punctuations
docs <- tm_map(docs, removePunctuation)

# Eliminate extra white spaces
docs<- tm_map(docs, stripWhitespace)

#Text stemming
#docs <- tm_map(docs, stemDocument)

# Build a term-document matrix
dtm <- TermDocumentMatrix(docs)
words_by_row <- as.matrix(dtm)
words_count <- sort(rowSums(words_by_row), decreasing = TRUE)
words_count_df <- data.frame(word=names(words_count), freq=words_count)

# Generate word cloud
set.seed(1234)
png("11_Python/R_Constituion_WordCloud.png",width = 800, height = 800)
wrdCl <- wordcloud(words=words_count_df$word,freq = words_count_df$freq, min.freq = 2,
          max.words = 200, random.order = FALSE, rot.per = 0.35,colors = brewer.pal(8,"Dark2"))
dev.off()


#References:
#http://www.sthda.com/english/wiki/text-mining-and-word-cloud-fundamentals-in-r-5-simple-steps-you-should-know