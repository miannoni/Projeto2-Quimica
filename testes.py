diction = {"S": "a"}

def conversor(variavel, var_do_tipo_certo):
	x = 0
	print(str(type(var_do_tipo_certo))[str(type(var_do_tipo_certo)).find("'") + 1:-2])
	print(str(variavel))
	exec("x += " + str(type(var_do_tipo_certo))[str(type(var_do_tipo_certo)).find("'") + 1:-2] + "(" + str(variavel) + ")")
	return x

a = conversor("1.5", float())
print(a)
print(type(a))
