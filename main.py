from algorithms import fifo

TESTING_DATA_PATH = "testing-data/"
FRAME_SIZES = [3, 4, 5, 6]


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
    for testing_data in testing_data_to_array():
        for reference_string in testing_data:
            for frame_size in FRAME_SIZES:
                fifo.run_algorithm(reference_string, frame_size)


if __name__ == "__main__":
    main()
