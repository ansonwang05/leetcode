class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        totalMatch = playerP = trainerP = 0
        sortPlayers = sorted(players) 
        sortTrainers = sorted(trainers) 
        
        while (playerP != len(players)) and (trainerP != len(trainers)):
            if sortPlayers[playerP] <= sortTrainers[trainerP]: 
                totalMatch += 1
                playerP += 1 
                trainerP += 1 
            else: 
                trainerP += 1
        
        return totalMatch
