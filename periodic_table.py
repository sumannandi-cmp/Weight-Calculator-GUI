import tkinter as tk

class PeriodicTable(tk.Toplevel):
    def __init__(self, parent, index):
        super().__init__(parent)
        self.index = index
        self.parent = parent
        self.geometry('1000x500')
        self.attributes('-topmost', 'true')
        self.build()

    def build(self):
        elements = [
    # Alkali metals
    ('H', '1.008', 1, 0, '#f7ff98'),
    ('Li', '6.94', 2, 0, '#f7ff98'),
    ('Na', '22.99', 3, 0, '#f7ff98'),
    ('K', '39.098', 4, 0, '#f7ff98'),
    ('Rb', '85.468', 5, 0, '#f7ff98'),
    ('Cs', '132.91', 6, 0, '#f7ff98'),
    ('Fr', '223.00', 7, 0, '#f7ff98'),

    # Alkaline earth metals
    ('Be', '9.0122', 2, 1, '#fdf6a7'),
    ('Mg', '24.305', 3, 1, '#fdf6a7'),
    ('Ca', '40.078', 4, 1, '#fdf6a7'),
    ('Sr', '87.62', 5, 1, '#fdf6a7'),
    ('Ba', '137.33', 6, 1, '#fdf6a7'),
    ('Ra', '226.03', 7, 1, '#fdf6a7'),

    # Transition metals
    ('Sc', '44.956', 4, 2, '#f8b7b7'),
    ('Y', '88.906', 5, 2, '#f8b7b7'),
    ('La >|', '138.91', 6, 2, '#f8b7b7'),
    ('Ac >|', '227.03', 7, 2, '#f8b7b7'),

    ('Ti', '47.867', 4, 3, '#f8b7b7'),
    ('Zr', '91.224', 5, 3, '#f8b7b7'),
    ('Hf', '178.49', 6, 3, '#f8b7b7'),
    ('Rf', '267.00', 7, 3, '#f8b7b7'),

    ('V', '50.942', 4, 4, '#f8b7b7'),
    ('Nb', '92.906', 5, 4, '#f8b7b7'),
    ('Ta', '180.95', 6, 4, '#f8b7b7'),
    ('Ha', '268.00', 7, 4, '#f8b7b7'),

    ('Cr', '51.996', 4, 5, '#f8b7b7'),
    ('Mo', '95.95', 5, 5, '#f8b7b7'),
    ('W', '183.84', 6, 5, '#f8b7b7'),
    ('Sg', '269.00', 7, 5, '#f8b7b7'),

    ('Mn', '54.938', 4, 6, '#f8b7b7'),
    ('Tc', '98', 5, 6, '#f8b7b7'),
    ('Re', '186.21', 6, 6, '#f8b7b7'),
    ('Bh', '270.00', 7, 6, '#f8b7b7'),

    ('Fe', '55.845', 4, 7, '#f8b7b7'),
    ('Ru', '101.07', 5, 7, '#f8b7b7'),
    ('Os', '190.23', 6, 7, '#f8b7b7'),
    ('Hs', '277.00', 7, 7, '#f8b7b7'),

    ('Co', '58.933', 4, 8, '#f8b7b7'),
    ('Rh', '102.91', 5, 8, '#f8b7b7'),
    ('Ir', '192.22', 6, 8, '#f8b7b7'),
    ('Mt', '278.00', 7, 8, '#f8b7b7'),

    ('Ni', '58.693', 4, 9, '#f8b7b7'),
    ('Pd', '106.42', 5, 9, '#f8b7b7'),
    ('Pt', '195.08', 6, 9, '#f8b7b7'),

    ('Cu', '63.546', 4, 10, '#f8b7b7'),
    ('Ag', '107.87', 5, 10, '#f8b7b7'),
    ('Au', '196.97', 6, 10, '#f8b7b7'),

    ('Zn', '65.38', 4, 11, '#f8b7b7'),
    ('Cd', '112.41', 5, 11, '#f8b7b7'),
    ('Hg', '200.59', 6, 11, '#f8b7b7'),

    # Group 13
    ('B', '10.81', 2, 12, 'lime'),
    ('Al', '26.982', 3, 12, 'Light Blue'),
    ('Ga', '69.723', 4, 12, 'Light Blue'),
    ('In', '114.82', 5, 12, 'Light Blue'),
    ('Ti', '204.38', 6, 12, 'Light Blue'),

    # Group 14
    ('C', '12.011', 2, 13, 'lime'),
    ('Si', '28.085', 3, 13, 'lime'),
    ('Ge', '72.630', 4, 13, 'Light Blue'),
    ('Sn', '118.71', 5, 13, 'Light Blue'),
    ('Pb', '207.20', 6, 13, 'Light Blue'),

    # Group 15
    ('N', '14.007', 2, 14, 'lime'),
    ('P', '30.974', 3, 14, 'lime'),
    ('As', '74.922', 4, 14, 'lime'),
    ('Sb', '121.76', 5, 14, 'Light Blue'),
    ('Bi', '208.98', 6, 14, 'Light Blue'),

    # Group 16
    ('O', '15.999', 2, 15, 'lime'),
    ('S', '32.06', 3, 15, 'lime'),
    ('Se', '78.971', 4, 15, 'lime'),
    ('Te', '127.60', 5, 15, 'lime'),
    ('Po', '209.00', 6, 15, 'Light Blue'),

    # Group 17
    ('F', '18.998', 2, 16, 'lime'),
    ('Cl', '35.45', 3, 16, 'lime'),
    ('Br', '79.904', 4, 16, 'lime'),
    ('I', '126.90', 5, 16, 'lime'),
    ('At', '210.00', 6, 16, 'lime'),

    # Noble gases
    ('He', '4.003', 1, 17, '#e6c1f0'),
    ('Ne', '20.18', 2, 17, '#e6c1f0'),
    ('Ar', '39.948', 3, 17, '#e6c1f0'),
    ('Kr', '83.798', 4, 17, '#e6c1f0'),
    ('Xe', '131.29', 5, 17, '#e6c1f0'),
    ('Rn', '222.00', 6, 17, '#e6c1f0'),

    # Lanthanides (Bottom Row)
    ('>| Ce', '140.12', 11, 3, 'light goldenrod'),
    ('Pr', '140.91', 11, 4, 'light goldenrod'),
    ('Nd', '144.24', 11, 5, 'light goldenrod'),
    ('Pm', '145.00', 11, 6, 'light goldenrod'),
    ('Sm', '150.36', 11, 7, 'light goldenrod'),
    ('Eu', '151.96', 11, 8, 'light goldenrod'),
    ('Gd', '157.25', 11, 9, 'light goldenrod'),
    ('Tb', '158.93', 11, 10, 'light goldenrod'),
    ('Dy', '162.50', 11, 11, 'light goldenrod'),
    ('Ho', '164.93', 11, 12, 'light goldenrod'),
    ('Er', '167.26', 11, 13, 'light goldenrod'),
    ('Tm', '168.93', 11, 14, 'light goldenrod'),
    ('Yb', '173.05', 11, 15, 'light goldenrod'),
    ('Lu', '174.97', 11, 16, 'light goldenrod'),
    
    # Actinides (row 12)
    ('>| Th', '232.04', 12, 3, '#ffd3c9'),
    ('Pa', '231.04', 12, 4, '#ffd3c9'),
    ('U', '238.03', 12, 5, '#ffd3c9'),
    ('Np', '237.00', 12, 6, '#ffd3c9'),
    ('Pu', '244.00', 12, 7, '#ffd3c9'),
    ('Am', '243.00', 12, 8, '#ffd3c9'),
    ('Cm', '247.00', 12, 9, '#ffd3c9'),
    ('Bk', '247.00', 12, 10, '#ffd3c9'),
    ('Cf', '251.00', 12, 11, '#ffd3c9'),
    ('Es', '252.00', 12, 12, '#ffd3c9'),
    ('Fm', '257.00', 12, 13, '#ffd3c9'),
    ('Md', '258.00', 12, 14, '#ffd3c9'),
    ('No', '259.00', 12, 15, '#ffd3c9'),
    ('Lr', '262.00', 12, 16, '#ffd3c9'),
]

        for symbol, weight, row, col, color in elements:
            if symbol:  
                tk.Button(
                    self,
                    text=symbol,
                    width=5,
                    height=2,
                    bg=color,
                    command=lambda s=symbol, w=weight: self.write(self.index, s, w)
                ).grid(row=row, column=col)
            else:
                tk.Label(self, text="").grid(row=row, column=col)

    def write(self, a, b, c):
        self.destroy()
        self.parent.n2[int(a)].set(b)
        self.parent.n3[int(a)].set(c)
