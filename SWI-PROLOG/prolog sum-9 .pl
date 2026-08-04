edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, d, 1).
edge(c, e, 3).
edge(d, g, 2).
edge(e, g, 1).

heuristic(a, 7).
heuristic(b, 5).
heuristic(c, 4).
heuristic(d, 2).
heuristic(e, 1).
heuristic(g, 0).

best_first(Start, Goal) :-
    search([Start], Goal).

search([Goal|_], Goal) :-
    write('Goal Reached: '),
    write(Goal), nl.

search([Current|Path], Goal) :-
    findall(H-Next,
            (edge(Current, Next, _),
             heuristic(Next, H)),
            Children),
    sort(Children, Sorted),
    get_nodes(Sorted, Nodes),
    search(Nodes, Goal).

get_nodes([], []).
get_nodes([_-Node|T], [Node|R]) :-
    get_nodes(T, R).