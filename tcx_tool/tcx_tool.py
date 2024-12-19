
with open('./run_new.tcx', 'w') as write:
    with open('./run.tcx', 'r') as run:

        for line in run:
            for tag in ['DistanceMeters', 'Speed']:
                if (i := line.find('<'+ tag + '>')) != -1:
                    num = float(line[i + len(tag) + 2 : line.index('</' + tag)])
                    num *= 1.609
                    line = line[:i] + '<' + tag + '>' + str(num) + '</' + tag + '>' + '\n'
            write.write(line)
