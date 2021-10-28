


def statistics(path):
    data = []
    with open(path) as f:
        for line in f:
            fields = line.split()
            rowdata = map(float, fields)
            data.extend(rowdata)
    
    max_ = max(data)
    min_= min(data)
    average_ = sum(data)/len(data)
    
    return average_,max_,min_