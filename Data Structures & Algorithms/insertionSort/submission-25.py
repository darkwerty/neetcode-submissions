# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        length = len(pairs)

        if length == 0:
            return []

        pair_changes = []
        pair_changes.append(pairs.copy())

        # We check each pair of the pairs array starting from the second element
        # Then we look at the element to its left and see if its bigger than actual element
        # If it is, we have to insert the lower pair there and push the rest to the right
        for i in range(1, length):
            if pairs[i].key < pairs[i-1].key:
                posInsertion = 0
                
                while posInsertion < i and pairs[i].key >= pairs[posInsertion].key: posInsertion += 1

                tmp = pairs[i] # We store this
                print(tmp)
                for j in range(i, posInsertion, -1):
                    pairs[j] = pairs[j-1]                 

                pairs[posInsertion] = tmp


                # We have found first element that is greater than the element that we have to insert
                #pairs[posInsertion:i+1] = [pairs[i]] + pairs[posInsertion:i]


            pair_changes.append(pairs.copy())

        return pair_changes