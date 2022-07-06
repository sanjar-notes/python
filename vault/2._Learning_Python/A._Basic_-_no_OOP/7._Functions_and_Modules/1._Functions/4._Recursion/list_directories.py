import os

# # 1 print the contents of the current directory
# listing = os.walk('.')
# for root, directories, files in listing:
#     print('Root:',root)
#     print('Directories:')
#     for d in directories:
#         print('\t',d)
#     print('Files:')
#     for f in files:
#         print('\t',f)


def f(a):
    n=a
    def g(n):
        # nonlocal Name
        if n == 0:
            return
        print(n, Name)
        g(n - 1)
    Name = 1
    if 1==1:
        g(n)
# f(6)


# 2 function to print about all folders and subfolders
def list_directories(s):    # the helper function

    def dir_list(d):    # the recursive function, prints everything
        # nonlocal tab_stop
        files = os.listdir(d)
        nonlocal tab_stop
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print('\t' * tab_stop, 'Directory' + f)
                tab_stop += 1
                return
                dir_list(current_dir)
                tab_stop-=1
            # else:
            #     print('\t'*tab_stop + f)

    # working starts here
    tab_stop = '0'
    # anchor and recursive call
    if os.path.exists(s):
        print('Directory listing of', s)
        dir_list(s)

# list_directories(os.curdir)


# def h():
#     for i in range(10):
#         1 == 1
#     print(i)

# h()
