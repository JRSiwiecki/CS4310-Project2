from algorithms import fifo, lru, opt

TESTING_DATA_PATH = "testing-data/"
TEST_REFERENCE_STRING = "135732345051740"
FRAME_SIZES = [3, 4, 5, 6]


def testing_data_to_array():
    with open(TESTING_DATA_PATH + "TestingData.txt", "r", encoding="utf-8") as file:
        string_list = []

        for line in file.readlines():
            string_list.append(line.strip())

        return string_list


def run_fifo_tests():
    for reference_string in testing_data_to_array():
        for frame_size in FRAME_SIZES:
            fifo.run_algorithm(reference_string, frame_size)


def run_lru_tests():
    for reference_string in testing_data_to_array():
        for frame_size in FRAME_SIZES:
            lru.run_algorithm(reference_string, frame_size)


def run_opt_tests():
    for reference_string in testing_data_to_array():
        for frame_size in FRAME_SIZES:
            opt.run_algorithm(reference_string, frame_size)


def main():
    # Test to make sure algorithm works
    fifo.run_algorithm(TEST_REFERENCE_STRING, 5)
    lru.run_algorithm(TEST_REFERENCE_STRING, 5)
    opt.run_algorithm(TEST_REFERENCE_STRING, 5)

    # run_fifo_tests()
    # run_lru_tests()
    # run_opt_tests()


if __name__ == "__main__":
    main()
