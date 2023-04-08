def func_args(*args):
    if not args:
        print('vazio')
    else:
        print(f'categoria = {args[0]}')
        print(f'page = {args[1]}')



func_args('serie', 1 )
func_args()