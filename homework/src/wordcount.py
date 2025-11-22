# obtain a list of files in the input directory

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_count_words import write_count_words


def main():
    ## mover a la función read_all_lines
    all_lines = read_all_lines()

    ### mover a la función preprocess_lines
    all_lines = preprocess_lines(all_lines)

    ### mover "split_into_words"
    words = split_into_words(all_lines)

    ### mover "count_words"
    counter = count_words(words)

    ### mover "write_count_words"
    write_count_words(counter)


if __name__ == "__main__":
    main()