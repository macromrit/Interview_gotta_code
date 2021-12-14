def designerPdfViewer(h, word):
    """pdf viewer

    Args:
        h (list): an array a.k.a list in python consistin of values mapped to lower case alphas via index
        word (str): a string with len>=10
    """
    x = list()
    for letter in word:
        x.append(h[ord(letter)-97])
    return max(x)*len(x)
