def perm(selected, rem, perms):
	if len(rem) == 0:
		perms.append(selected)

	for c in rem:
		new_rem = list(rem)
		new_rem.remove(c)
		new_selected = list(selected)
		new_selected.append(c)
		perm(new_selected, new_rem, perms)


def run(input_str):
	perms = []
	perm([], list(input_str), perms)
	print perms

run('abc')
