import pytvmaze
from datetime import datetime


def tvMazeCreator(items, mainChoice, tvName=None):
    if tvName is not None:
        return pytvmaze.show_search(str(tvName))
    else:
        return pytvmaze.show_search(items[int(mainChoice)].name)[int(mainChoice)]


def tvMazeDate(tvMaze):
    currentDate = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
    try:
        nextReleaseDate = datetime.strptime(tvMaze.next_episode.airdate, '%Y-%m-%d')
        deltaDate = (nextReleaseDate - currentDate).days
    except:
        nextReleaseDate = "---"
        deltaDate = "---"
    return deltaDate, nextReleaseDate


def extractTV(tvdbID, pItems):
    if tvdbID is not None:
        if len(pItems) > 0:
            for item in pItems:
                if item.externals['thetvdb'] == tvdbID:
                    return item
        else:
            return pItems