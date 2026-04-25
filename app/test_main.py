import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        # --- базові ---
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),

        # --- перший людський рік ---
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),

        # --- другий людський рік ---
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 28, [2, 2]),

        # --- третій людський рік ---
        (28, 29, [3, 2]),
        (32, 34, [4, 4]),

        # --- великі значення ---
        (100, 100, [
            2 + (100 - 24) // 4,
            2 + (100 - 24) // 5
        ]),

        # --- граничні негативні ---
        (-1, -1, [0, 0]),
        (-10, 5, [0, 0]),
        (5, -10, [0, 0]),
    ],
    ids=[
        "0 years → 0 human",
        "1 year → 0 human",
        "14 years → 0 human",

        "15 years → 1 human",
        "16 years → 1 human",
        "23 years → 1 human",

        "24 years → 2 human",
        "25 years → 2 human",
        "27/28 years → 2 human",

        "28/29 years → 3 human",
        "32/34 years → 4 human",

        "large numbers → correct scaling",

        "negative both → 0",
        "negative cat → 0",
        "negative dog → 0",
    ]
)
def test_get_human_age(cat_age, dog_age, expected) -> None:
    assert get_human_age(cat_age, dog_age) == expected
