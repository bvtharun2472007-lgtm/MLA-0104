monkey_at(door).
box_at(window).
banana_at(ceiling).

can_push(monkey, box).
can_climb(monkey, box).
can_reach(monkey, banana).

gets_banana :-
    monkey_at(door),
    box_at(window),
    can_push(monkey, box),
    can_climb(monkey, box),
    can_reach(monkey, banana).