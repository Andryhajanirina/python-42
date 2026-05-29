#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/04 15:19:44 by andry-ha            #+#    #+#            #
#   Updated: 2026/05/22 15:48:08 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


class ScoreAnalyticsError(Exception):
    pass


class NoScoresProvidedError(ScoreAnalyticsError):
    def __init__(self) -> None:
        message = "No scores provided. "\
                  "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        super().__init__(message)


class NonNumericScoreError(ScoreAnalyticsError):
    def __init__(self, score_str: str) -> None:
        message = f"Invalid parameter '{score_str}'"
        super().__init__(message)


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")

    try:
        scores_string: list[str] = sys.argv[1:]
        if not scores_string:
            raise NoScoresProvidedError()

        scores: list[int] = []
        for score_str in scores_string:
            try:
                scores.append(int(score_str))
            except ValueError:
                print(NonNumericScoreError(score_str))

        if not scores:
            raise NoScoresProvidedError()

        total_players: int = len(scores)
        total_score: int = sum(scores)
        average_score: float = total_score / total_players
        highest_score: int = max(scores)
        lowest_score: int = min(scores)
        score_range: int = highest_score - lowest_score

        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score:.1f}")
        print(f"High score: {highest_score}")
        print(f"Low score: {lowest_score}")
        print(f"Score range: {score_range}")

    except NoScoresProvidedError as e:
        print(f"{e}")
    except ScoreAnalyticsError as e:
        print(f"{e}")
    except ZeroDivisionError as e:
        print(f"Error: Cannot calculate average score - {e}")
    finally:
        print()


if __name__ == "__main__":
    ft_score_analytics()
