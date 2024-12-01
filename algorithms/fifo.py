def run_algorithm(reference_string, frame_size):
    page_frame = []
    fault_track = ""

    print("Running FIFO on", reference_string, "with frame size", frame_size)

    for page in reference_string:

        # If page already in page_frame, no need to change anything
        if page in page_frame:
            fault_track += " "
            print(page, "-", page_frame)
            continue

        # Otherwise, if page_frame is already full, need to remove
        # the current first element in the frame
        if len(page_frame) >= frame_size:
            page_frame.pop(0)

        # Then we can add our new page
        page_frame.append(page)
        fault_track += "X"

        print(page, "-", page_frame, end=" ")

        if fault_track[-1] == "X":
            print("X")

    fault_count = fault_track.count("X")

    print("FIFO yields", fault_count, "page faults")
    return fault_count
