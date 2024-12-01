def run_algorithm(reference_string, frame_size):
    page_frame = []
    fault_track = ""

    print("Running OPT on", reference_string, "with frame size", frame_size)

    for current_index, page in enumerate(reference_string):

        # If page is already in the frame, no page fault
        if page in page_frame:
            fault_track += " "
            print(page, "-", page_frame)
            continue

        fault_track += "X"

        # If the frame is full, replace the optimal page
        if len(page_frame) >= frame_size:
            furthest_usage = -1
            page_to_replace = None

            for frame_page in page_frame:
                # Find the next occurrence of the current frame page
                if frame_page in reference_string[current_index + 1 :]:
                    next_usage = reference_string[current_index + 1 :].index(frame_page)
                else:
                    next_usage = float("inf")  # Page won't be used again

                # Select the page with the furthest future usage
                if next_usage > furthest_usage:
                    furthest_usage = next_usage
                    page_to_replace = frame_page

            page_frame.remove(page_to_replace)

        page_frame.append(page)

        print(page, "-", page_frame, end=" ")
        if fault_track[-1] == "X":
            print("X")

    fault_count = fault_track.count("X")
    print("OPT yields", fault_count, "page faults")
