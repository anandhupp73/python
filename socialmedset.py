insta={"Alice","Bob","Charlie","David"}
twitter={"Bob","David","Eve","Frank"}
fb={"Alice","David","Grace","Henry"}
print(insta.union(twitter).union(fb))
print(insta.intersection(twitter).intersection(fb))
print(insta.difference(twitter).difference(fb))