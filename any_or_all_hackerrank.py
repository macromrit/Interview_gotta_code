total_input = int(input())
main_ans = [True if x>=0 else False for x in list(map(int, str(input()).strip().split()))]
print(True) if False not in main_ans and str(total_input)[::-1]==str(total_input) else print(False)
