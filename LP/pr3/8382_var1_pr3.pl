/*
	Бригада 1 группы 8382 - Кузина, Кулачкова, Мирончик
	
	Задание: Реализуйте, используя рекурсию и отсечение, цикл с постусловием (типа repeat <оператор> until <условие>).
*/

:- dynamic(variables/2).
set(Var, Val) :- (\+variables(Var, _), !; retract(variables(Var, _))), assertz(variables(Var, Val)).
get(Var, Val) :- variables(Var, Val).

test :- start_counter(10).

start_counter(StartCount) :- 
    set(i, StartCount),
    repeat, 
    get(i, Count), 
    format('Count ~d\n', [Count]), 
    set(i, Count - 1), 
    (Count =< 1, !; fail).