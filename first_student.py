def find_longest_word(words):
    longest_word = ''
    for word in words:
        longest_word = word
    return longest_word


def main():
    words = ['tiger', 'cat', 'dragon']
    longest_word = find_longest_word(words)
    print(longest_word)


if __name__ == "__main__":
    main()
