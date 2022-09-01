from dataclasses import dataclass
import yaml


@dataclass
class Screen:
    title: str
    width: int
    height: int
    fps: int


@dataclass
class Color:
    rgb: tuple[int, int, int]


@dataclass
class Colors:
    yellow: Color
    red: Color
    white: Color


@dataclass
class Game:
    screen: Screen
    colors: Colors
    intro_count: int
    score: list[int, int]
    round_over_cooldown: int
    music: str
    background: str
    victory: str
    font: str


@dataclass
class Fighter:
    size: int
    scale: int
    offset: list[int, int]
    weapon_sound: str
    image: str
    animation_steps: list[int]


@dataclass
class Fighters:
    warrior: Fighter
    wizard: Fighter


@dataclass
class Config:
    game: Game
    fighters: Fighters


def load_config(path: str = None) -> Config:
    with open(file=f"{path}/settings.yaml", mode="r") as f:
        params = yaml.load(f, Loader=yaml.FullLoader)

    return Config(
        game=Game(
            screen=Screen(
                title=params["game"]["screen"]["title"],
                width=params["game"]["screen"]["width"],
                height=params["game"]["screen"]["height"],
                fps=params["game"]["screen"]["fps"],
            ),
            colors=Colors(
                yellow=Color(rgb=params["game"]["colors"]["yellow"]),
                red=Color(rgb=params["game"]["colors"]["red"]),
                white=Color(rgb=params["game"]["colors"]["white"]),
            ),
            intro_count=params["game"]["intro_count"],
            score=params["game"]["score"],
            round_over_cooldown=params["game"]["round_over_cooldown"],
            music=params["game"]["music"],
            background=params["game"]["background"],
            victory=params["game"]["victory"],
            font=params["game"]["font"],
        ),
        fighters=Fighters(
            warrior=Fighter(
                size=params["fighters"]["warrior"]["size"],
                scale=params["fighters"]["warrior"]["scale"],
                offset=params["fighters"]["warrior"]["offset"],
                weapon_sound=params["fighters"]["warrior"]["weapon_sound"],
                image=params["fighters"]["warrior"]["image"],
                animation_steps=params["fighters"]["warrior"]["animation_steps"],
            ),
            wizard=Fighter(
                size=params["fighters"]["wizard"]["size"],
                scale=params["fighters"]["wizard"]["scale"],
                offset=params["fighters"]["wizard"]["offset"],
                weapon_sound=params["fighters"]["wizard"]["weapon_sound"],
                image=params["fighters"]["wizard"]["image"],
                animation_steps=params["fighters"]["wizard"]["animation_steps"],
            ),
        ),
    )


# a = load_config()
# print(a)
