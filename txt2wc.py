from wordcloud import WordCloud
import matplotlib.pyplot as plt

def word_map_from_file(file_name):
    # initialize list of words we'll learn from the file
    word_list = []

    with open(file_name) as f:
        for line in f:
            # assume words are separated by a space
            new_words = line.split(' ')
            for w in new_words:
                # make sure all words are lower case
                word_list.append(w.lower())

    wordcloud = WordCloud(width=480, height=480).generate(' '.join(word_list))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()


word_map_from_file('sample.txt')
