class Team(object):

    def _init_(self, relativeIds, owner, active):

        self.relativeIds = relativeIds
        self.owner = owner
        self.active = active

    # this must be done in order.
    def load_next_season(self,scores):

        self.scores = scores
        # self.wins = wins
        # self.losses = losses
        # self.points_for = points_for
        # self.points_against = points_against