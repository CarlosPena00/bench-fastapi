sleep 1
for n_users in 10 20 50;do
    rate=$((n_users / 10))
    locust -f src/locust.py --headless --html results/$n_users.html -u $n_users -r $rate -t 2m
    sleep 5
done
