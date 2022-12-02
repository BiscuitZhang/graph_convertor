import os

data_path = "./multi_files/"
multi_names = os.listdir(data_path)

for id in range(len(multi_names)):
    start_flag = False
    edges = {}
    v_record = {}
    edges_record = []
    dimacs_filename = data_path + multi_names[id].strip(".mtx")
    if multi_names[id].count(".mtx"):
        with open(data_path + multi_names[id], "r") as f:
            with open(dimacs_filename, "w") as fo:
                for line in f:
                    args = line.strip().split()
                    if '%' in args:
                        continue
                    if len(args) == 3 and start_flag is False:
                        v_num_1, v_num_2, e_num = args
                        start_flag = True

                    # unweighted
                    if len(args) == 2:
                        u, v = args
                        #  drop self-loops
                        if u == v:
                            continue

                        #  drop repeated
                        if (u, v) in edges.keys() and (v, u) in edges.keys():
                            continue
                        else:
                            v_record[u] = 1
                            v_record[v] = 1
                            edges[(u, v)] = 1
                            edges[(v, u)] = 1
                            edges_record.append("e {} {}\n".format(u, v))

                    # weighted
                    if len(args) == 3 and start_flag is True:
                        u, v, weight = args
                        #  drop self-loops
                        if u == v:
                            continue

                        #  drop repeated
                        if (u, v) in edges.keys() and (v, u) in edges.keys():
                            continue
                        else:
                            v_record[u] = 1
                            v_record[v] = 1
                            edges[(u, v)] = 1
                            edges[(v, u)] = 1
                            edges_record.append("e {} {}\n".format(u, v))

                fo.write("p edge {} {}\n".format(len(v_record), len(edges_record)))
                for i in range(len(edges_record)):
                    fo.write(edges_record[i])
            print("finished" + dimacs_filename)
