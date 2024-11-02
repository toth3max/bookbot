bookFile = "./books/frankenstein.txt"

def main():
	with open(bookFile) as f:
		file_contents = f.read().lower()
		book_dict = {}

		for char in file_contents:
			if char.isalpha():
				if char in book_dict:
					book_dict[char] += 1
				else:
					book_dict[char] = 1

		char_list = [{"character": char, "count": count} for char, count in book_dict.items()]

		char_list.sort(key=lambda x: x["count"], reverse=True)

		#words = file_contents.split()
		#print(len(words))
		#print(book_dict)
		print(f"Charater fequencies: ", char_list)
main()
