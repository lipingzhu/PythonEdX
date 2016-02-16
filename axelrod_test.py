import axelrod
strategies = [s() for s in axelrod.ordinary_strategies if s().classifier['stochastic']]
tournament = axelrod.Tournament(strategies)
results = tournament.play()
