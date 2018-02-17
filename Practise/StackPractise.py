def is_comment(item):
    return isinstance(item,str) and item.startswith('#')

def execute(program):

    #finds whether all lines are comment or not
    while program :
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else:
        print("All lines are comments")
        return

    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e :

            pending = []
            pending.append(result)
        else:
            pending.append(item)
    else:
        print(pending)

    print("finished")


if __name__ == '__main__' :
    import operator
    program = list( reversed
                    (( '#A short program to add some constants' ,
                      5,
                      2,
                      operator.add,
                      3,
                       operator.mul)))

    execute(program)