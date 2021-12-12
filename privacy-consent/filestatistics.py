
import statistics

def filestatistics(path):
    data = []
    with open(path) as f:
        for line in f:
            fields = line.split()
            rowdata = map(float, fields)
            data.extend(rowdata)
    
    max_ = max(data)
    max_ = round(max_, 2)

    min_= min(data)
    min_ = round(min_, 2)


    average_ = sum(data)/len(data)
    average_ = round(average_, 2)


    std_ = statistics.stdev(data)
    std_ = round(std_, 2)


    return average_,max_,min_,std_