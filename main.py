# cleaning the text
# 1) create a text file and take text from it
# 2) convert letters into lowercase ("Apple" is not equals to "apple")
# 3) Remove punctuation ,.?/"" etc etc.
import matplotlib.pyplot as plt
from collections import Counter
import string

text = open("read.txt",encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

# in above method we have 3 params in maketrans(param1,param2,param3)
# param1 is str and it takes text to be replaced
# param2 is str and it takes text to be replaced with
# param3 is str and it takes list of characters to be deleted


print(cleaned_text)
tokenized_words = cleaned_text.split()
#print(tokenized_words)


stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

#print(final_words)




emotion_list = []
with open("emotions.txt","r") as file:
    for line in file:
        clear_line = line.replace("\n",'').replace(',','').replace("'",'').strip()
        #print(clear_line)
        word,emotion = clear_line.split(":")
        #print("word :"+word + " "+ "Emotion :"+ emotion)

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)

w = Counter(emotion_list)
print(w)


fig,ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()