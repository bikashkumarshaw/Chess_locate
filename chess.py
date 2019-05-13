import argparse

class Chess(object):
    def run(self):
        self.args = self._define_args()
        self.reachable_index()

    def get_neighbours(self, index):
        row, column = index
        child_index = [(row-2, column-1), (row-2, column+1), \
        (row+2, column-1), (row+2, column+1), (column-2, row-1), \
        (column-2, row+1), (column+2, row-1), (column+2, row+1)]

        reachable_index = []
        row_order, column_order = map(int, self.args.matrix_order.split(","))
        for each_index in child_index:
            child_row, child_colum = each_index
            if child_row <0 or child_row > row_order-1 or child_colum < 0 or child_colum > column_order-1:
                continue
            reachable_index.append(each_index)

        return reachable_index

    def reachable_index(self):
        row_order, column_order = map(int, self.args.matrix_order.split(","))
        marked = [[0 for i in range(column_order)] for j in range(row_order)]
        start_row, start_column = map(int, self.args.start_index.split(","))
        start_index = (start_row, start_column)
        queue = [start_index]
        while(queue!=[]):
            row, column = queue.pop(0)
            if not marked[row][column]:
                neighbours = self.get_neighbours(start_index)
                marked[row][column] = 1
                if neighbours:
                    queue.extend(neighbours)

        find_row_index, find_column_index = map(int, self.args.search_index.split(","))
        if marked[find_row_index][find_column_index]:
            print "The index {} can be reached fom {} with knight".format(self.args.search_index, self.args.start_index)
        else:
            print "The index {} can not be reached fom {} with knight".format(self.args.search_index, self.args.start_index)

    def _define_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--matrix-order", help="specify the order of the matrix with comma separation eg. 3,3", type=str)
        parser.add_argument("--search-index", help="specify the index of the matrix to be searched with comma separation eg. 2,1", type=str)
        parser.add_argument("--start-index", help="specify the index of the matrix to start the search from with comma separation eg. 1,3", type=str)
        return parser.parse_args()

if __name__=="__main__":
    Chess().run()
