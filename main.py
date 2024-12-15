from fastapi import FastAPI

app = FastAPI()   
json={
  "matches": [
    {
      "match_id": "001",
      "tournament": {
        "name": "Australian Open",
        "year": 2024,
        "round": "Final"
      },
      "players": {
        "winner": {
          "name": "Player A",
          "player_id": "A001",
          "seed": 1
        },
        "loser": {
          "name": "Player B",
          "player_id": "B001",
          "seed": 2
        }
      },
      "score": {
        "sets": [
          {
            "set_number": 1,
            "winner_games": 6,
            "loser_games": 4
          },
          {
            "set_number": 2,
            "winner_games": 7,
            "loser_games": 6,
            "tiebreak_winner": True
          }
        ],
        "total_games_won": {
          "winner_games_won": 13,
          "loser_games_won": 10
        }
      },
      "match_stats_url_suffix": "/stats/001"
    },
    {
      "match_id": "002",
      "tournament": {
        "name": "Wimbledon",
        "year": 2024,
        "round": "Semi-Final"
      },
      "players": {
        "winner": {
          "name": "Player C",
          "player_id": "C001",
          "seed": 3
        },
        "loser": {
          "name": "Player D",
          "player_id": "D001",
          "seed": 4
        }
      },
      "score": {
        "sets": [
          {
            "set_number": 1,
            "winner_games": 6,
            "loser_games": 3
          },
          {
            "set_number": 2,
            "winner_games": 5,
            "loser_games": 7
          },
          {
            "set_number": 3,
            "winner_games": 6,
            "loser_games": 2
          }
        ],
        "total_games_won": {
          "winner_games_won": 17,
          "loser_games_won": 12
        }
      },
      "match_stats_url_suffix": "/stats/002"
    }
  ]
}


@app.get("/tennisscore")
def root():
	return json




