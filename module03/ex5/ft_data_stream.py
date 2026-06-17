import random
import typing

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep",
           "grab", "move", "climb",
           "swim", "release", "use"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield random.choice(PLAYERS), random.choice(ACTIONS)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event_choice = random.randint(0, len(events) - 1)
        event = events[event_choice]
        events.pop(event_choice)
        yield event


if __name__ == "__main__":
    print('=== Game Data Stream Processor ===')

    events = gen_event()
    for index in range(1000):
        player, action = next(events)
        print(f"Event {index}: Player {player} did action {action}")

    list_events: list[tuple[str, str]] = []
    for _ in range(10):
        player, action = next(events)
        list_events.append((player, action))
    print(f'Built list of 10 events: {list_events}')

    for event in consume_event(list_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_events}")