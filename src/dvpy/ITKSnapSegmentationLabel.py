class ITKSnapSegmentationLabel:

    __slots__ = ["IDX", "R", "G", "B", "A", "VIS", "MSH", "LABEL"]

    def __init__(self, IDX, R, G, B, A, VIS, MSH, LABEL):
        self.IDX = IDX
        self.R = R
        self.G = G
        self.B = B
        self.A = A
        self.VIS = VIS
        self.MSH = MSH
        self.LABEL = LABEL

    def __str__(self):
        return '{} {} {} {} {} {} {} "{}"'.format(
            self.IDX, self.R, self.G, self.B, self.A, self.VIS, self.MSH, self.LABEL
        )

    def get_rgb(self):
        return (self.R, self.G, self.B)

    def get_normalized_rgb(self):
        return (x / 255. for x in self.get_rgb())
