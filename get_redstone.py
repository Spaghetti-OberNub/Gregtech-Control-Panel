from config import frequency_path_name, redstone_sample_path

class FrequencyList:
    def __init__(self, path):
        self.frequency_dict = {}

        with open(path, "r", encoding="utf-8") as f:
            for index, line in enumerate(f.readlines()):
                self.frequency_dict[str(index)] = line

    def __getitem__(self, item):
        try:
            return self.frequency_dict[item]
        except KeyError:
            print(f"KeyError for Key:'{item}' and Dict:{self.frequency_dict}")
    

class RedstoneSignal:
    def __init__(self, redstone_id):
        self.active_redstone_id = redstone_id
        self.active_redstone_name = RedstoneSignal.get_name_from_id(self.active_redstone_id)

    @staticmethod
    def get_name_from_id(redstone_id):
        if type(redstone_id) == int:
            redstone_id = str(redstone_id)

        return RedstoneSignal.frequency_name_dict[redstone_id]
            
    @staticmethod
    def get_active_redstone_list():
        with open(redstone_sample_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        redstone_list = []

        for line in lines:
            if line.strip() == "-":
                output_string = ""
                continue
            try:
                frequency = int(line)
                redstone_list.append(RedstoneSignal(frequency))
            except ValueError:
                print(f"Frequency not Found: {line.strip()}")
                redstone_list.append(RedstoneSignal(None))
                continue
            
        return redstone_list
    
    frequency_name_dict = FrequencyList(frequency_path_name)