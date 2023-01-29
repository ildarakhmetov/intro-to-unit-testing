def find_longest_word(words):
    longest_word = ''
    num_words = len(words)
    for i in range(num_words - 1):  # -1 to avoid index out of range
        if len(words[i]) > len(longest_word):
            longest_word = words[i]
    return longest_word


def main():
    words = ['cat', 'dragon', 'tiger']
    longest_word = find_longest_word(words)
    print(longest_word)


if __name__ == "__main__":
    main()
