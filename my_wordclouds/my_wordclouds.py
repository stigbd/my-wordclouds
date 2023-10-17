import os
from os import path

import matplotlib.pyplot as plt
from wordcloud import WordCloud


def create_wordcloud(inputfile: str) -> None:
    # get data directory
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, inputfile)).read()

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # the matplotlib way:
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("prodapp.png", bbox_inches="tight")
    plt.show()
    plt.close()
