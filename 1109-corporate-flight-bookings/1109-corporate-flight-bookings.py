class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        '''
        first phase
        swipe line arr = [] of size n + 1
        pref_arr = []
        for q in query:
            firs, last, seat = 
            swipe_first and swipe last + 1 with seat
        for i in len(1, swipe_arr):
            construct prefix arr                
        '''
        swipe = [0] * (n + 1)
        for start, last, seats in bookings:
            start -= 1            
            swipe[start] += seats
            swipe[last] -= seats
            
        pref_arr = swipe.copy()
        for i in range(1, len(pref_arr)):
            pref_arr[i] += pref_arr[i - 1]
            
        return pref_arr[:-1]