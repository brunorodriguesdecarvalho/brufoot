from ui.frames.team.team_base_frame import BaseTeamFrame
from utils.team.save_team import save_team
from persistence.config import TEAM_ATTRIBUTES

class TeamEditFrame(BaseTeamFrame):
    def __init__(self, master, switch_frame, team_data, team_id):
        self.team_data = team_data
        self.team_id = team_id
        super().__init__(master, switch_frame, "Editar Time")
        self.populate_fields()

    def populate_fields(self):
        for attribute, value in zip(TEAM_ATTRIBUTES, self.team_data):
            self.entries[attribute[0]].delete(0, "end")
            self.entries[attribute[0]].insert(0, value)
        self.update_color_preview()

    def save_team(self):
        save_team(self.entries, self.return_to_team_management_menu, self.team_id)
