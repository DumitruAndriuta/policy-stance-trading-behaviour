quietly reg investingproximity votingproximity, robust

estimates store REG1

quietly reg investingproximity votingproximity party, robust

estimates store REG2

quietly reg investingproximity votingproximity party state, robust

estimates store REG3

quietly reg investingproximity votingproximity party female state, robust

estimates store REG4

estimates table REG1 REG2 REG3 REG4, b(%10.3f) stats(N r2 r2_a) star(0.05 0.01 0.001)

reg investingproximity votingproximity party female state i.politician1 i.politician2, robust

quietly reg investingproximity votingproximity i.politician1 i.politician2, robust

estimates store REG1

quietly reg investingproximity votingproximity party female state i.politician1 i.politician2, robust

estimates store REG2

quietly reg investingproximity votingproximity state i.politician1 i.politician2, robust

estimates store REG3

quietly reg investingproximity votingproximity party state i.politician1 i.politician2, robust

estimates store REG4

quietly reg investingproximity votingproximity female state i.politician1 i.politician2, robust

estimates store REG5

quietly reg investingproximity votingproximity, robust

estimates store REG6

estimates table REG1 REG2 REG3 REG4 REG5 REG6, b(%10.3f) stats(N r2 r2_a) star(0.05 0.01 0.001)



reg votingproximity party, robust





quietly reg investingproximity votingproximity, robust

estimates store REG1

quietly reg investingproximity votingproximity party state female i.politician1 i.politician2, robust

estimates store REG2

quietly reg investingproximity votingproximity party state i.politician1 i.politician2, robust

estimates store REG3

quietly reg investingproximity votingproximity party female state, robust

estimates store REG4

estimates table REG1 REG2 REG3 REG4, b(%10.3f) stats(N r2 r2_a) star(0.05 0.01 0.001)

reg investingproximity votingproximity party female state, robust
