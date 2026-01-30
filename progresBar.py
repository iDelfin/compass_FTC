import time

def progressBar(part:int, total:int, length:int=50, sub_title:str="") -> str:
    frac = part/total
    completed = int(frac * length)
    missing = length - completed
    bar = f"{sub_title}\n[{'#'* completed}{'-'*missing}]{frac:.2%}"
    return bar