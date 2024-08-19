from fasthtml.common import *


@dataclass
class WorkExperience:
    company: str
    position: str
    date_range: str
    bullets: list[str]

    def __ft__(self):
        """ The __ft__ method renders the dataclass at runtime."""
        content = []
        content.extend([H4(B(self.position + ", " + self.company)), P(self.date_range), P(self.bullets)])
        return Div(Section(*content))
