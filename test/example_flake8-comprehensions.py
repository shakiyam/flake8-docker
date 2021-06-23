list(x + 1 for x in range(10))  # C400
set(x + 1 for x in range(10))  # C401
dict((x, str(x)) for x in range(10))  # C402
set([x + 1 for x in range(10)])  # C403
dict([(x, x) for x in range(10)])  # C404
set([])  # C405
dict([])  # C406
tuple()  # C408
tuple([])  # C409
list([])  # C410
list([x + 1 for x in range(10)])  # C411
list(sorted([2, 3, 1]))  # C413
list(list(''))  # C414
set([2, 3, 1][::-1])  # C415
[x for x in range(5)]  # C416

# C400 Unnecessary generator - rewrite as a list comprehension.
# C401 Unnecessary generator - rewrite as a set comprehension.
# C402 Unnecessary generator - rewrite as a dict comprehension.
# C403 Unnecessary list comprehension - rewrite as a set comprehension.
# C404 Unnecessary list comprehension - rewrite as a dict comprehension.
# C405 Unnecessary <list/tuple> literal - rewrite as a set literal.
# C406 Unnecessary <list/tuple> literal - rewrite as a dict literal.
# C408 Unnecessary <dict/list/tuple> call - rewrite as a literal.
# C409 Unnecessary <list/tuple> passed to tuple()
#      - (remove the outer call to tuple()/rewrite as a tuple literal).
# C410 Unnecessary <list/tuple> passed to list()
#      - (remove the outer call to list()/rewrite as a list literal).
# C411 Unnecessary list call - remove the outer call to list().
# C413 Unnecessary <list/reversed> call around sorted().
# C414 Unnecessary <list/reversed/set/sorted/tuple> call
#      within <list/set/sorted/tuple>().
# C415 Unnecessary subscript reversal of iterable
#      within <reversed/set/sorted>().
# C416 Unnecessary <list/set> comprehension - rewrite using <list/set>().
