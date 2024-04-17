###################################################################################################################
# modify_dataframe is meant to add functionality to pandas dataframes
###################################################################################################################

def add_dict_to_dataframe(dictionary,dataframe):
	""" Input a dictionary and the dataframe:
	Returns the dataframe with the dictionaries added.
	"""
	df_dictionary = pd.DataFrame.from_dict(dictionary)
	output = pd.concat([dataframe, df_dictionary], ignore_index=True)
	return output

def add_multiple_dict_to_dataframe(dictionary_list,dataframe):
	""" Input a list of dictionaries and the dataframe:
	Returns the dataframe with the dictionaries added.
	"""
	output = dataframe
	for i in dictionary_list:
		output = add_dict_to_dataframe(i,output)
	return output




if __name__ == "__main__":
	import pandas as pd


	test_og_dict = {"Name":["Jen","John","Kate"], "Age": [42,4,105]}
	test_other_dict = {"Name":["Cal","Tim","Bill"], "Age": [2,34,15]}
	test_other_dict2 = {"Name":["Syd","Jojo","Chad"], "Age": [91,7,39]}
	test_other_dict3 = {"Name":["Nick","Noel","Lorry"], "Age": [19,23,40]}
	test_df = pd.DataFrame.from_dict(test_og_dict)

	#print(test_df.head())

	new_test_df = add_dict_to_dataframe(test_other_dict,test_df)
	print(new_test_df.head())

	new_test_df_list = [test_other_dict,test_other_dict2,test_other_dict3]

	new_test_df2 = add_multiple_dict_to_dataframe(new_test_df_list,test_df)

	print(new_test_df2)