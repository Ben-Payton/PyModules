

class species_out_file:

    def __init__(self,file_name:str):
        
        self.species_list = []
        self.numbers_list = []
        self.dict_vals = {}

        with open(file_name,'r') as file:
            file_list = file.readlines()
        
        for i in file_list:
            if "#" in i:
                self.species_list.append(i.split())
                del self.species_list[-1][0]
            else:
                numbers_list.append(i.split)
                for i in range(len(self.numbers_list[-1])):
                    self.numbers_list[-1][i] = int(self.numbers_list[-1][i])
        
        self.dict_vals = self.add_keys()
        for i in range(len(self.species_list)):
            self.add_values()

    def check_keys(self,key,dict):
        return key in dict.keys()

    def find_longest_key_length(self,dict):
        longest_key = 0 
        for i in dict.keys():
            length =len(dict(i))
            if length > longest_key:
                longest_key = length
        return longest_key
    
    def add_keys(self):
        for i in self.species_list:
            for key in i:
                if not check_keys(self.dict_vals,key)
        return dict
    
    def add_values(self):
        for i in self.dict_vals.keys():
            if i in self.species_list:
                self.dict_vals[i].append(self.numbers_list[self.species_list.index(i)])
            else:
                self.dict_vals[i].append(0)

    