def get_sample(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output = []

    for line in lines:
        line = list(line)
        for i, letter in enumerate(line):
            if letter == "§":
                line.pop(i)
                line.pop(i)

        output.append("".join(line))

    stored_eu = []
    total_capacity = []
    used_capacity = ""
    eu_input = " "
    eu_output = " "

    for line in output:
        if line[:11] == "EU Stored: ":
            stored_eu.append(line[11:].strip())

        if line[:15] == "Used Capacity: ":
            used_capacity = line[15:].strip()

        if line[-17:] == "(last 5 seconds)\n":
            if line[7] == "I":
                eu_input = line[11:-18].strip()
            elif line[7] == "O":
                eu_output = line[12:-18].strip()

        if line[:16] == "Total Capacity: ":
            total_capacity.append(line[16:].strip())

    if len(stored_eu) == 0:
        return " "
        
    output_dict = {
        "eu_stored": stored_eu,
        "used_capacity": used_capacity,
        "eu_input": eu_input,
        "eu_output": eu_output,
        "total_capacity": total_capacity
    }

    return output_dict
