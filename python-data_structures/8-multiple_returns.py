#!/usr/bin/python3
def multiple_returns(sentence):
    ext = len(sentence)
    if len(sentence) == 0:
        return ext, None
    else:
        primer = sentence[0]
        return ext, primer


if __name__ == '__main__':
    multiple_returns(sentence)
