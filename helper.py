import os 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

def directory():
	return os.getcwd()

def assets_directory():
	return directory() + '/90kDICT32px'

def store_dataframe_to_csv(df, filename, columns):
    df.to_csv(filename, columns = columns)

def labels_to_character_map(labels):
	character_set = set()
	max_word_size = float('-inf')

	for label in labels:
		if len(label) > max_word_size:
			max_word_size = len(label)

		for c in label:
			character_set.add(c)

	# not starting at zero for usit it as padding
	count = 1

	character_map = {}
	for c in character_set:
		character_map[c] = count
		count += 1

	return character_map, max_word_size


def label_to_one_hot(label, max_word_size, character_map):
	
	one_hot = [character_map[c] for c in label]

	if len(one_hot) < max_word_size:
		padding = [0] * (max_word_size - len(one_hot))
		one_hot += padding

	return one_hot


def words_to_one_hot(labels):
	character_map, max_word_size = labels_to_character_map(labels)

	word_to_one_hot = {}

	for label in labels:
		word_to_one_hot[label] = label_to_one_hot(label, max_word_size, character_map)

	return word_to_one_hot