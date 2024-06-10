from collections import Counter


def is_unique_chars(string):
    freq = Counter(string)
    return len(freq) == len(string)


def find_heterograms(slowa, output_file_name):
    # polish_heterograms_list = [slowo for slowo in slowa if is_unique_chars(slowo)]
    polish_heterograms_list = []

    for slowo in slowa:
        if is_unique_chars(slowo):
            polish_heterograms_list.append(slowo)

    polish_heterograms_list.sort(key=len, reverse=True)

    with open(output_file_name, mode="w", encoding="utf-8") as heterograms_file:
        heterograms_file.writelines(polish_heterograms_list)

    return polish_heterograms_list


def separate_lines(file_to_separate, output_file_name, create_file):
    # slowa = [word.strip() + '\n' for line in file_to_separate for word in line.split(",")]
    slowa = []
    for line in file_to_separate:
        for word in line.split(","):
            slowa.append(word.strip() + '\n')

    if create_file:
        with open(output_file_name, 'w', encoding='utf-8') as outfile:
            outfile.writelines(slowa)

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
