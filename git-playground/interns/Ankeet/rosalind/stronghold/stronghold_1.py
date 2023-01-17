from decor import timing
#Problem 1
@timing
def func1(s):
      print(s.count("A"), s.count("G"), s.count("C"), s.count("T"))

@timing
def func2(needed_str):
	main_dict = {}
	for x in needed_str:
		if x in main_dict.keys():
			main_dict[x] += 1
		else:
			main_dict[x] = 1
	#print(main_dict.values())
	vals = ["A", "G", "C", "T"]
	for x in vals:
		if x is not vals[-1]:
			print(main_dict[x], end=" ")
		else:
			print(main_dict[x])

@timing
def func3(s):
	print(*map(s.count, "AGCT"))

__all__ = [func1, func2, func3]