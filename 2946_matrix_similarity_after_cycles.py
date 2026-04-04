class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        temp=mat
        def shiftleft(arr):
            temp=arr[:]
            for i in range(len(arr)):
                arr[i]=temp[(i+k)%len(arr)]
                

        def shiftright(arr):
            temp=arr[:]
            for i in range(len(arr)):
                arr[i]=temp[(i-k)%len(arr)]


        res=[i[:] for i in mat]
        for i in range(len(mat)):
            if i%2==0:
                shiftleft(mat[i])

            if i%2==1:
                shiftright(mat[i])
        print(mat)
        print(res)
        return mat==res
