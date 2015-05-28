import re




def words(inputs):
    sep = re.compile(r"\b(?:\w*\-)?[A-Za-z]+\b")
    serrate = re.findall(sep, inputs)
    if len(serrate) == 0:
        return None
    else:
        return serrate


def phone_number(inputs):
    nums = re.match(r'\(?(\d{3})\)?[\-\.]?\s*?(\d{3})[\-\.]?(\d{4})', inputs)
    if nums == None:
        return None
    else:
        return {"area_code":nums.group(1),
         "number": nums.group(2) +"-"+ nums.group(3)}

def money(inputs):
    pass

def zip(inputs):
    pass

def date(inputs):
    pass
