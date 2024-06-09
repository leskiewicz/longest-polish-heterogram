from collections import Counter


def is_unique_chars(string):
    freq = Counter(string)
    return len(freq) == len(string)


def find_heterograms(slowa, output_file_name):
    polish_heterograms_list = []

    for idx, slowo in enumerate(slowa):
        if is_unique_chars(slowo):
            polish_heterograms_list.append(slowo)

    polish_heterograms_list.sort(key=len, reverse=True)

    heterograms_file = open(output_file_name, mode="w", encoding="utf-8")
    for slowo in polish_heterograms_list:
        heterograms_file.write(slowo)
    heterograms_file.close()

    return polish_heterograms_list


def separate_lines(file_to_separate, output_file_name, create_file):
    slowa = []
    for line in file_to_separate:
        split_lines = line.split(",")
        for word in split_lines:
            stripped_word = word.strip()
            stripped_word = stripped_word + '\n'
            slowa.append(stripped_word)

    if create_file:
        with open(output_file_name, 'w', encoding='utf-8') as outfile:
            for slowo in slowa:
                outfile.write(slowo)

    return slowa


def info(heterograms_list):
    longest_heterogram = heterograms_list[0].replace('\n', '')
    print('Najdłuższy heterogram w pliku: ' + longest_heterogram)
    print('Długość słowa wynosi: ' + str(len(longest_heterogram)))


if __name__ == '__main__':
    slowa = open("slowa.txt", mode="r", encoding="utf-8")
    heterogramy_bez_odmian = find_heterograms(slowa, "heterogramy.txt")
    info(heterogramy_bez_odmian)

    odmiany = separate_lines(open("slowa_odmiany.txt", mode="r", encoding="utf-8"), "converted_odmiany.txt", False)
    # odmiany = open("converted_odmiany.txt", mode="r", encoding="utf-8")
    heterogramy_odmiany = find_heterograms(odmiany, "heterogramy_odmiany.txt")
    info(heterogramy_odmiany)

# TODO: Add słowotwórstwo as future possibility
# TODO: Refactor this code
