"""
Load the cornell movie dialog corpus.
"""
MOVIE_LINES_FIELDS = ["lineID", "characterID", "movieID", "character", "text"]
MOVIE_CONVERSATIONS_FIELDS = ["character1ID", "character2ID", "movieID", "utteranceIDs"]


class CornellData:
    """
    """

    def __init__(self, dirName):
        """
        Args:
            dirName (string): directory where to load the corpus
        """
        self.lines = {}
        self.conversations = []

        self.lines = self.loadLines(dirName + "movie_lines.txt", MOVIE_LINES_FIELDS)
        self.conversations = self.loadConversations(dirName + "movie_conversations.txt", MOVIE_CONVERSATIONS_FIELDS)

        # print('Loaded: %d lines, %d conversations' % (len(self.lines), len(self.conversations)))
        # TODO: Cleaner program !!

    def loadLines(self, fileName, fields):
        """
        Args:
            fileName (str): file to load
            fields (set<str>): fields to extract
        Return:
            dict<??>: the extracted fields for each line
        """
        lines = {}

        with open(fileName, 'r', encoding='iso-8859-1') as f:
            for line in f:
                values = line.split(" +++$+++ ")

                # Extract fields
                lineObj = {}
                for i, field in enumerate(fields):
                    lineObj[field] = values[i]

                lines[lineObj['lineID']] = lineObj

        return lines

    def loadConversations(self, fileName, fields):
        """
        Args:
            fileName (str): file to load
            fields(set<str>): fields to extract
        Return:
            dict<??>: the extracted fields for each line
        """
        conversations = []

        with open(fileName, 'r', encoding='iso-8859-1') as f:
            for line in f:
                values = line.split(" +++$+++ ")

                # Extract fields
                convObj = {}
                for i, field in enumerate(fields):
                    convObj[field] = values[i]

                lineIds = convObj["utteranceIDs"][2:-3].split("', '")

                # print(convObj["utteranceIDs"])
                # for lineId in lineIds:
                    # print(lineId, end=' ')
                # print()

                # Reassemble lines
                convObj["lines"] = []
                for lineId in lineIds:
                    convObj["lines"].append(self.lines[lineId])

                conversations.append(convObj)

        return conversations

    def get_conversation(self):
        return self.conversations
