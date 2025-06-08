def get_reactor_sample(path):
    with open(path,"r",encoding="utf-8") as f:
        lines = f.readlines()

    output_dict = {}

    if lines[0].strip() == "false":
        output_dict["isRunning"] = "Not Running"
    elif lines[0].strip() == "true":
        output_dict["isRunning"] = "Running"

    output_dict["item_name"] = lines[1].strip()

    for i in range(8):
        output_dict[f"{i}-durability"] = lines[i+2].strip()

    return output_dict
        



    