import os
import string
import random
import cv2

#TODO Dataset formats
"""
-Partitions
	- TestLines.lst
	- TrainLines.lst
	- ValidationLines.lst
Transcript
	- file.txt >> content is the transcript, file name is the image name
Images
	- images of the data

"""


def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

def write_line(file_name, line):
    with open(file_name, "a") as f:
        f.write(line + "\n")


def get_filenames(ff):
	with open(ff) as f:
		lines = f.readlines()
	lines = [line.strip() for line in lines]
	names = [line.split(" ")[0][:-4] for line in lines]
	transcriptions = [line.split(" ")[1:] for line in lines]
	train_counter = 0
	valid_counter = 0
	test_counter = 0
	cc = 0
	for i in range(len(names)):
		print(cc)
		cc += 1
		# train files
		
		if train_counter < 6000:
			train_counter += 1
			write_line("/home/gabir/Desktop/Active_Projects/Deeplance/David OCR project/handwritten-text-recognition/raw/gabir/Partitions/TrainLines.txt", names[i])
			# Transcriptions
			write_line("/home/gabir/Desktop/Active_Projects/Deeplance/David OCR project/handwritten-text-recognition/raw/gabir/Transcriptions/" + names[i] + ".txt", " ".join(transcriptions[i]).upper())
		elif valid_counter < 2500:
			valid_counter += 1
			write_line("/home/gabir/Desktop/Active_Projects/Deeplance/David OCR project/handwritten-text-recognition/raw/gabir/Partitions/ValidationLines.txt", names[i])
			# Transcriptions
			write_line("/home/gabir/Desktop/Active_Projects/Deeplance/David OCR project/handwritten-text-recognition/raw/gabir/Transcriptions/" + names[i] + ".txt", " ".join(transcriptions[i]).upper())

		else:
			write_line("/home/gabir/Desktop/Active_Projects/Deeplance/David OCR project/handwritten-text-recognition/raw/gabir/Partitions/TestLines.txt", names[i])
			# Transcriptions
			write_line("/home/gabir/Desktop/Active_Projects/Deeplance/David OCR project/handwritten-text-recognition/raw/gabir/Transcriptions/" + names[i] + ".txt", " ".join(transcriptions[i]))


		

        
get_filenames("/home/gabir/Desktop/Active_Projects/Deeplance/David OCR project/handwritten-text-recognition/gt_capital.txt")

# imgs_dir = "/home/gabir/Desktop/Active_Projects/Deeplance/David OCR project/handwritten-text-recognition/out"
# new_imgs = "/home/gabir/Desktop/Active_Projects/Deeplance/David OCR project/handwritten-text-recognition/new_out"

# for line in os.listdir(imgs_dir):
#     name = get_random_string(15)
#     print(name)
#     print("line: ", line)
#     img = cv2.imread(os.path.join(imgs_dir, line))
#     cv2.imwrite(os.path.join(new_imgs, name + ".jpg"), img)
#             # os.rename(self.data_directory + line, self.output_dir + name + ".jpg")
#             # file_name = line.split('_')[1][:-4]
#     gt = line.split("_")[0][::-1]
#     print("gt: ", gt)
#     # new_gt, new_char_lst = self.check_gt(gt, new_char_lst)
#     # threshold = 120
#     new_line = name + ".jpg" + " " + gt
#     write_line(new_line)
#     break