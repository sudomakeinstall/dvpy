from dvpy import determine_number_of_files
import os


def test_determine_number_of_files(tmpdir):

    pattern = "%d.png"

    for N in [0, 1, 2, 25, 100]:
        directory = os.path.join(str(tmpdir), "test_determine_number_of_files_%d" % (N))
        helper(directory, pattern, N)


def helper(directory, pattern, N):

    os.makedirs(directory, exist_ok=True)
    for i in range(N):
        f_name = os.path.join(str(directory), str(pattern % (i)))
        with open(f_name, "w") as f:
            f.write("contents")

    assert determine_number_of_files(directory, pattern) == N
