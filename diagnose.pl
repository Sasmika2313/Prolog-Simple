% diagnose.pl

% Facts will be asserted dynamically from Python.

% Rule definitions:
fault(starter_faulty) :-
    engine_cranks(no),
    battery_ok(yes).

fault(battery_faulty) :-
    battery_ok(no).

fault(battery_faulty) :-
    lights_dim(yes).

fault(brake_pads_worn) :-
    brake_noise(yes).

fault(cooling_system_fault) :-
    engine_overheat(yes).

fault(fuel_system_fault) :-
    engine_power_loss(yes).

fault(fuel_system_fault) :-
    engine_cranks(yes),
    engine_cranks_but_not_start(yes).

fault(suspension_steer_issue) :-
    steering_vibrate(yes).

fault(alternator_faulty) :-
    alternator_ok(no),
    battery_ok(yes).
