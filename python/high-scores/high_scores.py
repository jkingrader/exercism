def latest(scores):
    return scores[len(scores)-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores_copy = scores.copy()
    scores_copy.sort()
    scores_copy.reverse()
    return scores_copy[0:min(len(scores_copy),3)]

