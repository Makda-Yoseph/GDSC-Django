from math_operations import basic_operations, power_operation, apply_operations

# Test basic_operations
result_basic = basic_operations(10, 5)
print("Basic Operations Result:", result_basic)

# Test power_operation
result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)

# Test power_operation with modulo
result_power_modulo = power_operation(2, 3, modulo=5)
print("Power Operation with Modulo Result:", result_power_modulo)

# Test apply_operations
operations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5)),
]

result_apply = apply_operations(operations)
print("Apply Operations Result:", result_apply)
def basic_operations(a,b):
    output={}
    try:
        a=float(a)
        b=float(b)
        try:
            output['division']=a/b
        except ZeroDivisionError:
            print('\n\t_ERROR_ Division by zero is not allowed: in basic_operations\n')
        output['addition']=a+b
        output['subtration']=a-b
        output['multiplication']=a*b
    except ValueError:
        print('\n\t_ERROR_ renter only a number: in basic_operations\n')
    return output
            


def power_operation(base, exponent, **kwargs):
    try:
        base=float(base)
        exponent=float(exponent)
        powered=(base**exponent)
        modulo=0
        if 'modulo' in kwargs:
            try:
                modulo=float(kwargs['modulo'])
                powered=powered%modulo
            except ValueError:
                print('\n\t_ERROR_ please enter only a number: in power_operations, modulo\n')
        return powered
    except ZeroDivisionError:
        print('\n\t_ERROR_ division by zero is not allowed: in power_operations, modulo\n')

    
    

def apply_operations(operations):
    def each(my_tuple):
        lambda_func=my_tuple[0]
        x=my_tuple[1][0]
        y=my_tuple[1][1]
        return lambda_func(x,y)
    
    output=map(each, operations)
    return list(output)

import os
import time
'''
functions
    list_files
    created_or_modified -st_mtime- -st_ctime-
    append_time_stamp
    create_folder
    move_files
'''
def list_files():
    files=[]
    for a_file in os.scandir():
        if a_file.is_file():
            files.append(a_file.name)

    return files

def created_or_modified_24(my_file):
    my_path=os. getcwd()+'/'+my_file
    crtd=os.stat(my_path).st_ctime
    mdfd=os.stat(my_path).st_mtime
    now=time.time()

    crtd_hr=(now-crtd)/3600
    mdfd_hr=(now-mdfd)/3600
    print(str(now)+' '+str(crtd)+' '+str(crtd_hr)+' '+ my_file)

    if crtd_hr<=24 or mdfd_hr<=24:
        return True
    return False

def append_time_stamp(my_file):
    file = open(my_file, "a")
    file.write(str(time.time())+'\n')
    file.close()

def create_folder():
    import os
    path = "last_24hours"
    if os.path.isdir(path):
        print("The folder already exists")
    else:
        os.mkdir(path)


def move_files():
    cwd = os.getcwd()
    create_folder()
    files=list_files()
    for file in files:
        if created_or_modified_24(file) and file != 'main.py':
            append_time_stamp(file)
            src = os.path.join(cwd, file)
            dst = os.path.join(cwd, "last_24hours", file)
            os.rename(src, dst)

move_files()