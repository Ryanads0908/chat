
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	林宥呈_wordz_count = 0
	諭筠_wordz_count = 0
	林宥呈_sticker_count = 0
	諭筠_sticker_count = 0
	林宥呈_image_count = 0
	諭筠_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '林宥呈':
			if s[2] == '貼圖':
				林宥呈_sticker_count += 1
			elif s[2] == '圖片':
				林宥呈_image_count += 1
			else:
				for m in s[2:]:
					林宥呈_wordz_count += len(m)
		elif name == '諭筠':
			if s[2] == '貼圖':
				諭筠_sticker_count += 1
			elif s[2] == '圖片':
				諭筠_image_count += 1
			else:
				for m in s[2:]:
					諭筠_wordz_count += len(m)
	print('林宥呈說了', 林宥呈_wordz_count, '個字')
	print('林宥呈傳了', 林宥呈_sticker_count, '個貼圖')
	print('林宥呈傳了', 林宥呈_image_count, '張圖片')

	print('諭筠說了', 諭筠_wordz_count, '個字')
	print('諭筠傳了', 諭筠_sticker_count, '個貼圖')
	print('諭筠傳了', 諭筠_image_count, '張圖片')
		# print(s[2:])
	

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('[LINE]yy.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main()