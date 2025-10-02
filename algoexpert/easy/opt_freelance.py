def optimal_freelancing(jobs):
    DAYS_CNT = 7
    profit = 0
    sorted_jobs = sorted(jobs, key = lambda x: x["payment"], reverse = True)
    timeline = [False] * DAYS_CNT
    for job in sorted_jobs:
        max_time = min(job["deadline"], DAYS_CNT)
        #for ind in range(max_time - 1, -1, -1):
        for ind in reversed(range(max_time)):    
            if timeline[ind] == False:
                timeline[ind] = True
                profit += job["payment"]
                break
    return profit    

def main():
    jobs = [ {"deadline": 8, "payment": 3}, {"deadline": 1, "payment": 1},
            {"deadline": 1, "payment": 2}]
    ans = optimal_freelancing(jobs)
    print(f"ans = {ans}")

if __name__ == "__main__":
    main()    