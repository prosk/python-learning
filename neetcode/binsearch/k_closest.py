from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid

        # l это первый индекс где arr[l] >= x
        # если все arr[l] < x то будет l = len(arr) - 1
        # если слева от него нет индексов, то просто будут браться первые k справа
        # если слева есть индекс, то надо обязательно на 1-ой итерации сравнить arr[l-1] и arr[l] 
        # так как x может быть "между ними" и мы начинаем расширения окна не с конкретного элемента
        # а находясь как бы между элементами
        # поэтому тут такой хитрый прием - окно на выходе это отрезок [l+1; r-1]
        # пусть l_find - это индекс, найденный бин поиском
        # тогда изначально ставится l = l_find-1 и r = l_find и получается 
        # что если индекс l_find-1 есть то как раз будет первое сравнение элементов
        # l = l_find-1 и r = l_find
        # и если окажется что ближе элемент слева то станет
        # l -= 1 и l = l_find-2 и r = l_find и в итоге окно будет [l_find-1; l_find-1]
        # то есть мы начнем из окна из одного элемента l_find-1
        # а если справа будет ближе то будет r += 1 и r = l_find + 1 и l = l_find-1
        # и в итоге окно станет [l_find; l_find] и мы начнем с одного элемента l_find
        # то есть начальные значения подобраны так, чтобы после первой итерации цикла
        # получить корректное окно из одного элемента, которое уже на последующих
        # итерациях будет расширяться далее
        l, r = l - 1, l
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1

        return arr[l + 1:r]
        

    def findClosestElementsBtfl(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l + k]    
    

def test():
    test_arr = [3, 7, 12, 15, 16, 16, 45, 77, 89, 90, 92, 95, 96, 96, 98]
    solution = Solution()
    ans1 = solution.findClosestElements(test_arr, 3, 10)
    ans2 = solution.findClosestElementsBtfl(test_arr, 3, 10)
    print(f"ans1 = {ans1} ans2 = {ans2}")


test()