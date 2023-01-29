def find_longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
            return longest_word


def main():
    words = ['dragon', 'cat', 'tiger']
    longest_word = find_longest_word(words)
    print(longest_word)


if __name__ == "__main__":
    main()
