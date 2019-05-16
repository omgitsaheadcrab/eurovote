from flask_table import Table, Col

class Statistics():
    def __init__(self):
        self.max_score = 0
        self.min_score = 0
        self.max_song = 0
        self.min_song = 0
        self.max_outfit = 0
        self.min_outfit = 0
        self.max_performance = 0
        self.min_performance = 0

class StatsTable(Table):
    name = Col('Name')
    total_score = Col('Total')
    song_score = Col('Song')
    outfit_score = Col('Outfit')
    performance_score = Col('Performance')
    border = True
    classes = ['table', 'table-striped', 'table-bordered', 'table-condensed']
