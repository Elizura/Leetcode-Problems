    def totalFruit(self, fruits: List[int]) -> int:
            max_len=0
            left=0
            fruit_type=0
            counter=Counter()
            for right in range (len(fruits)):
                counter[fruits[right]]+=1

                if counter[fruits[right]]==1:
                    fruit_type+=1
                while fruit_type>2:
                    counter[fruits[left]] -= 1
                    if counter[fruits[left]]==0:
                        fruit_type-=1
                    left+=1
                cur_len=right-left+1
                max_len=max(max_len,cur_len)
            return max_len
