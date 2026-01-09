import pendulum

print(pendulum.datetime(2025, 7, 11).int_timestamp)
print(pendulum.datetime(2025, 7, 31).int_timestamp)
print(pendulum.parse('2012-09-05T23:26:11.123789').int_timestamp)