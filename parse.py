def tojiStateChecker(bool):
    enabledStatement = 'armed and ready'
    disabledStatement = 'disabled. Toji is dead for the third time'

    if bool == 1:
        return enabledStatement
    elif bool == 0:
        return disabledStatement
    else:
        return 
