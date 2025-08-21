action_fans={"John","Sarah","Mike","Lisa"}
comedy_fans={"Sarah","Mike","Tom","David"}
drama_fans={"Mike","Lisa","Tom","David"}
print(action_fans.intersection(comedy_fans).intersection(comedy_fans).intersection(drama_fans))
print(action_fans.difference(comedy_fans))
print(action_fans.union(comedy_fans).union(drama_fans))