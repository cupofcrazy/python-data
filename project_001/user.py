class Query:
    # (fav) will have to be an array of items
    def __init__(self, fav):
        self.count = 1
        self.fav = fav
        self.queries = len(self.fav)
        self.list = []

    def query_time(self):
        print('Q&A TIME...!')
        while self.count <= self.queries:
            for f in self.fav:
                q = input('Question ' + str(self.count) + ': What is your favourite ' + f + '? ')
                self.list.append(q)
                self.count += 1

    def _print_fav(self):
        print('\nHere are the list of your favourites...')
        for y in self.list:
            print(y)

#Here is a (fav)
my_list = ['book', 'movie', 'game']

#new instance of the class 'Query'
que = Query(my_list)

#Initialize
que.query_time()
que._print_fav()



