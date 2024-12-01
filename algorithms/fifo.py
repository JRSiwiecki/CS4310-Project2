def run_algorithm(reference_string, frame_size):
    page_frame = []
    fault_track = ""

    print(reference_string)

    for page in reference_string:
        if page in page_frame:
            fault_track += " "
            print(page_frame)
            continue

        if len(page_frame) >= frame_size:
            page_frame.pop(0)

        page_frame.append(page)
        fault_track += "X"

        print(page_frame, end=" ")
        if fault_track[-1] == "X":
            print("X")

    fault_count = 0
    for char in fault_track:
        if char == "X":
            fault_count += 1

    print("FIFO yields", fault_count, "page faults with frame size", frame_size)
