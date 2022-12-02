import os

data_path = "./multi_files/"
file_path = "./"
multi_names = os.listdir(data_path)

start_flag = False
with open(file_path + "graph.mtx", "w") as fo:
    for id in range(len(multi_names)):
        if multi_names[id].count(".mtx"):
            with open(data_path + multi_names[id], "r") as f:
                print("process: " + multi_names[id])
                for line in f:
                    args = line.strip().split()
                    if '%' in line:
                        continue
                    if len(args) == 3 and start_flag is False:
                        fo.write(line)
                        start_flag = True
                    else:
                        fo.write(line)
