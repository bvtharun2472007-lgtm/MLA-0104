bird(parrot).
has_wings(parrot).
can_fly(parrot).

flies(X) :-
    bird(X),
    has_wings(X),
    can_fly(X).