#!/usr/bin/python3
''' Module of my_list
'''


class MyList(list):
    ''' Represents a MyList
    '''

    def print_sorted(self):
        '''
        prints list and but sorted
        '''
        print(sorted(self))
