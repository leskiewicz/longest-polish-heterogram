from collections import Counter


def is_unique_chars(string):
    freq = Counter(string)
    return len(freq) == len(string)


def heterograms_in_slowa(slowa):
    polish_heterograms_list = []

    for idx, slowo in enumerate(slowa):
        if is_unique_chars(slowo):
            polish_heterograms_list.append(slowo)

    polish_heterograms_list.sort(key=len, reverse=True)

    heterograms_file = open("heterogramy.txt", mode="w", encoding="utf-8")
    for slowo in polish_heterograms_list:
        heterograms_file.write(slowo)
    heterograms_file.close()

    longest_heterogram = polish_heterograms_list[0]
    print('Najdłuższy heterogram wg słownika slowa.txt: ' + longest_heterogram)
    print('Długość słowa wynosi: ' + str(len(longest_heterogram) - 1))


# def heterograms_in_odmiany(odmiany):
#     polish_heterograms_odmiany_list = []
#
#     for idx, slowo in enumerate(odmiany):
#         if is_unique_chars(slowo):
#             polish_heterograms_odmiany_list.append(slowo)
#
#     polish_heterograms_odmiany_list.sort(key=len, reverse=True)
#
#     heterograms_odmiany_file = open("heterogramy_odmiana.txt", mode="w", encoding="utf-8")
#     for slowo in polish_heterograms_odmiany_list:
#         heterograms_odmiany_file.write(slowo)
#     heterograms_odmiany_file.close()
#
#     longest_heterogram_odmiany = polish_heterograms_odmiany_list[0]
#     print('Najdłuższy heterogram wg słownika slowa.txt: ' + longest_heterogram_odmiany)
#     print('Długość słowa wynosi: ' + str(len(longest_heterogram_odmiany) - 1))


# def convert_odmiany(odmiany_to_convert):
#     converted_odmiany = []
#     for idx, slowo in enumerate(odmiany_to_convert):
#         slowo.splitlines(True)
#         converted_odmiany.append(slowo)
#
#     converted_odmiany_file = open("converted_odmiany.txt", mode="w", encoding="utf-8")
#     for slowo in converted_odmiany:
#         converted_odmiany_file.write(slowo)
#     converted_odmiany_file.close()
#
#     return converted_odmiany


if __name__ == '__main__':
    slowa = open("slowa.txt", mode="r", encoding="utf-8")
    heterograms_in_slowa(slowa)

    # odmiany = open("odmiany.txt", mode="r", encoding="utf-8")
    # odmiany = convert_odmiany(odmiany)
    # heterograms_in_odmiany(odmiany)



# TODO: Add słowotwórstwo as future possibility
# TODO: Fix converting - now it is removing lines and has to little words
# TODO: Refactor this shitty code