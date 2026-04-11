# solution from https://yandex.ru/jobs/interview/algorithms
# тут более простые (но эквивалентные if) по сравнению с generate_brackets
def generate_parentheses(n):
   result = []
   
   def backtrack(s="", open_count=0, close_count=0):
       if len(s) == 2 * n:
           result.append(s)
           print(s)
           return
           
       if open_count < n:
           backtrack(s + "(", open_count + 1, close_count)
           
       if close_count < open_count:
           backtrack(s + ")", open_count, close_count + 1)
   
   backtrack()
   return result

generate_parentheses(4)