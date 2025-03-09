words = """apple and banana one apple one banana
          a red apple and a green apple"""

words_list = words.split()
width = 10
print (f"{'apple: ':<{width}} - {words_list.count('apple'):>{width-7}}\n"
       f"{'and: ':<{width}} - {words_list.count('and'):>{width-7}}\n"
       f"{'banana: ':<{width}} - {words_list.count('banana'):>{width-7}}\n"
       f"{'one: ':<{width}} - {words_list.count('one'):>{width-7}}\n"
       f"{'a: ':<{width}} - {words_list.count('a'):>{width-7}}\n"
       f"{'red: ':<{width}} - {words_list.count('red'):>{width-7}}\n"
       f"{'green: ':<{width}} - {words_list.count('green'):>{width-7}}")