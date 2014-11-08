from functools import wraps
import copy


def size_check(f):

    @wraps(f)
    def wrapper(*argv, **kvargs):
        f(*argv, **kvargs)
        self = argv[0]
        rows_n = len(self.rows)
        for i in range(rows_n):
            if len(self.rows[i]) != rows_n:
                return
        self.size = rows_n

    return wrapper


class Matrix:
    rows = []
    size = None

    def __init__(self, rows=None):
        self.rows = rows
        if rows is None:
            self.rows = []
        self.size = len(self.rows)

    def value(self):
        if self.size == 2:
            self.show()
            print()
            return self.rows[0][0]*self.rows[1][1]-self.rows[0][1]*self.rows[1][0]
        else:
            suma = 0
            for i in range(self.size):
                m = Matrix(copy.deepcopy(self.rows))
                m.delete_row(0)
                m.delete_column(i)
                self.show()
                print()
                print("Ucinam wiersz 0 i kolumne", i)
                v = (-1)**(i+2)*self.rows[0][i]
                suma += v*m.value()
            return suma

    @size_check
    def set_rows(self, rows):
        self.rows = rows

    @size_check
    def delete_row(self, n):
        if len(self.rows)-1 < n:
            raise Exception("Nie ma takiego indeksu wiersza")
        self.rows.remove(self.rows[n])

    @size_check
    def delete_column(self, n):
        for row in self.rows:
            row.pop(n)

    def show(self):
        for row in self.rows:
            for n in row:
                print(n, end=' ')
            print()
