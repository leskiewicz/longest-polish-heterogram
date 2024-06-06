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

    # longest_heterogram = polish_heterograms_list[0]
    # print('Najdłuższy heterogram wg słownika slowa.txt: ' + longest_heterogram)
    # print('Długość słowa wynosi: ' + str(len(longest_heterogram) - 1))


def separate_lines(file_to_separate):
    slowa = []
    for line in file_to_separate:
        slowa.extend([word.strip() for word in line.split(',')])

    with open('converted_odmiany_test.txt', 'w', encoding='utf-8') as outfile:
        for slowo in slowa:
            outfile.write(slowo + '\n')
    return slowa


if __name__ == '__main__':
    slowa = open("slowa.txt", mode="r", encoding="utf-8")
    # find_heterograms(slowa, "heterogramy.txt")

    odmiany = open("slowa_odmiany_test.txt", mode="r", encoding="utf-8")
    odmiany = separate_lines(odmiany)
    # find_heterograms(odmiany, "heterogramy_odmiany.txt")

# TODO: Add słowotwórstwo as future possibility
# TODO: Fix converting - now it is removing lines and has to little words
# TODO: Refactor this shitty code
