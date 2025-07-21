class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        sortFolders = sorted(folder)

        roots = [sortFolders[0]]
        prev = roots[0]
        for i in range(1, len(sortFolders)):
            curr = sortFolders[i]
            if not curr.startswith(prev + "/"): 
                roots.append(curr)
                prev = curr
        
        return roots
