TESTING_DATA_PATH = "testing-data/"


def testing_data_to_array():
    testing_data_list = []

    for i in range(3):
        with open(
            TESTING_DATA_PATH + "TestingData-" + str(i) + ".txt", "r", encoding="utf-8"
        ) as file:
            string_list = []

            for line in file.readlines():
                string_list.append(line.strip())

            testing_data_list.append(string_list)

    return testing_data_list


def main():
    print(testing_data_to_array())


if __name__ == "__main__":
    main()
