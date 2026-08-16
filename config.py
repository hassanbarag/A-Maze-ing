#!/usr/bin/env python3

from dataclasses import dataclass
from mazegen.style import getValue


@dataclass
class Config:
    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: int | None = None
    algorithm: str | None = None


def parse_bool(value: str) -> bool:
    return value.strip().lower() == "true"


def parse_tuple(value: str) -> tuple[int, int]:
    x, y = value.split(",")
    return int(x), int(y)


def load_config(path: str) -> Config:
    data: dict[str, str] = {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith('#'):
                    continue
                try:
                    key, value = line.split("=", 1)
                except ValueError:
                    raise ValueError(f"Invalid config line: {line}")

                data[key.strip()] = value.strip()

    except FileNotFoundError:
        raise ValueError(f"Config file not found: {path}")

    config = Config(
        width=int(getValue("WIDTH", path)),
        height=int(getValue("HEIGHT", path)),
        entry=parse_tuple(data["ENTRY"]),
        exit=parse_tuple(getValue("EXIT", path)),
        output_file=data["OUTPUT_FILE"],
        perfect=parse_bool(data["PERFECT"]),
        seed=int(getValue("SEED", path)),
    )

    validate_config(config)
    return config


def validate_config(config: Config) -> None:

    if config.width <= 0:
        raise ValueError("WIDTH must be greater than 0")

    if config.height <= 0:
        raise ValueError("HEIGHT must be greater than 0")

    entry_x, entry_y = config.entry
    exit_x, exit_y = config.exit

    # ENTRY
    if not (
        0 <= entry_x < config.width
        and
        0 <= entry_y < config.height
    ):
        raise ValueError(f"Invalid ENTRY: {config.entry}")

    # EXIT
    if not (
        0 <= exit_x < config.width
        and
        0 <= exit_y < config.height
    ):
        raise ValueError(f"Invalid EXIT: {config.exit}")

    # SAME CELL
    if config.entry == config.exit:
        raise ValueError("ENTRY and EXIT must be different")

    if (
        config.seed is not None
        and
        config.seed < 0
    ):
        raise ValueError("SEED must be positive")
