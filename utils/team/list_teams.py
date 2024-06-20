from persistence.team_dao import get_teams_from_db
from persistence.config import TEAM_ATTRIBUTES

def list_teams(self, tk):
    teams = get_teams_from_db()
    self.team_ids = []  # Limpa a lista de IDs antes de atualizar
    # Limpar a tabela antes de preencher com os dados atualizados
    for item in self.tree.get_children():
        self.tree.delete(item)
    if not teams:
        self.tree.insert("", tk.END, values=("Não há registros.",) * len(TEAM_ATTRIBUTES))
    else:
        for team in teams:
            self.team_ids.append(team['id'])  # Armazena o ID do time
            values = [team[attr[0]] for attr in TEAM_ATTRIBUTES]
            item_id = self.tree.insert("", tk.END, values=values)

            # Aplicar cor de fundo
            primary_color = team.get('primary_color', '#FFFFFF')  # Padrão para branco se não houver cor
            secondary_color = team.get('secondary_color', '#000000')  # Padrão para preto se não houver cor
            self.tree.tag_configure(primary_color, background=primary_color)
            self.tree.tag_configure(secondary_color, foreground=secondary_color)

            self.tree.item(item_id, tags=(primary_color, secondary_color))
