# System

# Third Party
import pandas as pd

# Internal


def aha_segments():
    return pd.DataFrame(
        [
            [0, "G", ""],
            [1, "B", "Ant"],
            [2, "B", "AntSep"],
            [3, "B", "InfSep"],
            [4, "B", "Inf"],
            [5, "B", "InfLat"],
            [6, "B", "AntLat"],
            [7, "M", "Ant"],
            [8, "M", "AntSep"],
            [9, "M", "InfSep"],
            [10, "M", "Inf"],
            [11, "M", "InfLat"],
            [12, "M", "AntLat"],
            [13, "A", "Ant"],
            [14, "A", "Sep"],
            [15, "A", "Inf"],
            [16, "A", "Lat"],
            [17, "P", ""],
        ],
        columns=["SegmentID", "Slice", "Segment"],
    )
