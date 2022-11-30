# Python program to generate WordCloud

# importing all necessary modules
from traceback import print_tb
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Reads 'Youtube04-Eminem.csv' file
df = pd.read_excel('C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore.xlsx')

comment_words = ''
stopwords = set(STOPWORDS)
def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
# iterate through the csv file
# for val in df.CONTENT:
	
# 	# typecaste each val to string
# 	val = str(val)

# 	# split the value
# 	tokens = val.split()
	
# 	# Converts each token into lowercase
# 	for i in range(len(tokens)):
# 		tokens[i] = tokens[i].lower()
	
# 	comment_words += " ".join(tokens)+" "
# print(comment_words)  
wordcloud = WordCloud(
				stopwords = stopwords,background_color="white", width=3000, height=2000, max_words=500,
				min_font_size = 10).generate_from_text(df['Sub-Category'])
# word_freq = nmf.topic_word_frequency(topic_idx)
wordcloud.recolor(color_func = black_color_func)
# plot the WordCloud image					
plt.figure(figsize = (7,5), facecolor = None)
plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
