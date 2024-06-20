from ui.frames.personalize.team_base_frame import BaseTeamFrame
from utils.team.save_team import save_team

class TeamAddFrame(BaseTeamFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master, switch_frame, "Adicionar Time")

    def save_team(self):
        save_team(self.entries, self.return_to_team_management_menu)